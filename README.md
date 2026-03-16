# Metadata Management System

A backend service for managing **dataset metadata and lineage relationships** built using **FastAPI, PostgreSQL, SQLAlchemy, and Alembic**.

The system allows users to:

* Store dataset metadata
* Track dataset lineage (upstream / downstream)
* Search datasets by name or column
* Prevent invalid lineage cycles (DAG validation)

---

# Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Alembic migrations
* Docker & Docker Compose
* Python 3.10+

---

# Project Structure

```
project/
│
├── api/
│   ├── dataset_routes.py
│   ├── lineage_routes.py
│   └── search_routes.py
│
├── core/
│   ├── config.py
│   └── database.py
│
├── models/
│   ├── dataset.py
│   ├── column.py
│   └── lineage.py
│
├── schemas/
│   ├── dataset_schema.py
│   ├── column_schema.py
│   └── lineage_schema.py
│
├── services/
│   ├── dataset_service.py
│   ├── lineage_service.py
│   └── search_service.py
│
├── utils/
│   └── graph_utils.py
│
├── alembic/
├── main.py
├── docker-compose.yml
├── Dockerfile
├── alembic.ini
└── .env
```

---

# Dataset Model

Each dataset represents a table in a data system.

Example FQN:

```
connection.database.schema.table
```

Example:

```
snowflake_prod.sales.public.orders
```

Dataset fields:

* id
* fqn
* connection_name
* database_name
* schema_name
* table_name
* source_type

---

# Column Model

Columns belong to a dataset.

Example:

```
[
  {"name": "order_id", "type": "int"},
  {"name": "customer_id", "type": "int"}
]
```

---

# Lineage

Lineage represents dataset dependencies.

Example:

```
orders_raw → orders_clean → orders_aggregated
```

Rules:

* Graph must be **Directed Acyclic Graph (DAG)**
* Cycles are rejected

Example invalid:

```
A → B → C
C → A ❌
```

Error returned:

```
Cycle detected in lineage graph
```

---

# API Endpoints

## Create Dataset

POST `/datasets`

Example request:

```json
{
  "fqn": "snowflake.sales.public.orders",
  "connection_name": "snowflake",
  "database_name": "sales",
  "schema_name": "public",
  "table_name": "orders",
  "source_type": "PostgreSQL",
  "columns": [
    {"name": "order_id", "type": "int"},
    {"name": "customer_id", "type": "int"}
  ]
}
```

Response:

```json
{
  "message": "Dataset inserted successfully"
}
```

---

## Add Lineage

POST `/lineage`

Request:

```json
{
  "upstream_dataset_id": 1,
  "downstream_dataset_id": 2
}
```

Response:

```json
{
  "message": "Lineage inserted successfully"
}
```

---

## Get Upstream Datasets

GET `/datasets/{id}/upstream`

Example:

```
GET /datasets/2/upstream
```

---

## Get Downstream Datasets

GET `/datasets/{id}/downstream`

Example:

```
GET /datasets/1/downstream
```

---

## Search Datasets

GET `/search?q=keyword`

Search priority:

1. Table name
2. Column name
3. Schema name
4. Database name

Example:

```
/search?q=order
```

---

# Database Setup

Create PostgreSQL database:

```
metadata_db
```

Example `.env`

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/metadata_db
```

---

# Run with Docker

Start services:

```
docker-compose up --build
```

API will run at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

# Database Migrations

Generate migration:

```
alembic revision --autogenerate -m "initial tables"
```

Apply migration:

```
alembic upgrade head
```

---

# Example Data Flow

```
orders_raw
     ↓
orders_clean
     ↓
orders_aggregated
```

---

# Future Improvements

* Authentication
* Pagination
* Async database queries
* Graph visualization
* Column-level lineage

---

# Author

Backend implementation using **FastAPI + PostgreSQL + SQLAlchemy**.
