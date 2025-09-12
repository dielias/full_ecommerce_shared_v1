from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "postgresql://ecommerce:my_password@toxiproxy:5432/ecommerce"

# users/database.py
DATABASE_URL = "postgresql+psycopg2://ecommerce:my_password@toxiproxy:8475/ecommerce"

# products/database.py
DATABASE_URL = "postgresql+psycopg2://ecommerce:my_password@toxiproxy:8476/ecommerce"

# orders/database.py
DATABASE_URL = "postgresql+psycopg2://ecommerce:my_password@toxiproxy:8477/ecommerce"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
