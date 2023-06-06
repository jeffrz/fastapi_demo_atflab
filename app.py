from fastapi import FastAPI

app = FastAPI()

# configuration goes here
# maybe you import a model.py file containing your database spec
# do other things???

@app.get("/")
async def home():
    return {"message": "Hello World"}
