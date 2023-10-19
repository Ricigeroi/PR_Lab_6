# PR Lab 6 -- Electro Scooters API

This repository contains a REST API for managing electro scooters using Flask and PostgreSQL.

## Libraries Required

- `Flask`
- `psycopg2`
- `flask_swagger_ui`

## Repository Structure

- `app.py`: Main application file that initializes the Flask app and sets up the Swagger UI for API documentation.
- `init_db.py`: Script to initialize the database with the required tables.
- `models/`: Contains the database connection setup and the ElectroScooter model.
  - `database.py`: Provides a function to get a connection to the PostgreSQL database.
  - `electro_scooter.py`: Defines the ElectroScooter class and its associated CRUD operations.
- `routes.py`: Defines the API endpoints for creating, reading, updating, and deleting electro scooters.
- `static/swagger.json`: Swagger documentation for the API.

## How to Launch

1. Ensure you have all the required libraries installed.
2. Set up your PostgreSQL database and update the connection details in `models/database.py`.
3. Run `init_db.py` to initialize the database with the required tables.
4. Run `app.py` to start the Flask server.
5. Visit the Swagger UI at `/api/docs` to view the API documentation and test the endpoints.

## Possible HTTP Requests

1. **POST** `/api/electro-scooters`: Create a new electro scooter.
2. **GET** `/api/electro-scooters/{id}`: Retrieve details of an electro scooter by its ID.
3. **PUT** `/api/electro-scooters/{id}`: Update details of an electro scooter by its ID.
4. **DELETE** `/api/electro-scooters/{id}`: Delete an electro scooter by its ID (requires a password in the request header).