# app/Config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

# ruta de la base de datos 
# ruta de la base de datos 
DATABASE_URL = "mysql+pymysql://admin:LFS1ieqpA7bhuCK3W1Xo@db-aquashield-dev.c5guy4ya6433.us-east-2.rds.amazonaws.com:3306/dbaquashielddev"


# Creamos el motor, el cual al comienzo de la ruta de la DB
# Se especifica que es sqlite
engine = create_engine(DATABASE_URL,
                    pool_size= 10, max_overflow= 30
                    )

# Luego creamos los parametros para las sessiones que se creen de dicho motor
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# Creamos el mapeador ORM 
Base = declarative_base()

 # Creamos la función para el uso de session de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()