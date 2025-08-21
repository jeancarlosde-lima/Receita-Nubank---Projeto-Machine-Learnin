import yfinance as yf
import pandas as pd

# Define o ticker para a Nubank
ticker = "NU"

# Cria o objeto Ticker
nu_ticker = yf.Ticker(ticker)

# Pega os dados financeiros trimestrais (demonstração de resultados)
quarterly_financials = nu_ticker.quarterly_financials

# Verifica se os dados foram baixados
if quarterly_financials.empty:
    print(f"Não foi possível baixar os dados financeiros de {ticker}. Verifique o símbolo do ticker.")
else:
    # Transpõe o DataFrame para que as datas sejam as linhas
    quarterly_financials = quarterly_financials.T

    # Filtra para a coluna "Total Revenue" (Receita Total) e remove valores nulos
    if 'Total Revenue' in quarterly_financials.columns:
        revenue = quarterly_financials[['Total Revenue']].dropna()
        revenue.index.name = 'Date'
        
        # Garante que os dados estão em ordem cronológica
        revenue = revenue.sort_index()

        # Salva os dados em um arquivo CSV
        file_path = "nu_historical_revenue.csv"
        revenue.to_csv(file_path)

        print("Dados de Receita Trimestral da Nubank:")
        # Exibe a receita em milhões para melhor legibilidade
        print((revenue / 1e6).to_string(formatters={'Total Revenue': '{:,.2f}M'.format}))
        print(f"\nDados históricos de receita salvos em {file_path}")
    else:
        print("Não foi possível encontrar 'Total Revenue' nos dados financeiros. Colunas disponíveis:")
        print(quarterly_financials.columns)
