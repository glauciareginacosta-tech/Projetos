# ETL Project: Function Point Analysis – Specialist vs AI Prompt

## Overview
This project implements an **ETL pipeline** designed to process and analyze demands where there is a 
significant disparity between **Function Point Analysis (FPA)** performed by human specialists and FPA 
results generated through **AI prompts**.  

The goal is to measure, compare, and highlight functional size differences between the two approaches, 
providing insights into the reliability and limitations of AI-based counting methods.

## Features
- **Data Extraction**: Collects demand history and functional size metrics.  
- **Transformation**: Applies specific calculations to compare specialist counts with AI-generated counts.  
- **Loading**: Exports processed data into spreadsheets for presentation and reporting.  
- **AI Justification Function**: A playful component where generative AI provides explanations for its
- own counting errors, included for transparency and experimentation.  

## Technologies
- Python (ETL pipeline implementation)  
- Pandas & NumPy (data processing and calculations)  
- Jupyter/Colab Notebooks (execution environment)  
- GitHub for version control and collaboration
- Excel (presentation)  

## How to Run
   git clone https://github.com/glauciareginacosta-tech/TamanhoFuncional.git
   follow the steps in the colab.
   Note: You must provide an active API key in the secret code field to run the AI Justification Function. 
   (For security reasons, GitHub does not allow pushes that contain secret codes.)


## Output
- Comparative analysis of **functional size differences** between specialist and AI counts.  
- Exported spreadsheet containing results for presentation.  

## Notes
- Ensure that **no API keys or secrets** are committed to the repository.  
- The AI justification function is **experimental** and intended for illustrative purposes only.  
