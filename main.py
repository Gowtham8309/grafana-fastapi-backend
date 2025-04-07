from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Grafana FastAPI backend is live!"}

@app.get("/health")
def health():
    return {"status": "ok"}
