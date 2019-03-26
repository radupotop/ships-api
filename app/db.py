import peewee as pw
import config

db = pw.PostgresqlDatabase(
    config.DB_NAME, host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS
)
