from fastapi import FastAPI

app = FastAPI()


@app.get("/display")
def view():
    return "Hello world Harrish"


# 2. path parameter
@app.get("/path/{id}")
def path_parameter(id):
    return f"The path id you passed is: {id}"


emp = [
    {
        "id": 1,
        "name": "Admin",
        "location": "Bengaluru",
    },
    {
        "id": 16,
        "name": "Harrish PT",
        "location": "Bengaluru",
    },
]


@app.get("/employee/{id}")
def employee_details(id: int):
    for e in emp:
        if e["id"] == id:
            return e


@app.get("/emp_name/{name}")
def employee_name(name: str):
    for e in emp:
        if e["name"] == name:
            return e


 # 3. Query parameter
 @app.get("/emp")
def query_param():
    