from database_connect import get_db_connection


class ElectroScooter:
    def __init__(self, name, battery_level, id=None):
        self.id = id
        self.name = name
        self.battery_level = battery_level

    @classmethod
    def create(cls, name, battery_level):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO scooters (name, battery_level) VALUES (%s, %s) RETURNING id;",
                       (name, battery_level))
        id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        return cls(name, battery_level, id)

    @classmethod
    def get_by_id(cls, scooter_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, battery_level FROM scooters WHERE id = %s;", (scooter_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return cls(result[1], result[2], result[0])
        return None

    def update(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE scooters SET name = %s, battery_level = %s WHERE id = %s;",
            (self.name, self.battery_level, self.id)
        )
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM scooters WHERE id = %s;", (self.id,))
        connection.commit()
        cursor.close()
        connection.close()

