# Housing Data API

This repository contains a Python API program built with Flask that allows you to store and retrieve housing data. The API supports storing JSON data in a PostgreSQL database and provides endpoints to retrieve statistics about the housing data.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL database

## Installation

1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```
   Replace `<repository_url>` with the actual URL of the GitHub repository.

2. Navigate to the cloned repository directory:
   ```
   cd housing-data-api
   ```

3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Configure the PostgreSQL Database:
   - Make sure you have a PostgreSQL database set up with the necessary credentials.
   - Update the PostgreSQL connection URL in the `app.py` file to match your configuration. Look for the following line and modify it accordingly:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
     ```

## Usage

1. Run the Python API program using the following command:
   ```
   python app.py
   ```
   The Flask development server will start running on `http://localhost:5000`.

2. Access the API endpoints:
   - To store JSON data in the database, make a POST request to `http://localhost:5000/houses` with the JSON data as the request body.
   - To retrieve statistics about the housing data, make a GET request to `http://localhost:5000/statistics`.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality of the API, feel free to open an issue or submit a pull request.
