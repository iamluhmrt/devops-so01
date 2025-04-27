from typing import Union
from fastapi import FastAPI
import random

app = FastAPI()

# Secret number randomly generated
secret_number = random.randint(1, 100)

@app.get("/")
def read_root():
    return {"message": "Welcome to the guessing game! Try to guess the number between 1 and 100."}

@app.get("/guess/{number}")
def guess_number(number: int):
    global secret_number
    
    if number < 1 or number > 100:
        return {"message": "Please choose a number between 1 and 100."}
    
    if number < secret_number:
        return {"message": "Try a higher number!"}
    elif number > secret_number:
        return {"message": "Try a lower number!"}
    else:
        secret_number = random.randint(1, 100)  # Restart the game with a new number
        return {"message": "Congratulations! You guessed it! A new number has been generated."}
