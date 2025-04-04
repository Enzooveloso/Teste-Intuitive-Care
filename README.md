# Teste de Nivelamento - Intuitive Care

Este repositório contém a solução para o teste de nivelamento proposto pela Intuitive Care, abordando tarefas de **Web Scraping**, **Transformação de Dados**, **Banco de Dados** e **Desenvolvimento de API + Frontend**. O projeto está containerizado com Docker e utiliza tecnologias modernas para garantir performance, escalabilidade e organização de código.

## Etapas do Desafio

### Teste 1 – Web Scraping

- Download dos Anexos I e II (PDFs) do site da ANS.
- Armazenamento na pasta /pdfs/.
- Compactação dos arquivos.

### Teste 2 – Transformação de Dados

- Extração da tabela do Anexo I em PDF.
- Conversão e limpeza dos dados.
- Geração do arquivo .csv tratado.
- Substituição de siglas por nomes completos.
- Compactação do CSV final.

### Teste 3 – Banco de Dados

- Instalação e configuração do MySQL no WSL2.
- Criação do banco de dados ans_dados.

### Teste 4 – API

- Desenvolvimento com *FastAPI*.
- Integração com *MySQL* via *SQLAlchemy*.
- Endpoints criados:
  - GET /operadoras
  - GET /operadoras/{registro_ans}
  - POST /operadoras
  - PUT /operadoras/{registro_ans}
  - DELETE /operadoras/{registro_ans}


---

## Postman

- Foi criada uma *coleção do Postman* com todas as requisições.
- A coleção pode ser importada no Postman para simular as chamadas da API.
- Arquivo: [API_Operadoras_ANS.postman_collections.json](./postman_collection.json) 

## 🚀 Como Executar (Docker)

**Pré-requisitos:**

- Docker + Docker Compose instalados

**Passos:**

```bash
# Subir a aplicação
docker-compose up --build

# A API estará em:
http://localhost:8000

# O frontend Vue (se habilitado) estará em:
http://localhost:5173
```

## 🔬 Testes Automatizados

Execute os testes com `pytest`:

```bash
pytest tests/
```

## ⚙️ Tecnologias Utilizadas

### Backend:

- Python 3.12
- FastAPI
- SQLAlchemy + MySQL Connector

### Banco de Dados:

- MySQL 8 

### Frontend:

- Vue.js + Vite

### Infraestrutura:

- Dockerfile 
- Docker Compose 

### Testes:

- pytest

### Padrão de projeto

- Repository
- Unit Of Work

## 📦 Variáveis de Ambiente

Exemplo de `.env`:

```env
DATABASE_URL=mysql+mysqlconnector://root:1234567@db:3306/ans_dados
```

