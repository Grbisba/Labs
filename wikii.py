from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

# python -m uvicorn wikii:app --reload

class Wikiped(BaseModel):
    name_of_title: str
    true_name_of_tittle: str | None
    resume: str
    URL: str

a = "Wikipedia"

@app.get("/Wikipedia")
def tittle_page(a: str):
    return a


@app.get("/search/{prin}")
def search_text(prin: str):
    return wikipedia.search(prin)


@app.get("/search_times/{prin}")
def search_times(prin: str, times: int):
    return wikipedia.search(prin, results=times)


@app.post("/true_name_of_tittle/")
def true_name_of_tittle(pri: str | None):
    # if type(wikipedia.suggest(pri)) == type(None):
    #     return "All right!"
    # else:
    #     return wikipedia.suggest(pri)
    return wikipedia.suggest(pri)


@app.post("/wikipedia_basa/", response_model=Wikiped)
def with_body(pri: str, resp: Wikiped):
    resp.name_of_title = pri
    resp.true_name_of_tittle = wikipedia.suggest(pri)
    if type(wikipedia.suggest(pri)) == type(None):
        resp.true_name_of_tittle = pri
    else:
        resp.true_name_of_tittle = wikipedia.suggest(pri)
    resp.resume = wikipedia.summary(resp.true_name_of_tittle)
    resp.URL = wikipedia.page(resp.true_name_of_tittle).url
    # if type(resp.true_name_of_tittle) == type(None):
    #     resp.resume = wikipedia.summary(resp.name_of_tittle)
    #     resp.URL = wikipedia.page(resp.name_of_tittle).url
    # elif type(resp.true_name_of_tittle) == type(str):
    #     resp.resume = wikipedia.summary(resp.true_name_of_tittle)
    #     resp.URL = wikipedia.page(resp.true_name_of_tittle).url
    return resp
