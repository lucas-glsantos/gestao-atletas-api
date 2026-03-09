# Projeto: Desenvolvendo uma API assíncrona com FastAPI
## 🏋️ API de Gestão de Atletas

Esta projeto é uma API Restful assíncrona de gestão de atletas de alto rendimento. É simples, intuitivo e hands-on, Construída com [FastAPI](https://fastapi.tiangolo.com/).

### O que é FastAPI?
FastAPI é uma estrutura web moderna e rápida (de alto desempenho) para criar APIs com Python baseado nos próprios type hints padrões do Python.

#### O que é Assíncrono
Em Ciência da Computação, "assíncrono" refere-se a um modelo onde tarefas são executadas independentemente, sem esperar uma pela outra, permitindo paralelismo e melhor responsividade. Código assíncrono pode iniciar um processo agora e finalizar esse processo posteriormente. Assincronicidade permite que operações demoradas sejam executadas sem 
bloquear o fluxo principal da aplicação, utilizando mecanismos de agendamento e tratamento de resultados futuros.

### 🎯 Objetivo
Este projeto tem como objetivo demonstrar, de forma prática, a construção de uma API moderna em Python, abordando:

- Desenvolvimento de APIs REST assíncronas

- Modelagem de dados relacional

- Validação e serialização de dados

- Dependency Injection

- Versionamento de banco de dados

- Containerização com Docker

- Organização de código orientada a domínio

O projeto também serve como material de portfólio, evidenciando maturidade técnica além de um CRUD básico.

## 🏗️ Arquitetura
O projeto segue uma arquitetura modular por domínio, inspirada em princípios de DDD (Domain-Driven Design):
```bash
gestao_atletas_api/
├── atleta/
├── categorias/
├── centro_treinamento/
├── configs/
├── contrib/
```

### Domínios da Aplicação
Cada domínio segue o mesmo padrão:
```bash
dominio/
├── controller.py  → Endpoints (FastAPI)
├── models.py      → Entidades (SQLAlchemy)
├── schemas.py     → Contratos (Pydantic)
└── __init__.py
```

## 🔗 Modelagem de entidade e relacionamento - MER
![MER](/gestao-atletas-api/mer.jpg "Modelagem de entidade e relacionamento")

### 🧩 Funcionalidades

### Atletas
- Criar atleta
- Listar atletas
- Consultar atleta por ID
- Atualizar dados do atleta
- Remover atleta

Cada atleta está obrigatoriamente associado a:
- Uma Categoria
- Um Centro de Treinamento

### Categorias
- Criar categoria
- Listar categorias
- Consultar categoria por ID

### Centros de Treinamento
- Criar centro de treinamento
- Listar centros de treinamento
- Consultar centro de treinamento por ID


## ⚙️ Stack Tecnológica
- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Docker
- AsyncPG

## 🗃️ Banco de Dados
- Banco relacional PostgreSQL
- Migrações controladas com Alembic
- Relacionamentos bem definidos:
  - Atleta -> Categoria (N:1)
  - Atleta -> Centro de Treinamento (N:1)

## 🐳 Execução com Docker
O projeto foi projetado para rodar exclusivamente em ambiente containerizado.

### Pré-requisitos
Antes de começar, garanta que você tenha instalado:
- Docker
- Docker Compose

### 1. Clonar o repositório
```bash
git clone https://github.com/lukaz-devops/gestao-atletas-api.git
cd gestao-atletas-api
```

### 2. Configurar variáveis de ambiente
Crie ou confirme o arquivo `.env` na raiz do projeto:
```bash
DATABASE_URL=postgresql+asyncpg://gestaoatletas:gestaoatletas@db:5432/gestaoatletas
```

⚠️ Importante:
- "O host `db` funciona somente dentro do Docker"
- "Para execução fora do Docker, usar `localhost`"

### 3. Subir a aplicação com Docker Compose
Na raiz do projeto, execute:
```bash
docker compose up --build
```
O Docker irá:
1. Criar a imagem da API
2. Subir o container do PostgreSQL
3. Subir a API FastAPI
4. Conectar os serviços na mesma rede

### 4. Verificar se a aplicação está rodando
No terminal, você deve ver algo semelhante a:
```bash
Uvicorn running on http://0.0.0.0:8000
```

### 5. Acessar a aplicação
Documentação interativa (Swagger)
```bash
http://localhost:8000/docs
```

Documentação alternativa (ReDoc)
```bash
http://localhost:8000/redoc
```

### 6. Testar os endpoints
Use o Swagger UI para testar:

Exemplos de rotas disponíveis:
- `POST /categorias`
- `POST /centro_treinamento`
- `POST /atleta`
- `GET /atleta`
- `PATCH /atleta/{id}`
- `DELETE /atleta/{id}`

### 7. Banco de dados
- Banco: PostgreSQL
- Executa em container separado
- Dados persistidos via volume Docker
- Migrações gerenciadas via Alembic

### 8. Encerrar a aplicação
Para parar a execução:
```bash
CTRL + C
```

### 9. Derrubar os containers
Após parar o processo, execute:
```bash
docker compose down
```
Isso irá:
- Parar os containers
- Remover a rede criada
- Manter os dados (volume)

### 10. (Opcional) Remover tudo, inclusive dados
Isso apaga o banco de dados
```bash
docker compose down -v
```

Validar qualquer tipo de alteração/atualização
```bash
docker compose build --no-cache
docker compose up 
```

### Fluxo Resumido
```bash
clone -> Configura .env -> docker compose up
      -> Acessa /docs -> Testa API
      -> CTRL + C -> docker compose down
```


`Dockerfile`
- Cria imagem da aplicação
- Instala dependências
- Define comando de inicialização

`docker-compose.yml`
- Sobe:
  - API FastAPI
  - PostgreSQL
- Rede interna entre serviços
- Persistência via volume

### Obeservações Importantes
- A aplicação roda 100% em ambiente containerizado
- Não é necessário instalar Python ou PostgreSQL localmente

## 📄 Documentação da API
A documentação interativa é gerada automaticamente pelo FastAPI:

Swagger UI:

```bash
http://localhost:8000/docs
```

ReDoc:

```bash
http://localhost:8000/redoc
```

## 🛠️ Escalabilidade
Embora atualmente executado em localhost, o projeto foi estruturado para escalar:

- API assíncrona
- Separação clara de domínios
- Pool de conexões com banco de dados
- Pronto para:
  - Escala horizontal da API
  - Load balancers
  - Cache (Redis)
  - Observabilidade
  Evolução para Microsserviços

Nenhuma decisão arquitetural limita crescimento futuro.

## 🧠 Conceitos Técnicos Aprendidos
- Programação assíncrona em Python
- ORM moderno (SQLAlchemy)
- Injeção de dependências
- Separação de responsabilidades
- Arquitetura modular
- Versionamento de bd
- Containerização
- Capacidade de estruturar APIs profissionais
- Compreensão de arquitetura backend

## 👨‍💻 Autor
Projeto desenvolvido by [Lucas Santos](https://www.linkedin.com/in/lucasglsantos/), para fins educacionais e de portfólio, com foco em boas práticas de Software Engineering, backend moderno em Python e arquitetura escalável.