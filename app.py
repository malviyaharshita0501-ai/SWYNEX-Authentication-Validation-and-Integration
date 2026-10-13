from flask import Flask, request
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "swynex-dev-key")


# Consistent error response
def error_response(code, message, status_code):
    return {
        "success": False,
        "error": {
            "code": code,
            "message": message
        }
    }, status_code


# Check API key
def authenticate():
    user_key = request.headers.get("X-API-Key")
    return user_key == API_KEY


# Home endpoint
@app.route("/")
def home():
    return {
        "success": True,
        "message": "SWYNEX Task 3 API is running!"
    }, 200


# Protected endpoint
@app.route("/protected", methods=["GET"])
def protected():
    if not authenticate():
        return error_response(
            "UNAUTHORIZED",
            "API key is missing or invalid",
            401
        )

    return {
        "success": True,
        "message": "Authentication successful!",
        "data": {
            "access": "Granted"
        }
    }, 200


# Create product endpoint
@app.route("/products", methods=["POST"])
def create_product():

    # Authentication
    if not authenticate():
        return error_response(
            "UNAUTHORIZED",
            "API key is missing or invalid",
            401
        )

    # Validate JSON
    if not request.is_json:
        return error_response(
            "INVALID_CONTENT_TYPE",
            "Request must contain JSON data",
            415
        )

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return error_response(
            "INVALID_JSON",
            "A valid JSON object is required",
            400
        )

    # Validate product name
    name = data.get("name")

    if not isinstance(name, str) or not name.strip():
        return error_response(
            "VALIDATION_ERROR",
            "Product name is required",
            400
        )

    # Validate price
    price = data.get("price")

    if isinstance(price, bool) or not isinstance(price, (int, float)):
        return error_response(
            "VALIDATION_ERROR",
            "Price must be a number",
            400
        )

    if price <= 0:
        return error_response(
            "VALIDATION_ERROR",
            "Price must be greater than zero",
            400
        )

    # Successful response
    return {
        "success": True,
        "message": "Product validated successfully!",
        "data": {
            "name": name.strip(),
            "price": price
        }
    }, 201


if __name__ == "__main__":
    app.run(debug=True)