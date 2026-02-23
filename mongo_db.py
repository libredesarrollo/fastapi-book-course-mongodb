from db_connection import mongo_client

# Define la base de datos que contendrá todas las colecciones de nuestra aplicación.
# La librería motor la creará automáticamente si no existe.
database = mongo_client.task_manager

def get_mongo_database():
    """Devuelve la base de datos que se usará como dependencia."""
    return database
