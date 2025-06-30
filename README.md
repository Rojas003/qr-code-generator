# QR Code Generator App 

This Python application generates a QR code from a provided URL and saves it as an image file. The app can be run locally or inside a Docker container.

---

##  How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
### 2. Run the app
python3 main.py https://www.njit.edu
## How to Run in Docker

### 1. Build the Image
docker build -t qr-code-generator-app .
### 2. Run the container 
docker run --rm qr-code-generator-app
### Run with custom URL
docker run --rm qr-code-generator-app https://example.com

Available on https://hub.docker.com/repository/docker/rojas003/qr-code-generator-app

Source code hosted on Github https://github.com/rojas003/qr-code-generator

See how I learned all this through the Reflection Document for more about my experience using Docker and containerizing this app.