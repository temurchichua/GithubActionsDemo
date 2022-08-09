from src.app import app
import pytest


class SQLAlchemyMock:
    pass


@pytest.fixture(scope="session")
def application():
    yield app
    # teardown app


@pytest.fixture(scope="session")
def db():
    # DB connection
    return None


@pytest.mark.skip(reason="DB connection is not yet implemented")
def test_db(db):
    assert isinstance(db, SQLAlchemyMock)


def test_demo():
    assert 1 + 1 == 2
