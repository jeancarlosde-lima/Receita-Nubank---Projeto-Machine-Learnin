# Previsão de Receita para o Nubank (SARIMA)

Este é um projeto de uma aplicação web desenvolvida em Flask que utiliza um modelo de séries temporais (SARIMA) para prever a receita trimestral do Nubank. A aplicação permite que o usuário insira o número de trimestres futuros que deseja prever e exibe os resultados em um gráfico e uma tabela.

## Funcionalidades

-   **Previsão de Receita**: Gera previsões da receita trimestral do Nubank para os próximos 1 a 12 trimestres.
-   **Visualização de Dados**: Exibe os dados históricos e as previsões em um gráfico de linhas interativo.
-   **Tabela de Resultados**: Apresenta uma tabela com os valores previstos, incluindo a média da previsão, o erro padrão e os intervalos de confiança.

## Como Funciona

1.  **Interface do Usuário**: A página inicial (`index.html`) apresenta um formulário onde o usuário pode inserir o número de trimestres que deseja prever.
2.  **Requisição de Previsão**: Ao enviar o formulário, uma requisição POST é enviada para a rota `/prever`.
3.  **Carregamento do Modelo**: A aplicação carrega um modelo SARIMA pré-treinado (do arquivo `model/nubank_sarima.pkl`).
4.  **Geração da Previsão**: O modelo é usado para gerar a previsão para o número de trimestres solicitado.
5.  **Pós-processamento**: Os resultados da previsão são desescalonados para a magnitude correta (milhões de dólares).
6.  **Renderização dos Resultados**: Os dados históricos e previstos são enviados para a página de resultados (`resultado.html`), onde são exibidos em um gráfico (usando Chart.js) e em uma tabela.

## Tecnologias Utilizadas

-   **Back-end**: Python, Flask
-   **Modelo de Machine Learning**: SARIMA (Statsmodels)
-   **Front-end**: HTML, CSS, JavaScript (Chart.js)
-   **Bibliotecas Python**: Pandas, Scikit-learn, Statsmodels

## Como Executar o Projeto

1.  **Ative o Ambiente Virtual**:
    ```bash
    source .venv/bin/activate
    ```

2.  **Execute o Servidor de Desenvolvimento**:
    ```bash
    ./devserver.sh
    ```
    O script irá iniciar o servidor Flask. Você pode acessar a aplicação no painel de visualização do seu IDE ou no navegador.

**Observação**: O modelo `nubank_sarima.pkl` já está treinado e incluído no projeto, então não é necessário treiná-lo novamente para executar a aplicação.
