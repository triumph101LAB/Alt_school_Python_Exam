from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello world, this is my fist launch of my fast API project"}