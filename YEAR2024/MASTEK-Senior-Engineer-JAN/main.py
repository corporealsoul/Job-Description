# from lib.logic import wiki

# result = wiki()
# print(result)

#

from fastapi import FastAPI
import uvicorn
from lib.logic import wiki

app = FastAPI()

@app.get("/")
async def root():
    return {"Messege": "Hey Project"}

@app.get("add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""
    total = num1 + num2
    return{"Total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')