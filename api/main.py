from fastapi import FastAPI

app = FastAPI(title="Décisio API", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "decisio"}
