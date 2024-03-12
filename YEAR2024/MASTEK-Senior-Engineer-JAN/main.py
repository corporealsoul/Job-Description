# from lib.logic import wiki

# result = wiki()
# print(result)

#



# from fastapi import FastAPI
# import uvicorn
# from lib.logic import wiki

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"Messege": "Wikipedia API"}

# @app.get("add/{num1}/{num2}")
# async def add(num1: int, num2: int):
#     """Add two numbers together"""
#     total = num1 + num2
#     return{"Total": total}

# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')





from fastapi import FastAPI
import uvicorn
# from lib.logic import (wiki, search_wiki)
from lib.logic import search_wiki
from lib.logic import wiki as wikilogic
from lib.logic import phrase as wikiphrases

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API.  Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """Pages to search in wiki"""

    result = search_wiki(value)
    return{"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wiki"""

    result = wikilogic(name)
    return{"result": result}

@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wiki and Return phrase"""

    result = wikiphrases(name)
    return{"result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')