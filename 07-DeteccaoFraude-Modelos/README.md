                                       This README is available in English and Portuguese.

#  Fraud Detection Project - Data Science

## Purpose
The objective of this project is to explore and evaluate various supervised classification models for the detection of fraud in credit card transactions. The data utilized is categorized, and the "Class" variable indicates whether the transaction is fraudulent (1) or not (0).

## Project Flow

1. **Data Importation**
   - Importing the credit card transaction data, which contains relevant information for analysis.

2. **Analysis of the "Class" Variable Proportion**
   - Preliminary analysis to verify the balance of the dataset. Identification of the proportion of fraudulent transactions in relation to non-fraudulent ones, which is essential for the selection and evaluation of the models.

3. **Feature Engineering**
   - Performing transformations and selections of relevant variables to enhance the performance of the classification models.

4. **Data Segregation**
   - Dividing the data into training and testing sets, which is crucial for appropriately validating the performance of the models.

## Classification Models

### Model 1: Logistic Regression
- **Model Evaluation:**
  - **Classification Report:** A table containing the count of correct and incorrect predictions, comparing actual classes with predicted ones. Evaluation Metrics: Accuracy, precision, recall, F1 Score.
  - **ROC Curve:** Visualization of the true positive rate in relation to the false positive rate.
  - **Precision-Recall Curve:** Assessment of the model's precision in relation to its recall capability.

### Model 2: Random Forests
- **Model Evaluation:**
  - **Classification Report**
  - **ROC Curve**
  - **Precision-Recall Curve**

### Model 3: XGBoost
- **Model Evaluation:**
  - **Classification Report**
  - **ROC Curve**
  - **Precision-Recall Curve**

## Conclusion
At the conclusion of the project, we identified the model with the best performance for the detection of fraud in credit card transactions.

## System Used
The project was developed and executed in Google Colab. <img src="https://github.com/glauciareginacosta-tech/Projetos/blob/main/07-DeteccaoFraude-Modelos/colab.png" alt="Colab" width="25" />

### Step-by-Step Guide to Running the System in Google Colab
1. Open one of the `*.ipynb` files in Google Colab (note that both are identical; however, one contains text and comments in Portuguese while the other is in English).
2. Upload the `FDTimePrediction.xlsx` file to Colab.
3. Execute the system. 

---

# Projeto de Detecção de Fraude em Transações - Ciência de Dados

## Propósito
O objetivo deste projeto é explorar e avaliar diversos modelos de classificação supervisionada para a detecção de fraudes em transações de cartão de crédito. Os dados utilizados são categorizados e a variável "Class" indica se a transação é fraudulenta (1) ou não (0).

## Fluxo do Projeto

1. **Importação de Dados**
   - Importação dos dados de transações de cartão de crédito, que contêm informações relevantes para análise.

2. **Análise da Proporção da Variável "Class"**
   - Análise preliminar para verificar a balanceamento da base de dados. Identificação da proporção de transações fraudulentas em relação às não fraudulentas, essencial para a seleção e avaliação dos modelos.

3. **Feature Engineering**
   - Realização de transformações e seleções de variáveis relevantes para melhorar o desempenho dos modelos de classificação.

4. **Segregação de Dados**
   - Divisão dos dados em conjuntos de treino e teste, crucial para validar a performance dos modelos de forma adequada.

## Modelos de Classificação

### Modelo 1: Regressão Logística
- **Avaliação do Modelo:**
  - **Relatório de Classificação:** Tabela com a contagem de previsões corretas e incorretas, comparando classes reais com as previstas. Métricas de Avaliação: Acurácia, precisão, revocação, F1 Score.
  - **Curva ROC:** Visualização da taxa de verdadeiros positivos em relação à taxa de falsos positivos.
  - **Curva de Precisão e Revocação:** Avaliação da precisão do modelo em relação à sua capacidade de recuperação.

### Modelo 2: Florestas Aleatórias
- **Avaliação do Modelo:**
  - **Relatório de Classificação**
  - **Curva ROC**
  - **Curva de Precisão e Revocação**

### Modelo 3: XGBoost
- **Avaliação do Modelo:**
  - **Relatório de Classificação**
  - **Curva ROC**
  - **Curva de Precisão e Revocação**

## Conclusão
Ao final do projeto, identificamos o modelo com o melhor desempenho para a detecção de fraudes em transações de cartão de crédito.

## Sistema Utilizado
O projeto foi desenvolvido e executado no Google Colab. <img src="https://github.com/glauciareginacosta-tech/Projetos/blob/main/07-DeteccaoFraude-Modelos/colab.png" alt="Colab" width="25" />

### Passo a Passo para Executar o Sistema no Google Colab
1. Abra um dos arquivos `*.ipynb` no Google Colab (observação ambos são iguais, entretanto um está com com textos e comentários em português e outro em inglês).
2. Anexe o arquivo `FDTimePrediction.xlsx` no Colab.
3. Execute o sistema. 

---
