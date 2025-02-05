import requests
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="NUMBER CLASSIFICATION API",
    description="HNG12 | Stage One Task"
)

# Enabling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  # Ensure all headers are allowed
)

# defining functions
'''
"is_prime": false,
"is_perfect": false,
"properties": ["armstrong", "odd"],
"digit_sum": 11,  // sum of its digits
"fun_fact": getting a random fun fact from Numbers API
'''


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def is_perfect(num: int) -> bool:
    if num < 1:
        return False
    return sum(n for n in range(1, num) if num % n == 0) == num


def digit_sum(num: int) -> int:
    if num < 1:
        return False
    return sum(int(n) for n in str(num))


def is_amstrong(num: int) -> bool:
    if num < 1:
        return False
    digits = [int(d) for d in str(num)]

    return sum(d ** len(digits) for d in digits) == num


def get_fun_fact(num: int) -> str:

    response = requests.get(f"http://numbersapi.com/{num}/math?json")

    if response.status_code == 200:
        return response.json().get("text", "No fun fact available.")

    return "No fun fact available."

# input validator


def input_validator(num: str) -> bool:
    try:
        int(num)
        return True

    except ValueError:
        return False

# ENDPOINT


@app.get('/api/classify-number', status_code=status.HTTP_200_OK)
def classify_number(number: str):

    if not input_validator(number):
        return JSONResponse(status_code=400, content={
                            "error": True, "number": number})

    number = int(number)

    # classify number properties and get fun fact

    d_properties = []

    if is_amstrong(number):
        d_properties.append("armstrong")

    if number % 2 == 0:
        d_properties.append("even")
    else:
        d_properties.append("odd")

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": d_properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    return result