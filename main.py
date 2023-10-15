from fastapi import FastAPI
from pydantic import BaseModel
import pyjokes

app = FastAPI()

class Joke(BaseModel):
    friend: str
    joke: str

class JokeInput(BaseMod el):
    friend: str



@app.get("/")
def joke():
    return pyjokes.get_joke()


@app.get("{friend}")
def friends_joke(friend: str):
    return friend + " tell his joke" + pyjokes.get_joke()

@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + ""

    return result

@app.post("/")
def create_joke(joke_input: JokeInput):
    return joke