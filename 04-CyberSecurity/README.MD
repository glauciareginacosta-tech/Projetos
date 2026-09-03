# Sistema de Criptografia  de Arquivos
O FileEncryptor é um utilitário em Python projetado para proteger a privacidade e segurança de dados locais. O sistema realiza a criptografia e descriptografia em lote de todos os arquivos contidos em um diretório específico utilizando criptografia simétrica de alta segurança (AES-128 em modo CBC com autenticação HMAC / Fernet).
---
## Funcionalidades
- Geração de Chaves Seguras: Criação de chaves criptográficas aleatórias (`.key`).

- Criptografia em Lote: Cifra automaticamente todos os arquivos de um diretório selecionado.

- Descriptografia em Lote: Reverte os arquivos ao estado original utilizando a chave gerada

- Integridade Garantida: Impede a leitura de arquivos modificados ou corrompidos durante o processo.
---
## Pré-requisitos
- Python 3.8 ou superior.
- Biblioteca `cryptography`.
---
## Instalação das dependências
 - cryptography
---
## Estrutura do Código
O script contém as seguintes funções principais:
- gerar_chave(): Gera uma chave de criptografia Fernet e a salva em um arquivo local (chave.key).
- carregar_chave(): Lê e retorna a chave armazenada em chave.key.
- criptografar_pasta(caminho_pasta, chave): Percorre todos os arquivos da pasta informada e substitui o conteúdo original pelo conteúdo cifrado.
- descriptografar_pasta(caminho_pasta, chave): Lê os arquivos cifrados da pasta e restaura o conteúdo original usando a chave fornecida.
---
## Como Usar
 - Gerar a chave e criptografar a pasta

## Para proteger os arquivos de um diretório:
Efetue a execução das funções de criptografia do sistema de 1 à 6. 
## Atenção
Mantenha o arquivo chave.key em local seguro. Se você perder este arquivo, os dados criptografados não poderão ser recuperados.

 - Descriptografar a pasta com a chave
Para restaurar os arquivos criptografados ao estado original:
Efetue a execução das funções da criptografia: 2 e 4 e posteriormente execute as funções 1 à 3 da descriptografia.
---
## Boas Práticas de Segurança
 - Backup: Crie uma pasta para testar o sistema ou faça backup dos seus dados antes de rodar o script em pastas com informações críticas;
 - Segurança da Chave: Sem a chave correta, a reversão dos arquivos através do processo de descriptografia é computacionalmente inviável. Ou seja, realize a criptografia e descriptografia deste sistema.
-----------------------------------------------
# IN ENGLISH

# File Encryption System
The FileEncryptor is a Python utility designed to protect the privacy and security of local data. The system performs batch encryption and decryption of all files contained within a specified directory using high-security symmetric encryption (AES-128 in CBC mode with HMAC authentication / Fernet).
---
## Features
- Secure Key Generation: Creates random cryptographic keys (.key).
- Batch Encryption: Automatically encrypts all files within a selected directory.
- Batch Decryption: Restores files to their original state using the generated key.
- Guaranteed Integrity: Prevents the reading of files that have been modified or corrupted during the process.
---    
## Prerequisites
- Python 3.8 or higher.
- cryptography library.
---    
## Installing Dependencies
cryptography
---
## Code Structure
The script contains the following main functions:
- gerar_chave(): Generates a Fernet encryption key and saves it to a local file (chave.key).
- carregar_chave(): Reads and returns the key stored in chave.key.
- criptografar_pasta(caminho_pasta, chave): Iterates through all files in the specified directory and replaces their original content with encrypted data.
- descriptografar_pasta(caminho_pasta, chave): Reads the encrypted files in the directory and restores their original content using the provided key.
---    
## Usage
- Generate the Key and Encrypt the Directory
To protect the files within a directory:
   Execute the system's encryption functions from 1 to 6.
##Warning: 
Keep the chave.key file in a secure location. If this file is lost, the encrypted data cannot be recovered.

- Decrypt the Directory
To restore the encrypted files to their original state:
   Execute encryption functions 2 and 4, and subsequently execute decryption functions 1 to 3.
---
## Security Best Practices
- Backup: Create a test folder to evaluate the system, or back up your data prior to running the script on directories containing critical information.
- Key Security: Without the correct key, reversing the file encryption process is computationally infeasible. Ensure that you perform both the encryption and decryption processes using this system.

