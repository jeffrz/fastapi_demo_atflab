import os, csv
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
    
    # ***** SECRET KEY, DO NOT SEND IN PLAIN ******
    secret_key = os.environ.get('TOPIC_API_KEY')
    #response = twitter.api.get("tweets", tweetID, secret_api_key = secret_key)
    
    # DON'T SEND SECRETS IN PLAIN TEXT - WHENEVER YOU USE os.environ, PUT SOME FLAGS AROUND IT
    return templates.TemplateResponse("temp1.htm", {"request": request, "urlval": param, "value": secret_key})

@app.get("/is_even", response_class=ORJSONResponse)
async def iseven( request: Request, num: int):
    is_even = num % 2 == 0
    return [{"answer": is_even}, 'arraytest', 3]
    
    
# I put data here so that it is loaded ONCE, when the .py file is run the first time
# it's then kept in memory for when people need it
data = []
with open('BreakfastCereals.csv') as f:
    r = csv.DictReader(f)
    data = [row for row in r]
    # do some post-processing here like make extra dictionaries or store it in different ways
    # EFFICIENCY matters a lot when working on web apps
    # figure out what you can do ahead of time, what can sit in memory
    
@app.get("/cereals", response_class=ORJSONResponse)
async def servecereal():
    # if I put my data load here, then it gets loaded EVERY TIME someone asks for it
    return data





    
    
