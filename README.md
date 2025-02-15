# Sales Data Pipeline and Viewer

This project is a sales data pipeline and viewer application. It consists of several components including a database seeder, a MySQL database, an Airflow pipeline, and a Flask-based web frontend for viewing the data.

## Project Structure

```
├── /flask-etl-viewer  # project root
| ├── data-pipeline/  # Not ready yet
| │ ├── config/ 
| │ │ └── airflow.cfg 
| │ ├── dags/
| │ └── dockerfile 
| ├── frontend/ 
| │ ├── app/ 
| │ │ ├── blueprints/ 
| │ │ │ ├── __init__.py 
| │ │ │ ├── health_check.py 
| │ │ │ └── webui.py 
| │ │ ├── static/ 
| │ │ │ └── styles.css 
| │ │ ├── templates/ 
| │ │ │ ├── base.html 
| │ │ │ ├── buyers.html 
| │ │ │ ├── homepage.html 
| │ │ │ ├── products.html 
| │ │ │ ├── sales.html 
| │ │ │ └── sellers.html 
| │ │ ├── __init__.py 
| │ │ └── main.py 
| │ ├── .env 
| │ ├── dockerfile 
| │ └── requirements.txt 
| ├── repository/ 
| │ ├── __init__.py 
| │ ├── buyers.py 
| │ ├── connection.py 
| │ ├── products.py 
| │ ├── sales.py 
| │ └── sellers.py 
| | ├── seeder/ 
| | | ├── app/ 
| │ | | ├── __init__.py 
| │ | | ├── generator.py 
| │ | | └── main.py 
| | | ├── dockerfile 
| | └── requirements.txt
| ├── .gitignore 
| ├── database.sql 
| ├── docker-compose.yml 
| └── README.md 
```

## Components

### Data Pipeline

The data pipeline is located in the `data-pipeline/` is managed by Apache Airflow. 

The pipeline is responsible for orchestrating the data flow, extracting data from the database, manipulating it and providing "reports".

### Database

The MySQL database schema is defined in `database.sql`. It includes tables for products, buyers, sellers, and sales.

### Database Seeder

The database seeder is located in the `seeder/` directory. It uses the Faker library to generate random data for products, buyers, sellers, and sales.

It periodically inserts new sales into the database to simulate a system being fed real-time data, so that we always have data available for the `data-pipeline`.

### Web Frontend

The web frontend is built with Flask and is located in the `frontend` directory. It provides a user interface for viewing the data in the database.

Allows you to see both the original database tables **(sales, products, buyers, sellers)** and the reports generated by the `data-pipeline`.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd flask-etl-viewer
    ```

2. **Start the services using Docker Compose:**
    ```sh
    docker-compose up --build
    ```

3. **Access the web frontend at**:
    ```
    http://localhost:5000
    ```

## Endpoints

### Health Check

- **GET** `/health-check/ping`
    - Returns a JSON response indicating the health of the application and the database connection.

### Web UI

- **GET** `/webui/`
    - Renders the homepage.

- **GET** `/webui/sales`
    - Renders a page displaying all sales.

- **GET** `/webui/products`
    - Renders a page displaying all products.

- **GET** `/webui/buyers`
    - Renders a page displaying all buyers.

- **GET** `/webui/sellers`
    - Renders a page displaying all sellers.

`NOTE:` routes for viewing reports will be added later.

## Configuration

No need for additional configuration.
