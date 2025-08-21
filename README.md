# 📊 Previsão de Receita Nubank - Projeto Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com)
[![SARIMA](https://img.shields.io/badge/Model-SARIMA-purple.svg)](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)

> **Projeto acadêmico/portfólio que utiliza Machine Learning para prever a receita trimestral do Nubank (NU) com interface web interativa**

## 🎯 Sobre o Projeto

Este é um projeto de **Machine Learning aplicado a finanças** que demonstra como usar séries temporais para prever receitas corporativas. O objetivo é mostrar o pipeline completo: desde a coleta de dados até a visualização de resultados, utilizando o Nubank como case de estudo.

**O que este projeto faz:**
- Coleta dados financeiros históricos do Yahoo Finance
- Treina um modelo SARIMA para previsão de séries temporais
- Disponibiliza uma interface web simples para interação
- Gera gráficos com previsões e intervalos de confiança

**O que este projeto NÃO é:**
- Uma ferramenta de investimento profissional
- Um sistema de produção empresarial
- Aconselhamento financeiro oficial

## ✨ Funcionalidades

- **Coleta Automática de Dados**: Usa `yfinance` para baixar dados históricos da Nubank
- **Modelo de Séries Temporais**: Implementa SARIMA para capturar tendências e sazonalidade
- **Interface Web Simples**: Flask + HTML/CSS para interação básica
- **Visualização Interativa**: Gráficos com Chart.js mostrando histórico e previsões
- **Validação Estatística**: Intervalos de confiança para as previsões
- **Persistência do Modelo**: Salva o modelo treinado para evitar retreinamento

## 🛠️ Stack Tecnológica

**Backend & Machine Learning:**
```
Python 3.8+
Flask - Web framework leve
pandas - Manipulação de dados
numpy - Computação numérica
statsmodels - Modelo SARIMA
yfinance - Dados financeiros Yahoo
joblib - Serialização do modelo
```

**Frontend:**
```
HTML5 + CSS3 - Interface básica
Chart.js - Gráficos interativos
Vanilla JavaScript - Interações simples
```

## 📂 Estrutura do Projeto

```
projeto-nubank-ml/
├── main.py                    # Aplicação Flask principal
├── requirements.txt           # Dependências Python
├── README.md                  # Este arquivo
├── model/
│   └── nubank_sarima.pkl     # Modelo treinado (gerado automaticamente)
├── static/
│   └── css/
│       └── style.css         # Estilos da interface
└── templates/
    ├── index.html            # Página inicial
    └── resultado.html        # Página de resultados
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Conexão com internet (para baixar dados)

### Instalação

1. **Clone ou baixe o projeto**
   ```bash
   git clone [seu-repositorio]
   cd projeto-nubank-ml
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   python main.py
   ```

5. **Acesse no navegador**
   ```
   http://localhost:8080
   ```

### ⏰ Primeira Execução

Na primeira vez, o sistema irá:
- Baixar dados históricos da Nubank (pode levar ~30 segundos)
- Treinar o modelo SARIMA
- Salvar o modelo na pasta `model/`

Execuções posteriores serão mais rápidas, carregando o modelo já treinado.

## 🧠 Como Funciona o ML

### Modelo SARIMA
**S**easonal **A**uto**R**egressive **I**ntegrated **M**oving **A**verage

- **Sazonal**: Captura padrões que se repetem a cada 4 trimestres
- **Autoregressivo**: Usa valores passados para prever futuros
- **Integrado**: Trabalha com diferenças para tornar dados estacionários
- **Média Móvel**: Considera erros de previsões anteriores

### Pipeline de Dados

1. **Coleta**: yfinance → dados trimestrais da Nubank
2. **Preprocessamento**: 
   - Escala dados (divide por 1M para estabilidade numérica)
   - Verifica consistência temporal
3. **Treinamento**: SARIMA com configuração (1,1,1)×(1,1,1,4)
4. **Previsão**: Gera valores futuros com intervalos de confiança
5. **Pós-processamento**: Reescala valores para bilhões (USD)

### Limitações do Modelo

- **Dados limitados**: Nubank é empresa jovem (IPO em 2021)
- **Volatilidade**: Mercado financeiro tem muita incerteza
- **Mudanças estruturais**: Crescimento explosivo vs. maturação
- **Eventos externos**: Crises, regulamentações, competição

⚠️ **Este projeto é educacional - não use para decisões de investimento!**

## 📊 Interpretando os Resultados

### Gráfico Gerado
- **Linha azul**: Dados históricos reais
- **Linha vermelha**: Previsões do modelo
- **Área sombreada**: Intervalo de confiança (95%)

### Métricas Típicas
- **Amplitude do intervalo**: Maior incerteza = intervalo mais largo
- **Tendência**: Crescimento/declínio da receita prevista
- **Sazonalidade**: Padrões que se repetem trimestralmente

## 🎓 Conceitos Aprendidos

Este projeto demonstra:

**Machine Learning:**
- Séries temporais vs. problemas supervisionados tradicionais
- Importância da sazonalidade em dados financeiros
- Validação de modelos temporais
- Tratamento de dados financeiros reais

**Desenvolvimento Web:**
- Integração ML + Flask
- Serialização/persistência de modelos
- Visualização de dados científicos
- Interface para não-técnicos

**Engenharia de Dados:**
- APIs públicas de dados financeiros
- Preprocessamento e limpeza
- Pipeline automatizado de dados
- Tratamento de erros e exceções

## 🔧 Possíveis Melhorias

**Modelo ML:**
- [ ] Testar outros modelos (Prophet, LSTM)
- [ ] Incluir variáveis externas (PIB, inflação)
- [ ] Validação cruzada temporal mais robusta
- [ ] Ensemble de modelos

**Interface:**
- [ ] Design mais profissional
- [ ] Mais opções de configuração
- [ ] Export de gráficos/dados
- [ ] Comparação com outras empresas

**Dados:**
- [ ] Mais métricas financeiras (lucro, margem)
- [ ] Dados de outras fontes
- [ ] Tratamento de dados faltantes
- [ ] Atualização automática

## 🤝 Contribuições

Este é um projeto educacional aberto a melhorias! Sinta-se livre para:
- Reportar bugs
- Sugerir melhorias
- Fazer fork e experimentar
- Compartilhar insights sobre o modelo

## ⚖️ Disclaimer Legal

**IMPORTANTE**: Este projeto é puramente educacional e demonstrativo.

- ❌ **NÃO** é aconselhamento financeiro
- ❌ **NÃO** garante precisão das previsões  
- ❌ **NÃO** deve ser usado para decisões de investimento
- ✅ **É** um exemplo de ML aplicado a finanças
- ✅ **É** útil para aprender séries temporais
- ✅ **É** um projeto de portfólio

**Invista sempre com responsabilidade e consulte profissionais qualificados.**

## 📄 Licença

MIT License - Use como quiser, mas sem garantias! 😊

---

<div align="center">

**Projeto desenvolvido para fins educacionais e de portfólio**

⭐ Se achou interessante, deixe uma estrela no repositório!

</div>
