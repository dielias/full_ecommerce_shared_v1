from sqlalchemy import text
from sqlalchemy.orm import Session
from shared.database import engine, Base
from shared.models import User, Product, Order  # Importando todos os models

def connect_to_db():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        raise

def recreate_tables():
    print("🧹 Dropando todas as tabelas...")
    Base.metadata.drop_all(bind=engine)
    print("✅ Tabelas antigas apagadas!")

    print("🛠️  Criando tabelas novas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas com sucesso!")

def seed_data():
    session = Session(bind=engine)
    try:
        print("🌱 Inserindo dados de exemplo...")

        user = User(name="Admin", email="admin@example.com")
        product = Product(name="Produto Teste", price=99)

        session.add_all([user, product])
        session.commit()
        print("✅ Dados inseridos com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao inserir dados de exemplo: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    connect_to_db()
    recreate_tables()
    seed_data()

