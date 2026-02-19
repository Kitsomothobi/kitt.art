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

# --------------
def render(request: Request, template: str, active_page: str, **context):
    base = {
        "request": request,
        "year": datetime.now().year,
        "active_page": active_page
        }
    # Whenever a new webpage is clicked, we need to immediately update the context for our css
    base.update(context)
    return templates.TemplateResponse(template, base)


# Page routes
    #1 - Homepage decorater
@app.get("/")
def home(request: Request):
    return render(request, "index.html", "home")

    #2 - Gallery page
@app.get("/gallery")
def gallery(request: Request):
    return render(request, "gallery.html", "gallery")

    #3 - Blog page
@app.get("/blog")
def blog(request: Request):
    return render(request, "blog.html", "blog")

    #4 - Commissions
@app.get("/commissions")
def commissions(request: Request):
    return render(request, "commissions.html", "commissions")

    #5 - Projects
@app.get("/projects")
def projects(request: Request):
    return render(request, "projects.html", "projects")
