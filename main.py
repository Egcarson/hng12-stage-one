import requests
from fastapi import FastAPI, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HNG12",
    description= "Stage One Task"
)

# Enabling CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
)

#defining functions
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
    return sum(n for n in range(1, num) if num % n == 0) == num

def digit_sum(num: int) -> int:
    return sum(int(n) for n in str(num))

def is_amstrong(num: int) -> bool:
    digits = [int(d) for d in str(num)]

    return sum(d ** len(digits) for d in digits) == num

def get_fun_fact(num: int) -> str:

    response = requests.get(f"http://numbersapi.com/{num}/math?json")

    if response.status_code == 200:
        return response.json().get("text", "No fun fact available.")
    
    return "No fun fact available."

###########ENDPOINT
@app.get('/api/classify-number', status_code=status.HTTP_200_OK)
def classify_number(num: int):
    
    # classify number properties and get fun fact
    try:
        d_properties = []

        if is_amstrong(num):
            d_properties.append("armstrong")
        
        if num % 2 == 0:
            d_properties.append("even")
        else:
            d_properties.append("odd")
        
        result = {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": d_properties,
            "digit_sum": digit_sum(num),
            "fun_fact": get_fun_fact(num)
        }
        return result
    
    # Validate input    
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})
