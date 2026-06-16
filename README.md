# 🎓 Desafio de Análise de Universidades

## Sobre o Projeto

Este projeto tem como objetivo construir uma pipeline ETL completa utilizando Python e PostgreSQL para processar dados do ranking mundial de universidades de 2023.

Após o carregamento dos dados, são realizadas análises exploratórias utilizando SQL para responder questões relacionadas à estrutura, internacionalização, diversidade e eficiência operacional das instituições.

---

## Objetivos

- Extrair dados de um arquivo CSV.
- Realizar limpeza e transformação dos dados.
- Carregar os dados tratados em um banco PostgreSQL.
- Executar análises SQL sobre os dados processados.
- Demonstrar boas práticas de organização de projetos de dados.

---

## Tecnologias Utilizadas

- Python 3.12+
- Pandas
- NumPy
- PostgreSQL
- SQLAlchemy
- Psycopg2
- Python Dotenv

---

## Arquitetura da Solução

```text
CSV
 │
 ▼
Extract
 │
 ▼
Transform
 │
 ▼
PostgreSQL
 │
 ▼
Consultas SQL Analíticas
```

### Estrutura do Projeto

```text
.
├── Analise_SQL
│   ├── main.py
│   ├── queries
│   └── SQLExecutor.py
│
├── ETL
│   └── src
│       ├── drives
│       ├── infra
│       ├── stages
│       │   ├── extract
│       │   ├── transform
│       │   └── load
│       └── main.py
│
├── requirements.txt
└── README.md
```

---

## Fluxo ETL

### Extract

Responsável pela leitura do dataset original.

Arquivo:

```text
ETL/src/stages/extract/extract_csv.py
```

Atividades:

- Leitura do arquivo CSV.
- Tratamento de encoding.

---

### Transform

Responsável pela limpeza e padronização dos dados.

Arquivo:

```text
ETL/src/stages/transform/transform_data.py
```

Transformações realizadas:

- Remoção de registros duplicados.
- Conversão de colunas numéricas.
- Tratamento de percentuais.
- Criação da coluna `Type`.
- Separação da coluna `Female:Male Ratio`.
- Criação das colunas:
  - `female_pct`
  - `male_pct`
- Geração de datas aleatórias para análises temporais.

---

### Load

Responsável pelo carregamento dos dados no PostgreSQL.

Arquivo:

```text
ETL/src/stages/load/load_to_sql.py
```

Tabela criada:

```sql
universities_ranking
```

---

## Pré-requisitos

Antes de executar o projeto é necessário possuir instalado:

- Python 3.12+
- PostgreSQL 16+
- Git

Verifique as instalações:

```bash
python --version
psql --version
git --version
```

---

## Configuração do Ambiente

### Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd desafio_Analise_universidades
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Linux:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração do Banco de Dados

Criar um arquivo `.env` na raiz do projeto:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=analise_universidade_sql
```

Criar o banco:

```sql
CREATE DATABASE analise_universidade_sql;
```

---

## Executando o ETL

A partir da raiz do projeto:

```bash
python -m ETL.src.main
```

O processo irá:

1. Extrair os dados do CSV.
2. Realizar as transformações.
3. Carregar os dados para o PostgreSQL.

---

## Executando as Análises SQL

Após a carga dos dados:

```bash
python -m Analise_SQL.main
```

As consultas SQL serão executadas automaticamente.

---

## Análises Disponíveis

### Estrutura

- Quantidade de universidades.
- Quantidade de países.
- Média de estudantes por universidade.

### Porte

- Universidades com maior número de estudantes.
- Distribuição do porte das instituições.

### Internacionalização

- Média de estudantes internacionais.
- Universidades mais internacionalizadas.
- Tendências de internacionalização.

### Diversidade

- Distribuição de gênero.
- Instituições com predominância feminina.
- Instituições com predominância masculina.

### Eficiência Operacional

- Relação aluno/professor.
- Correlação entre tamanho da universidade e eficiência operacional.

---

## Dataset

O projeto utiliza dados do ranking mundial de universidades de 2023.

Principais informações disponíveis:

- Ranking da instituição.
- Nome da universidade.
- Quantidade de alunos.
- Relação aluno/professor.
- Percentual de estudantes internacionais.
- Distribuição por gênero.

---

## Possíveis Melhorias Futuras

- Dashboard em Power BI.
- Dockerização da aplicação.
- Testes automatizados.
- Integração contínua (CI/CD).
- Orquestração com Apache Airflow.
- Modelagem em camadas Bronze, Silver e Gold.
- Deploy em ambiente cloud.

---

## Autor

**Rafaela Brícia Ayres Nunes**

- LinkedIn: https://www.linkedin.com/in/rafaela-ayres
- GitHub: https://github.com/RafaBricia