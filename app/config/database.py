import os
import sys
import urlparse

class DBConfig(object):
 
    DB_ON = True
    DB_DRIVER = 'mysql'
    DB_ORM = False


class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'baseball'
    DB_HOST = 'localhost'
   
    DB_OPTIONS = {
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }


class StagingDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'baseball'
    DB_HOST = 'localhost'


class ProductionDBConfig(DBConfig):
    if 'CLEARDB_DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])

        # Ensure default database exists.
        # DATABASES['default'] = DATABASES.get('default', {})

        # Update with environment configuration.
        # DATABASES['default'].update({
        #     'NAME': url.path[1:],
        #     'USER': url.username,
        #     'PASSWORD': url.password,
        #     'HOST': url.hostname,
        #     'PORT': url.port,
        # })

    DB_USERNAME = url.username
    DB_PASSWORD = url.password
    DB_DATABASE_NAME = url.path[1:]
    DB_HOST = url.hostname

