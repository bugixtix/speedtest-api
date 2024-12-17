# Internet Speed Test Service

This is a Flask-based web application for measuring internet speed, including download, upload, and ping. It uses the `speedtest` Python module to perform tests and is hosted on a cloud platform like AWS.

## Features
- Measure download, upload, and ping speeds.
- JSON API response for easy integration.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/internet-speed-test.git
   cd internet-speed-test
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application locally:
   ```bash
   python app.py
   ```

## Usage
- Access the app in your browser at `http://localhost:5000` (or the deployed URL).
- The results are displayed in a JSON format.

## Deployment
- This app can be deployed on platforms like AWS. Ensure `gunicorn` is added to `requirements.txt` for production.

## License
This project is open-source and available under the [MIT License](LICENSE).