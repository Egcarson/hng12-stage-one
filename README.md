# Number Classification API

## Description
The **Number Classification API** is a FastAPI-based web service that takes a number as input and returns interesting mathematical properties about it, along with a fun fact retrieved from the Numbers API.

## Features
- Classifies numbers as **prime, perfect, Armstrong**
- Determines whether a number is **odd or even**
- Calculates the **sum of the digits** of a number
- Retrieves a **fun fact** about the number from the Numbers API
- Provides structured JSON responses
- Handles errors and invalid inputs

## Tech Stack
- **Programming Language:** Python
- **Framework:** FastAPI
- **Dependency Management:** `pip`
- **External API:** [Numbers API](http://numbersapi.com/)

## API Documentation
### Base URL
```
https://hng12-stage-one-4lvf.onrender.com/docs
```

### Endpoint: Classify Number
**GET** `/classify-number?number=<integer>`

#### **Request Parameters**
| Parameter | Type    | Description               |
|-----------|--------|---------------------------|
| `number`  | `int`  | The number to classify    |

#### **Success Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
}
```

#### **Error Response (400 Bad Request)**
```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation & Setup
### **Prerequisites**
- Python 3.x installed
- `pip` Package Installation

### **Installation Steps**
1. **Clone the Repository**
   ```bash
   git clone <repo-url>
   cd hng12-stage-one
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the FastAPI Server**
   ```bash
   fastapi dev main.py
   ```
5. **Access API Documentation Locally**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Deployment
To deploy the API on a cloud platform, follow these general steps:
1. **Cloud provider** Render
2. **Set up CORS** to handle cross-origin requests

## Contributing
Feel free to contribute to this project! Fork the repository, make changes, and submit a pull request.

---
**Author:** [Godprevail Eseh]

