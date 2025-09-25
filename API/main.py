from fastapi import FastAPI

app = FastAPI(title="API", version="1.0.0", description="API for the cabines")


@app.get("/")
async def root():
    return {"message": "Hello World"}