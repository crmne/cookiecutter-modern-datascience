from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def root():
    raise NotImplementedError
