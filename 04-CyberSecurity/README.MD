                               This README is available in English and Portuguese.

# Sistema de Criptografia de Arquivos (FileEncryptor)

O **FileEncryptor** é um utilitário em Python projetado para proteger a privacidade e segurança de dados locais. O sistema realiza criptografia e descriptografia em lote de todos os arquivos contidos em um diretório específico, utilizando criptografia simétrica de alta segurança (AES-128 em modo CBC com autenticação HMAC, implementado via Fernet).

---

## Funcionalidades

- **Geração de Chaves Seguras:** Cria chaves criptográficas aleatórias (`.key`) para uso no sistema.
- **Criptografia em Lote:** Cifra automaticamente todos os arquivos de um diretório selecionado.
- **Descriptografia em Lote:** Restaura os arquivos ao seu estado original usando a chave gerada.
- **Integridade Garantida:** Impede a leitura de arquivos que tenham sido modificados ou corrompidos durante o processo, garantindo a autenticidade dos dados.

---

## Pré-requisitos

- Python 3.8 ou superior   This README is available in English and Portuguese.

# Sistema de Criptografia de Arquivos (FileEncryptor)

O **FileEncryptor** é um utilitário em Python projetado para proteger a privacidade e segurança de dados locais. O sistema realiza criptografia e descriptografia em lote de todos os arquivos contidos em um diretório específico, utilizando criptografia simétrica de alta segurança (AES-128 em modo CBC com autenticação HMAC, implementado via Fernet).

---

## Funcionalidades

- **Geração de Chaves Seguras:** Cria chaves criptográficas aleatórias (`.key`) para uso no sistema.
- **Criptografia em Lote:** Cifra automaticamente todos os arquivos de um diretório selecionado.
- **Descriptografia em Lote:** Restaura os arquivos ao seu estado original usando a chave gerada.
- **Integridade Garantida:** Impede a leitura de arquivos que tenham sido modificados ou corrompidos durante o processo, garantindo a autenticidade dos dados.

---

## Pré-requisitos

- Python 3.8 ou superior  
- Biblioteca `cryptography` (instalável via `pip`)

---

## Instalação das Dependências

Execute o comando abaixo para instalar a biblioteca necessária:

```bash
pip install cryptography
```

---

## Estrutura do Código

O script principal contém as seguintes funções:

- `gerar_chave()`: Gera uma chave de criptografia Fernet e a salva em um arquivo (`chave.key`).
- `carregar_chave()`: Carrega a chave armazenada no arquivo `chave.key`.
- `criptografar_pasta(caminho_pasta, chave)`: Criptografa todos os arquivos presentes na pasta especificada.
- `descriptografar_pasta(caminho_pasta, chave)`: Restaura os arquivos criptografados ao seu estado original usando a chave.

---

## Como Usar

### Para proteger os arquivos de um diretório:

1. **Gerar a chave de criptografia**:

```python
gerar_chave()
```

2. **Criptografar a pasta desejada**:

```python
caminho = 'caminho/para/sua/pasta'
chave = carregar_chave()
criptografar_pasta(caminho, chave)
```

### Para restaurar os arquivos ao estado original:

1. **Carregar a chave**:

```python
chave = carregar_chave()
```

2. **Descriptografar a pasta**:

```python
descriptografar_pasta(caminho, chave)
```

---

## Recomendações e Cuidados

- **Armazenamento Seguro da Chave:** Mantenha o arquivo `chave.key` em local seguro. Se perdê-lo, a recuperação dos arquivos criptografados será inviável.
- **Backup:** Antes de executar operações de criptografia em pastas com dados críticos, faça backups ou utilize uma pasta de teste.
- **Segurança da Chave:** A chave é essencial para descriptografar os arquivos. Nunca compartilhe ou perca esta chave.

---

## Resumo do Processo

| Ação                     | Passo | Descrição                                          |
|--------------------------|---------|------------------------------------------------------|
| Gerar chave             | 1       | Executar `gerar_chave()` para criar e salvar a chave|
| Criptografar pasta      | 2       | Executar `criptografar_pasta()` com a chave carregada |
| Manter a chave segura   | 3       | Guardar `chave.key` em local seguro                 |
| Descriptografar pasta   | 4       | Executar `descriptografar_pasta()` com a chave carregada |

---

## Observações Finais

- Utilize o sistema com cuidado, especialmente em pastas com dados importantes.
- A segurança do processo depende do armazenamento adequado da chave.
- Para mais informações ou suporte, consulte a documentação do seu projeto ou entre em contato.

---

Se desejar, posso gerar uma versão em inglês ou adaptar ainda mais o conteúdo.
