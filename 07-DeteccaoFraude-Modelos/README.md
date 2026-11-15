                                       This README is available in English and Portuguese.
   
# Fraud Detection in Transactions Project - Data Science

## Purpose
The aim of this project is to explore and evaluate various supervised classification models for detecting fraud in credit card transactions. The dataset used is already categorized, with the variable "Class" indicating whether the transaction is fraudulent (1) or not (0).

## Project Flow

### 1. Data Import
The first step involves importing the credit card transaction data, which contains relevant information for the analysis.

### 2. Analysis of "Class" Variable Proportion
A preliminary analysis will be conducted to verify if the dataset is balanced. Identifying the proportion of fraudulent transactions compared to non-fraudulent ones is essential for model selection and evaluation.

### 3. Feature Engineering
In this stage, transformations and selections of relevant variables will be made to improve the performance of the classification models.

### 4. Data Segregation
The data will be split into training and testing sets. This separation is crucial for appropriately validating model performance.

## Classification Models

### Model 1: Logistic Regression
- **Model Evaluation**:
  - **ROC Curve**: The ROC curve will be generated to visualize the true positive rate against the false positive rate.
  - **Precision Recall Curve**: This curve will be used to evaluate the model's precision regarding its recall capability.

### Model 2: Random Forests
- **Model Evaluation**:
  - **ROC Curve**: Similar to the previous model, the ROC curve will be generated to assess model performance.
  - **Precision Recall Curve**: The model's effectiveness will also be measured using this curve.

### Model 3: XGBoost
- **Model Evaluation**:
  - **ROC Curve**: The ROC curve will be used to visualize the model's performance.
  - **Precision Recall Curve**: Precision and recall analysis will be conducted using this curve.

## Conclusion
At the end of the project, we will identify which model performed best in detecting fraud.

---
#Em Português
# Projeto de Detecção de Fraude em Transações - Ciência de Dados

## Propósito
O objetivo deste projeto é explorar e avaliar diversos modelos de classificação supervisionada para a detecção de fraudes em transações de cartão de crédito. Os dados utilizados já estão categorizados, sendo que a variável "Class" indica se a transação é fraudulenta (1) ou não (0).

## Fluxo do Projeto

### 1. Importação de Dados
O primeiro passo consiste na importação dos dados de transações de cartão de crédito, que contêm informações relevantes para a análise.

### 2. Análise da Proporção da Variável "Class"
Uma análise preliminar será realizada para verificar se a base de dados está balanceada. A identificação da proporção de transações fraudulentas em relação às não fraudulentas é essencial para a seleção e avaliação dos modelos.

### 3. Feature Engineering
Nesta etapa, serão realizadas transformações e seleções de variáveis relevantes, visando melhorar o desempenho dos modelos de classificação.

### 4. Segregação de Dados
Os dados serão divididos em conjuntos de treino e teste. Essa separação é crucial para validar a performance dos modelos de forma adequada.

## Modelos de Classificação

### Modelo 1: Regressão Logística
- **Avaliação do Modelo**:
  - **ROC Curve**: Será gerada a curva ROC para visualizar a taxa de verdadeiros positivos em relação à taxa de falsos positivos.
  - **Precision Recall Curve**: Esta curva será utilizada para avaliar a precisão do modelo em relação à sua capacidade de recuperação.

### Modelo 2: Florestas Aleatórias
- **Avaliação do Modelo**:
  - **ROC Curve**: Assim como no modelo anterior, a curva ROC será gerada para avaliar o desempenho do modelo.
  - **Precision Recall Curve**: A eficácia do modelo será medida também por meio desta curva.

### Modelo 3: XGBoost
- **Avaliação do Modelo**:
  - **ROC Curve**: A curva ROC será utilizada para visualizar a performance do modelo.
  - **Precision Recall Curve**: A análise de precisão e recuperação será feita através desta curva.

## Conclusão
Ao final do projeto, identificamos qual foi o modelo que teve o melhor desempenho para identificar fraudes.

