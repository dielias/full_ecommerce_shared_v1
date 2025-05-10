 Full Ecommerce API - Microservices Architecture

Este projeto é uma aplicação de e-commerce implementada com arquitetura de microserviços, utilizando **Python** e **FastAPI**, e um padrão de banco de dados compartilhado. 

## 🧱 Estrutura do Projeto

```
.
├── docker-compose.yml
├── services
│   ├── users               # Microserviço de usuários
│   ├── products            # Microserviço de produtos
│   ├── orders              # Microserviço de pedidos
│   └── db-init             # Inicialização dos bancos
│   └── shared              # 
├── tests                   # Testes automatizados
```

Cada microserviço possui seu próprio banco de dados PostgreSQL e API independente.

## 🚀 Como Executar

### Pré-requisitos

- Docker
- Docker Compose
- Python 3.12

### Subir os serviços

```bash
docker compose up --build
```

Isso inicializa todos os serviços e bancos de dados. A aplicação estará disponível nos seguintes endpoints:

| Serviço      | Porta | Endereço Base         |
|--------------|-------|------------------------|
| Users        | 8001  | `http://localhost:8001` |
| Products     | 8002  | `http://localhost:8002` |
| Orders       | 8003  | `http://localhost:8003` |

## 🔌 Endpoints

### Users

- `GET /users` - List users
- `GET /users/{user_id}` - Get user by user_id
- `POST /users` - Create user 
- `PUT /users/{user_id}` - Update user 
- `DELETE /users/{user_id}` - Delete user 

### Products

- `GET /products` - List products 
- `GET /products/{product_id}` - Get product by product_id
- `POST /products` - Create product
- `PUT /products/{product_id}` - Update product
- `DELETE /products/{product_id}` - Delete product

### Orders

- `GET /orders` - List product 
- `GET /orders/{order_id}` - Get product by order_id
- `POST /orders` - Create order 
- `PUT /orders/{order_id}` - Update order 
- `DELETE /orders/{order_id}` - Delete order 

## 🧪 Testes

Para rodar os testes (fora do docker):

```bash
cd tests
pytest
```

## 📦 Tecnologias

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- Pydantic
- Pytest

## 🛠️ Arquitetura

- **Microserviços**: Cada serviço (User, Product e Order) é um microserviço.
- **Shared Database**: Todos os serviços compartilham o mesmo banco de dado Postgres.


## 📝 Licença

Este projeto está licenciado sob a licença MIT.

## 🧑‍💻 Autor

Desenvolvido por Dinah (https://github.com/dielias)
