# FastAPI CRUD Example

A FastAPI project demonstrating how to implement basic **CRUD (Create, Read, Update, Delete)** operations. This project provides a simple API for managing resources, including validation, error handling, and data persistence.

## Features

- **Create**: Create new resources in the database.
- **Read**: Retrieve all resources or a single resource by its ID.
- **Update**: Update existing resources.
- **Delete**: Delete a resource.
- **Validation**: Data validation using Pydantic models for request and response formats.
- **Database Integration**: Uses SQLAlchemy for ORM and SQLite for data storage.
- **Error Handling**: Handles various HTTP errors and validation errors.
- **API Documentation**: Automatically generated API docs using Swagger UI and ReDoc.

## Requirements

- **Python 3.x**
- **FastAPI**: Web framework.
- **Uvicorn**: ASGI server for running the FastAPI app.
- **SQLAlchemy**: ORM for interacting with the database.
- **Pydantic**: Data validation.
- **SQLite**: Default database for the project.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/shahramsamar/Fast_Api_Crude.git
    cd Fast_Api_Crude
    ```

2. **Install Dependencies**:

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    To run the FastAPI app using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the server at `http://127.0.0.1:8000`.

### How to Use

1. **Create a Resource**:
    - Send a `POST` request to `/items/` with the required data to create a new resource.

    Example request:
    ```json
    {
        "name": "Item Name",
        "description": "Item Description"
    }
    ```

2. **Read Resources**:
    - Send a `GET` request to `/items/` to retrieve all resources.
    - Send a `GET` request to `/items/{item_id}/` to retrieve a specific resource by its ID.

3. **Update a Resource**:
    - Send a `PUT` request to `/items/{item_id}/` with the updated data to modify an existing resource.

    Example request:
    ```json
    {
        "name": "Updated Item",
        "description": "Updated Description"
    }
    ```

4. **Delete a Resource**:
    - Send a `DELETE` request to `/items/{item_id}/` to delete the resource by ID.

### Example Endpoints

- **Create Item**: `POST /items/`
- **Get All Items**: `GET /items/`
- **Get Item by ID**: `GET /items/{item_id}/`
- **Update Item**: `PUT /items/{item_id}/`
- **Delete Item**: `DELETE /items/{item_id}/`

### Project Structure

- `main.py`: Contains the FastAPI application, route handlers, and database setup.
- `models.py`: Defines SQLAlchemy ORM models (e.g., `Item`).
- `schemas.py`: Contains Pydantic models for data validation and response formatting.
- `database.py`: Configures the database connection and session handling.
- `requirements.txt`: Lists the necessary libraries and dependencies.

### API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Example Requests

1. **Create Item** (POST):
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/items/' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Sample Item",
        "description": "This is a sample item"
    }'
    ```

2. **Get All Items** (GET):
    ```bash
    curl -X 'GET' 'http://127.0.0.1:8000/items/'
    ```

### Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
