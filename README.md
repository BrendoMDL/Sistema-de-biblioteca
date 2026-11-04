# Sistema de Biblioteca

## 1. Sobre o projeto

O Sistema de Biblioteca é uma aplicação web desenvolvida para auxiliar no gerenciamento de livros de uma biblioteca.

O projeto possui uma interface frontend integrada a uma API backend, responsável pela comunicação com o banco de dados e pelo processamento das operações da aplicação.

Além do desenvolvimento da aplicação, o projeto implementa um processo de Integração Contínua e Entrega Contínua (CI/CD), utilizando GitLab CI/CD para automatizar etapas de compilação, testes automatizados, análise de qualidade, construção e publicação de imagens Docker e solicitação de implantação.

## 2. Tecnologias utilizadas

### Frontend
- React
- TypeScript
- Vite
- Axios
- ESLint
- Nginx

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
- GitLab
- GitLab CI/CD
- Docker
- GitLab Container Registry
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
│   ├── package-lock.json
│   ├── Dockerfile
│   └── nginx.conf
│
├── .gitlab-ci.yml
├── .gitignore
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

Configure as variáveis de ambiente necessárias:

- `DATABASE_URL`: endereço de conexão com o PostgreSQL.
- `FRONTEND_URL`: endereço do frontend autorizado pelo backend.

Inicie a API:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

http://127.0.0.1:8000

A documentação interativa estará disponível em:

http://127.0.0.1:8000/docs

### 4.3. Configurando o frontend

Abra outro terminal e acesse a pasta do frontend:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

Configure a variável de ambiente:

- `VITE_API_URL`: endereço da API backend.

Inicie o frontend:

```bash
npm run dev
```

O Vite exibirá no terminal o endereço local para acessar a aplicação.

## 5. Testes automatizados

Os testes automatizados do backend estão localizados em:

```text
backend/tests/
```

Para executar os testes, acesse a pasta do backend:

```bash
cd backend
```

Execute:

```bash
python -m pytest -v
```

O projeto possui três testes automatizados:

1. `test_rota_inicial`: verifica se a rota principal da API responde corretamente.
2. `test_listar_livros_vazio`: verifica se a listagem retorna uma lista vazia quando não existem livros cadastrados.
3. `test_criar_livro`: verifica se o cadastro de um livro retorna HTTP 201 e os dados esperados.

Os testes são executados automaticamente durante a etapa `test_backend` do pipeline.

## 6. Análise de qualidade

O projeto utiliza ferramentas específicas para verificar a qualidade do código e identificar possíveis problemas.

### Backend

Utiliza Ruff:

```bash
python -m ruff check app tests
```

### Frontend

Utiliza ESLint:

```bash
npm run lint
```

Essas verificações são executadas automaticamente durante a etapa de qualidade do pipeline.

## 7. Integração e entrega contínua (GitLab CI/CD)

O projeto utiliza GitLab CI/CD para automatizar as principais etapas do processo de desenvolvimento.

A configuração está armazenada no arquivo `.gitlab-ci.yml`, localizado na raiz do repositório.

O pipeline é organizado em cinco etapas:

### 7.1. Build

Responsável por preparar e verificar a compilação das aplicações.

- Instala as dependências do frontend.
- Executa a compilação do frontend utilizando Vite.
- Instala as dependências de desenvolvimento do backend.
- Verifica a compilação dos arquivos Python.

### 7.2. Test

Executa os testes automatizados do backend utilizando Pytest.

Essa etapa verifica se as principais funcionalidades testadas continuam funcionando corretamente após as alterações no código.

### 7.3. Quality

Executa as ferramentas de análise de qualidade:

- ESLint: verifica o código do frontend.
- Ruff: verifica o código do backend.

O objetivo é identificar problemas de padronização e possíveis erros antes da publicação.

### 7.4. Docker

Constrói as imagens Docker do frontend e do backend.

Após a construção, nas execuções de pipeline associadas a branches, as imagens são publicadas no GitLab Container Registry.

As imagens recebem uma identificação baseada no hash curto do commit:

```text
biblioteca-backend:<commit>
biblioteca-frontend:<commit>
```

Isso permite relacionar cada imagem à versão do código que a originou.

Em pipelines de Merge Request, as imagens são construídas para validação, mas não são publicadas no registro.

### 7.5. Deploy

Utiliza os Deploy Hooks do Render para solicitar a implantação do frontend e do backend.

Essa etapa é executada somente na branch `publicar-seguro`, desde que as duas variáveis de implantação estejam configuradas no GitLab.

O pipeline realiza a solicitação de implantação dos serviços hospedados no Render.

**Observação:** a publicação das imagens no GitLab Container Registry e a solicitação de implantação pelo Render são operações distintas. O pipeline constrói e publica as imagens no registro e também aciona os serviços configurados no Render.

## 8. Gatilhos de execução do pipeline

O pipeline utiliza regras definidas no arquivo `.gitlab-ci.yml`.

Os principais gatilhos são:

- **Push:** executa o pipeline quando alterações são enviadas para uma branch.
- **Merge Request:** executa o pipeline para verificar alterações antes da integração entre branches.
- **Deploy:** ocorre exclusivamente na branch `publicar-seguro`, quando as variáveis necessárias estão disponíveis.

As regras também evitam a execução duplicada de pipelines de push quando já existe um Merge Request aberto para a branch.

## 9. Variáveis de ambiente e segurança

As informações sensíveis não devem ser armazenadas diretamente no código-fonte ou no arquivo `.gitlab-ci.yml`.

As principais variáveis utilizadas são:

| Variável | Finalidade |
|---|---|
| `DATABASE_URL` | Endereço de conexão com o PostgreSQL. |
| `FRONTEND_URL` | Endereço do frontend autorizado pelo backend. |
| `VITE_API_URL` | Endereço da API utilizado pelo frontend. |
| `RENDER_DEPLOY_HOOK_BACKEND` | Aciona a implantação do backend no Render. |
| `RENDER_DEPLOY_HOOK_FRONTEND` | Aciona a implantação do frontend no Render. |

As variáveis de CI/CD utilizadas pelo pipeline são configuradas no GitLab em:

**Settings → CI/CD → Variables**

As credenciais e os endereços secretos dos Deploy Hooks devem permanecer protegidos nessa configuração, sem serem publicados no repositório.

O GitLab também disponibiliza variáveis predefinidas para autenticação e publicação das imagens no Container Registry.

## 10. Demonstração de falha e correção

Para demonstrar o funcionamento dos testes automatizados, foi realizado um teste controlado de falha.

Na demonstração, uma asserção do teste `test_criar_livro` foi alterada propositalmente para esperar um código HTTP incorreto.

Como resultado:

1. O teste automatizado identificou a divergência.
2. A etapa de testes do pipeline falhou.
3. O pipeline apresentou resultado vermelho.
4. A asserção foi corrigida para esperar o código HTTP 201.
5. Uma nova execução foi realizada.
6. O pipeline voltou a apresentar resultado verde.

Essa demonstração comprova que o processo de CI/CD identifica falhas antes de permitir a continuidade das etapas dependentes.

## 11. Aplicação publicada

O projeto está hospedado no Render.

### Frontend

https://biblioteca-frontend-6v2j.onrender.com/

### Backend

https://biblioteca-backend-uip0.onrender.com/

### Documentação interativa da API

https://biblioteca-backend-uip0.onrender.com/docs

## 12. Objetivo do projeto

O projeto tem como objetivo demonstrar o desenvolvimento de uma aplicação web integrada a uma API e a implementação de práticas de Integração Contínua e Entrega Contínua.

A utilização do GitLab CI/CD permite automatizar verificações de compilação, execução de testes, análise de qualidade, construção e publicação de imagens Docker e solicitação de implantação da aplicação.

Com isso, o projeto demonstra como a automação pode contribuir para a identificação antecipada de erros, a padronização do processo de desenvolvimento e a entrega de versões da aplicação em um ambiente acessível pela internet.