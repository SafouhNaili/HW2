# Car Showroom API

This is a Flask-based REST API for managing cars in a showroom. It supports the following endpoints:

- `GET /api/carshowroom`: Fetch all cars.
- `POST /api/carshowroom`: Add a new car.
- `PUT /api/carshowroom/<id>`: Update a car by ID.
- `DELETE /api/carshowroom/<id>`: Delete a car by ID.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install Flask mysql-connector-python`.
3. Run the app: `python3 app.py`.