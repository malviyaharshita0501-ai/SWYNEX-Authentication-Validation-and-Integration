# SWYNEX Internship Task 3

## Authentication, Validation, and Integration

### Project Overview

This project is a Python Flask API developed as part of the SWYNEX internship. It demonstrates API key authentication, input validation, and consistent JSON error responses.

### Technologies Used

* Python
* Flask
* REST API
* JSON
* Python unittest

### Features

* Public home endpoint
* API key authentication for protected endpoints
* Product creation endpoint with input validation
* Consistent JSON error responses
* Automated API tests

### Project Structure

```text
SWYNEX-Authentication-Validation-and-Integration/
├── app.py
├── test_api.py
├── requirements.txt
├── README.md
└── venv/
```

### Installation

1. Install Python.

2. Clone this repository.

3. Open the project folder in a terminal.

4. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

5. Activate the virtual environment.

   Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

6. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

### Run the Application

```bash
python app.py
```

The API runs locally at `http://127.0.0.1:5000`.

### API Endpoints

#### 1. Home

* Method: `GET`
* Path: `/`
* Authentication: Not required

#### 2. Protected Endpoint

* Method: `GET`
* Path: `/protected`
* Header: `X-API-Key`

#### 3. Create Product

* Method: `POST`
* Path: `/products`
* Header: `X-API-Key`
* Content-Type: `application/json`

Example request:

```json
{
  "name": "Laptop",
  "price": 50000
}
```

### Authentication for Testing

For local development, the application uses `swynex-dev-key` as its default API key.

To set your own API key in Windows PowerShell before starting the application:

```powershell
$env:API_KEY = "your-test-key"
python app.py
```

Use the same key in the `X-API-Key` header when testing protected endpoints.

**Security note:** The default key is for local development only. Use a strong secret stored in an environment variable for deployment. Never commit real API keys to GitHub.

### Testing

Run the automated tests with:

```bash
python -m unittest -v test_api.py
```

The tests cover the home endpoint, authentication, valid product creation, empty product names, and negative prices.

### Error Responses

Example unauthorized response:

```json
{
  "success": false,
  "error": {
    "code": "UNAUTHORIZED",
    "message": "API key is missing or invalid"
  }
}
```

Example validation error:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Product name is required"
  }
}
```

### Learning Outcomes

* Understanding API key authentication
* Validating incoming JSON payloads
* Returning consistent API error responses
* Writing automated tests for Flask applications
* Documenting API endpoints and testing procedures

### Internship

Developed as part of the SWYNEX Python Internship.
