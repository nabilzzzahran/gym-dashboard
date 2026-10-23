from fastapi import FastAPI #build the API

app = FastAPI(title="Gym Progress Dashboard")

@app.get("/health")
def health():
    return {"status": "ok"}