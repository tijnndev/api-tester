# Flask API Tester

A simple Flask web application that allows you to send HTTP requests (GET, POST, etc.) to any URL with custom headers, parameters, and optional authentication. Useful for testing and debugging APIs.

## Features

- Web interface served at `/` (HTML template required)
- POST endpoint at `/api/test` for sending API requests
- Supports:
  - HTTP methods (GET, POST, PUT, DELETE, etc.)
  - Custom headers
  - JSON body parameters
  - Bearer token authentication
- Static file serving from the `/static` directory

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tijnndev/api-tester.git
   cd flask-api-tester
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`

## API

### `POST /api/test`

Send a test request to any external API.

#### Request Body (JSON)

```json
{
  "url": "https://example.com/api",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "params": {
    "key": "value"
  },
  "auth_token": "optional_bearer_token"
}
```

#### Response

```json
{
  "status": 200,
  "response": {
    "data": "API response content"
  }
}
```

Or on error:

```json
{
  "error": "Error message"
}
```

## Directory Structure

```
project/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── (your static files)
```

## License

MIT License

```