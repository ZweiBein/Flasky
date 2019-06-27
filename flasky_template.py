import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role
from decouple import config as env_config

app = create_app(env_config('FLASK_CONFIG', default='default'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
