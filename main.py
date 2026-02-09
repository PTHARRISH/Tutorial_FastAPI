from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates").TemplateResponse

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]


product: list[dict] = [
    {
        "productId": 101,
        "productName": "Wireless Mouse",
        "price": 25.99,
    },
    {
        "productId": 102,
        "productName": "Keyboard",
        "price": 45.99,
    },
]

# HTMLResponse
# from fastapi.responses import HTMLResponse
# response display in HTML
# Json Response or dictif you return it will show error in HTML response internal server error
# ex: @app.get("/", response_class=HTMLResponse)


# include_in_schema = False
# HTML routes only for user view not for json response better to hide in docs
# Hide in docs add after response_class type include_in_schema=False
# route will work but hide in docs
# ex: @app.get("/products", response_class=HTMLResponse,include_in_schema=False)

# Two Routes
# stacking decorator two routes for same function
# ex: @app.get("/", response_class=HTMLResponse)
#     @app.get("/products", response_class=HTMLResponse)


@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    # return {"message": "Hello World"}
    return f"<H1>{posts[0]['title']}</h1>"


@app.get("/home")
def get_home(request: Request):
    return templates(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


# Jinja2Templates
# Jinja is a templating engine for Python,
# import Request in fastapi and create variable
# and assign templates = Jinja2Templates(directory="templates").TemplateResponse
# remove the response_class=HTMLResponse from def and add in parameters request: Request
# then in return templates(request, "home.html")

# Context
# Template variables are defined by the context dictionary passed to the template.

# Jinja template inheritance
# Jinja template inheritance is a powerful feature that allows you to create reusable
# and maintainable templates by defining a base structure and extending
# it in child templates.
# This approach is particularly useful for web applications where multiple pages
# share common elements like headers, footers, or navigation menus.


@app.get("/api/product")
def get_posts():
    return posts
