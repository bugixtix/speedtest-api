# Internet Speed Test Service

This is a Flask-based web application for measuring internet speed, including download, upload, and ping. It uses the `speedtest-cli` Python module to perform tests.

## Warning

The project considered as failed due to incorrect download speed that speedtest-cli package provides (The mentioned package uses old technologies to measure download speed).
Please don't hesitate opening PR if you find any solution for this problem. 

## Features
- Measure download, upload, and ping speeds.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/bugixtix/speedtest-py.git
   cd speedtest-py
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
- The results are displayed in a HTML format.

## Deployment
- This app can be deployed on platforms like AWS. Ensure `gunicorn` is added to `requirements.txt` for production.

## License
This project is open-source and available under the [MIT License](LICENSE).
