# Importing in our libraries and useful utilities
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from datetime import datetime

# Test
submissions = []

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


# Commission form 
@app.post("/commissions")
def submit_commission(request: Request,
    name: str = Form(...),
    email: str = Form(...),
    type: str = Form(...),
    budget: str = Form(None),
    description: str = Form(...) ):

    submissions.append({
        "name": name,
        "email": email,
        "type": type,
        "budget": budget,
        "description": description
    })

    return templates.TemplateResponse(
        "commission_success.html",
        {
            "request": request,
            "name": name,
            "active_page": "commissions",
            "year": datetime.now().year
        })
