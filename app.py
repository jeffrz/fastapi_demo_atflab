from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import ORJSONResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# configuration goes here
# maybe you import a model.py file containing your database spec
# do other things???

@app.get("/", response_class=HTMLResponse)
async def home():
    return "Hello World"

@app.get("/topic_page")
async def topic_vis( request: Request, param: str ):
    # uses a template to insert variables into some html using jinja
    # composes the file, and sends it to the user
    return templates.TemplateResponse("temp1.htm", {"request": request, "urlval": param, "value": "hello"})

@app.get("/is_even", response_class=ORJSONResponse)
async def iseven( request: Request, num: int):
    is_even = num % 2 == 0
    return [{"answer": is_even}, 'arraytest', 3]
    
    
    
