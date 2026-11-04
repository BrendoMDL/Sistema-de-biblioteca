# Sistema de Biblioteca

## 1. Sobre o projeto

O Sistema de Biblioteca é uma aplicação web desenvolvida para auxiliar no gerenciamento de livros de uma biblioteca. O projeto possui uma interface frontend integrada a uma API backend, permitindo a comunicação entre a aplicação e o banco de dados.

O projeto também utiliza GitLab CI/CD para automatizar etapas de compilação, testes, análise de qualidade, construção de imagens Docker e solicitação de implantação.

## 2. Tecnologias utilizadas

### Frontend
- React
- TypeScript
- Vite
- Axios
- ESLint

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Uvicorn

### Testes e qualidade
- Pytest
- HTTPX
- Ruff
- ESLint

### DevOps e implantação
- GitLab CI/CD
- Docker
- Render

## 3. Estrutura do projeto

```text
sistema-de-biblioteca/
│
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── Dockerfile
│   └── nginx.conf
│
├── .gitlab-ci.yml
└── README.md
```

## 4. Executando o projeto localmente

### 4.1. Pré-requisitos

- Python 3.12 ou superior.
- Node.js e npm.
- PostgreSQL.
- Git.

### 4.2. Configurando o backend

No terminal, acesse a pasta do backend:

```bash
cd backend
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements-dev.txt
```

Configure a variável de ambiente `DATABASE_URL` com a conexão do banco PostgreSQL local.

Inicie a API:

```bash
uvicorn app.main:app --reload
```

A documentação interativa da API estará disponível em:

http://127.0.0.1:8000/docs

### 4.3. Configurando o frontend

Abra outro terminal e acesse:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

Configure a variável `VITE_API_URL` com o endereço da API backend.

Inicie o frontend:

```bash
npm run dev
```

O Vite exibirá no terminal o endereço local para acessar a aplicação.

## 5. Executando os testes automatizados

Os testes do backend estão localizados em:

```text
backend/tests/
```

Para executar os testes, acesse a pasta backend:

```bash
cd backend
```

Execute:

```bash
python -m pytest -v
```

Atualmente, existem três testes automatizados:

1. `test_rota_inicial`: verifica se a rota principal da API responde corretamente.
2. `test_listar_livros_vazio`: verifica se a listagem retorna uma lista vazia quando não existem livros cadastrados.
3. `test_criar_livro`: verifica se o cadastro de um livro retorna HTTP 201 e os dados esperados.

## 6. Análise de qualidade

O projeto utiliza ferramentas de análise de qualidade para identificar problemas no código.

Backend:

```bash
python -m ruff check app tests
```

Frontend:

```bash
npm run lint
```

## 7. Integração e entrega contínua (GitLab CI/CD)

A configuração do pipeline está no arquivo `.gitlab-ci.yml`, localizado na raiz do repositório.

O pipeline possui cinco etapas:

### Build
Compila o frontend com TypeScript e Vite e verifica a instalação e sintaxe do backend.

### Test
Executa os testes automatizados do backend utilizando Pytest.

### Quality
Executa o ESLint no frontend e o Ruff no backend para verificar a qualidade do código.

### Docker
Constrói as imagens Docker do backend e frontend para validar os respectivos Dockerfiles.

### Deploy
Utiliza os Deploy Hooks do Render para solicitar a implantação do backend e frontend.

O pipeline é executado automaticamente conforme as regras de execução configuradas no GitLab.

## 8. Configuração de variáveis de ambiente

As configurações sensíveis e os endereços utilizados na implantação devem ser configurados por variáveis de ambiente, sem armazenar senhas ou credenciais diretamente no código-fonte.

Principais variáveis utilizadas:

| Variável | Finalidade |
|---|---|
| `DATABASE_URL` | Conexão com o banco de dados PostgreSQL. |
| `FRONTEND_URL` | Endereço do frontend permitido na configuração do backend. |
| `VITE_API_URL` | Endereço da API utilizado pelo frontend. |
| `RENDER_DEPLOY_HOOK_BACKEND` | Solicita a implantação do backend no Render. |
| `RENDER_DEPLOY_HOOK_FRONTEND` | Solicita a implantação do frontend no Render. |

No GitLab, as variáveis de CI/CD são configuradas em:

**Settings → CI/CD → Variables**

## 9. Aplicação publicada

Frontend:

https://biblioteca-frontend-6v2j.onrender.com/

Backend:

https://biblioteca-backend-uip0.onrender.com/

Documentação da API:

https://biblioteca-backend-uip0.onrender.com/docs

## 10. Objetivo do projeto

O projeto tem como objetivo demonstrar o desenvolvimento de uma aplicação web integrada a uma API e a utilização de práticas de integração e entrega contínua.

A implementação do pipeline permite automatizar verificações de compilação, testes, qualidade e construção de imagens Docker, além de solicitar a implantação da aplicação em um ambiente acessível pela internet.