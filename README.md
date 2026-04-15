# Quantum Calculator Web App

A modern, Docker-ready Flask calculator website with polished styling and deploy-ready configuration.

## Project Structure

- `app.py`: Flask application logic and route handling
- `requirements.txt`: Python package dependencies
- `Dockerfile`: Docker image build instructions
- `README.md`: Deployment and usage instructions
- `templates/index.html`: The interactive website UI template
- `static/styles.css`: Styling for the calculator web page

## What Makes This App Fascinating

- Modern gradient visuals and responsive layout
- Animated hero section and polished result cards
- Friendly error handling for invalid input and division by zero
- Production-ready Docker deployment using Gunicorn

## Build the Docker Image

1. Open a terminal in the project directory
2. Run:

   ```bash
   docker build -t flask-calculator .
   ```

   This creates a Docker image named `flask-calculator`.

## Run the Container

3. Run the app in Docker:

   ```bash
   docker run -p 5000:5000 flask-calculator
   ```

   This maps port 5000 inside the container to port 5000 on your machine.

## Access the App

4. Open your browser and visit:

   ```text
   http://localhost:5000
   ```

   You will see the polished calculator website with interactive form and result display.

## Local Development

If you want to run locally without Docker, first install dependencies and then start the app:

```bash
pip install -r requirements.txt
python app.py
```

Then visit `http://localhost:5000`.

## File Summary

### `app.py`
Handles GET and POST requests on the home page, validates input, computes results, and renders the HTML template.

### `requirements.txt`
Lists Flask and Gunicorn so the app can run locally and inside a container with a production-ready server.

### `Dockerfile`
Uses `python:3.11-slim`, installs dependencies, copies the app, exposes port 5000, and runs Gunicorn for deployment.

### `templates/index.html`
Defines the engaging website layout, hero section, calculator form, and result display.

### `static/styles.css`
Provides the visual styling, gradients, responsive layout, and polished form design.
