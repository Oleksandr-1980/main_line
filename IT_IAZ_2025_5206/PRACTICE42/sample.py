from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def my_function():
    return "Hello word" 

def my_function2():
    return