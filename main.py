from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def HelloFromFastApi():
    return "Hello word from fastapi"