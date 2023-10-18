import psycopg2


def get_db_connection():
    # config
    host = "127.0.0.1"
    user = "postgres"
    password = "admin"
    db_name = "ElectroScooters"

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    return connection
