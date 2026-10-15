from fastapi import FastAPI

app = FastAPI(title="Student Management API")


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


@app.get("/health")
def health_check():
    return {"status": "healty"}
