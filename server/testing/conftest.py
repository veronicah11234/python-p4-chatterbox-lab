

import pytest
from app import app, db

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))



@pytest.fixture(scope='session')
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        # Establish application context
        with app.app_context():
            # Create all database tables before each test session
            db.create_all()
        yield client

        # Clean up database after each test session
        with app.app_context():
            db.session.remove()
            db.drop_all()
