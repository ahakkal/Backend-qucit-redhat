WTF_CSRF_ENABLED = True
SECRET_KEY = 'you will never guess'


import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost/PFA'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
