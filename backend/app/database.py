from sqlmodel import create_engine, SQLModel
from . import settings, models

sqlite_url = f"sqlite:///{settings.db}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)
