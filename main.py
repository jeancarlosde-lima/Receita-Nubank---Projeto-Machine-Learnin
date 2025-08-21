import os
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import pickle
from flask import Flask, render_template, request, jsonify
import traceback

# --- Configuração do App Flask ---
app = Flask(__name__)

# --- Constantes ---
MODEL_PATH = 'model/nubank_sarima.pkl'
TICKER = "NU"
DATA_SCALE = 1e6 # Trabalhar com os dados em milhões para estabilidade numérica

def train_and_save_model():
    print(f"Iniciando download dos dados para {TICKER}...")
    try:
        nu_ticker = yf.Ticker(TICKER)
        financials = nu_ticker.quarterly_financials
        if financials.empty:
            raise ValueError("Não foi possível obter os dados financeiros.")

        revenue = financials.T['Total Revenue'].dropna() / DATA_SCALE
        revenue.index = pd.to_datetime(revenue.index).to_period('Q')
        revenue = revenue.sort_index()
    
        order = (1, 1, 1)
        seasonal_order = (1, 1, 0, 4)
        
        print("Treinando o modelo SARIMA com dados escalados...")
        model = sm.tsa.SARIMAX(revenue, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
    
        print(f"Salvando o modelo em {MODEL_PATH}...")
        with open(MODEL_PATH, 'wb') as pkl:
            pickle.dump(model_fit, pkl)
        
        print("Modelo treinado e salvo com sucesso!")
        return model_fit

    except Exception as e:
        print(f"Ocorreu um erro durante o treinamento: {e}")
        traceback.print_exc()
        return None

def get_model():
    if not os.path.exists(MODEL_PATH):
        print("Modelo não encontrado. Iniciando treinamento...")
        return train_and_save_model()
    else:
        print(f"Carregando modelo existente de {MODEL_PATH}...")
        try:
            with open(MODEL_PATH, 'rb') as pkl:
                return pickle.load(pkl)
        except Exception as e:
            print(f"Erro ao carregar o modelo ({e}). Treinando um novo...")
            traceback.print_exc()
            return train_and_save_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    try:
        modelo = get_model()
        if modelo is None:
            return "Erro: Não foi possível carregar ou treinar o modelo.", 500

        trimestres_a_prever = int(request.form['trimestres'])
        previsao = modelo.get_forecast(steps=trimestres_a_prever)
        previsao_df = previsao.summary_frame(alpha=0.05)
        
        # **CORREÇÃO AQUI**
        # Desescala TODAS as colunas relevantes, incluindo o erro padrão ('mean_se').
        for col in ['mean', 'mean_se', 'mean_ci_lower', 'mean_ci_upper']:
            previsao_df[col] *= DATA_SCALE

        previsao_df.columns = ['Previsão (Média)', 'Erro Padrão', 'IC Inferior', 'IC Superior']

        dados_historicos = pd.Series(modelo.model.endog[:, 0] * DATA_SCALE, index=modelo.model.data.dates.to_timestamp())

        # --- PREPARA DADOS PARA O GRÁFICO INTERATIVO ---
        labels_hist = [d.strftime('%Y-%m-%d') for d in dados_historicos.index]
        labels_prev = [d.strftime('%Y-%m-%d') for d in previsao_df.index.to_timestamp()]
        
        valores_hist = list(dados_historicos.values)
        valores_prev = list(previsao_df['Previsão (Média)'].values)
        ic_inferior = list(previsao_df['IC Inferior'].values)
        ic_superior = list(previsao_df['IC Superior'].values)

        chart_data = {
            "labels": labels_hist + labels_prev,
            "historical": valores_hist,
            "forecast": [None] * len(valores_hist) + valores_prev,
            "ci_lower": [None] * len(valores_hist) + ic_inferior,
            "ci_upper": [None] * len(valores_hist) + ic_superior
        }

        # Formata a tabela para melhor leitura
        tabela_formatada = previsao_df.copy()
        for col in tabela_formatada.columns:
            # Formata todas as colunas como moeda em bilhões, inclusive o erro padrão.
            tabela_formatada[col] = tabela_formatada[col].apply(lambda x: f"${x/1e9:.3f} B")

        return render_template('resultado.html',
                               tabela_previsao=tabela_formatada.to_html(classes='table table-striped text-center', justify='center'),
                               chart_data=chart_data)

    except Exception as e:
        print(f"Erro na rota /prever: {e}")
        traceback.print_exc()
        return f"Ocorreu um erro interno. Verifique os logs para detalhes.", 500

if __name__ == '__main__':
    if not os.path.exists('model'):
        os.makedirs('model')
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
