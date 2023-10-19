# init_db.py
from models.database import get_db_connection
from models.electro_scooter import ElectroScooter

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

    # Initialize with some data
    ElectroScooter.create("Honda Dio", 99.9)
    ElectroScooter.create("Yamaha Aerox", 1.23)
    connection.commit()

    # Close
    cursor.close()
    connection.close()


if __name__ == "__main__":
    init_database()
