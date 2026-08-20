import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

load_dotenv()

Base = declarative_base()
postgres_url = os.getenv("POSTGRES_URL")

engine = create_engine(postgres_url, echo=False)

# Session factory for DB transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# FastAPI Dependency for DB sessions
def get_session() -> Session:
    with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]