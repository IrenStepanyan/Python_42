# Intern Flask API

## Description
This Flask API simulates an intern who can introduce themselves, make coffee, and attempt to work. It provides three endpoints for interaction.

## Installation
### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application
### Using Flask (Development Mode)
```bash
python intern1.py
```
This will start the server on `http://127.0.0.1:5000/`.

### Using Gunicorn (Production Mode)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 intern1:app
```

## API Endpoints
### 1. Get Intern Name
**Endpoint:**
```http
GET /intern/<name>
```
**Example Response:**
```json
{"name": "Mark"}
```
If `default` is used instead of a name, it returns the default intern message.

### 2. Get Coffee from Intern
**Endpoint:**
```http
GET /intern/<name>/coffee
```
**Example Response:**
```json
{"coffee": "This is the worst coffee you ever tasted."}
```

### 3. Make Intern Work
**Endpoint:**
```http
GET /intern/<name>/work
```
**Example Response:**
```json
{"error": "I'm just an intern, I can't do that..."}
```

## Notes
- The API runs on port `5000` by default.
- The intern has a default name if `default` is passed.
- The `work` endpoint always returns an error message.



