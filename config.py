import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
userName = 'postgres'
password = '8MzbENHeFZ9yTQT7YllH'
host = 'containers-us-west-93.railway.app'
port = '6082'
dbName = 'railway'

# IMPLEMENT DATABASE URL
#  f'postgresql+psycopg2://{userName}:{password}@{host}:{port}/{dbName}'
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:aQapJtzcUsunM2MCpvvK@containers-us-west-74.railway.app:6145/railway"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
