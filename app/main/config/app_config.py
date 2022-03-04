import os


db_uri = "mysql+pymysql://{}:{}@{}:3306/{}".format(os.getenv('DB_USER'), os.getenv('DB_PASSWD'), os.getenv('DB_HOST'), os.getenv('DB'))
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'apiserver_for_registered_project')
	DEBUG = False


class DevelopmentConfig(Config):
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = db_uri
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = db_uri
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = db_uri


config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY