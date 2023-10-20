from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

# python -m uvicorn wikii:app --reload

class Wikiped(BaseModel):
    name_of_title: str
    times: int

class PostResponse(BaseModel):
    result: list[str]


@app.get('/')
def empty():
    return 'smth'


@app.get("/search/{prin}")
def search_text(prin: str):
    return wikipedia.search(prin)


@app.get("/search_times/{prin}")
def search_times(prin: str, times: int):
    return wikipedia.search(prin, results=times)


@app.post('/wiki_post', response_model=PostResponse)
def wikigeo(wikiwikiwiki: Wikiped):
    result = wikipedia.search(wikiwikiwiki.name_of_title, results=wikiwikiwiki.times)
    response = PostResponse(result=result)
    return response
