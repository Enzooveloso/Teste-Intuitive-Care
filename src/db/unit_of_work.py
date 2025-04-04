from contextlib import contextmanager
from collections.abc import Generator
from sqlalchemy.orm import Session
from src.db.database import SessionLocal

@contextmanager
def unit_of_work() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
