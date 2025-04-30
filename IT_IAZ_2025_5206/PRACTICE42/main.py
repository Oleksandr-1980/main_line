from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def f1():
    return "Hello world"

@app.get("/id")
def f2():
    return {"id":None, "countz":myList}

myList = [12,34,56,78,345,678,789]

@app.get("/id/{id}")
def f3(id:int):
    return {"id":id, "count":myList[id]*myList[id]}
