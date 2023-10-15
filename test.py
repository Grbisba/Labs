import wikipedia
from pydantic import BaseModel
print(type(wikipedia.suggest("snak")))
a = wikipedia.suggest("snake")
print(type(a))
print(type(None))

class Bebra(BaseModel):
    trusi: str | None

Bebra.trusi = wikipedia.suggest("snakee")

print(type(Bebra.trusi))