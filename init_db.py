# init_db.py
from models.database import get_db_connection


# creates db from scratch
def init_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
            CREATE TABLE scooters (
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL,
                battery_level float NOT NULL
            );
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    init_database()
