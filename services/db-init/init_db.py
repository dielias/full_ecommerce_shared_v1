from sqlalchemy import text
from services.shared.database import engine
from services.shared.models import Base  # corrigido aqui

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

if __name__ == "__main__":
    connect_to_db()
    recreate_tables()


