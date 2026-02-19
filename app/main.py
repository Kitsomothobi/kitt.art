# Importing in our libraries and useful utilities
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

# Initliaze the fastapi obeject
app = FastAPI()

# Conencting Jinja to our html/css files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Homepage decorater
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "year": datetime.now().year})
