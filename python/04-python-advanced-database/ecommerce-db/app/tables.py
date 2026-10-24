# Import the models so they register their tables with Base.metadata.
import app.models  # noqa: F401
from app.database import Base, engine


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
    print(f"Tables created successfully: {', '.join(Base.metadata.tables)}")


if __name__ == "__main__":
    create_tables()