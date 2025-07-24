from fastapi import FastAPI

app = FastAPI()


@app.get("/display")
def view():
    return "Hello world Harrish"


# 2. path parameter
@app.get("/path/{id}")
def path_parameter(id):
    return f"The path id you passed is: {id}"
