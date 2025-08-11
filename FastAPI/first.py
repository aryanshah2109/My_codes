from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def greet():
    return {'message':'Hello World'}

@app.get("/about")
def about():
    return {'message':'I am Aryan shah'}
