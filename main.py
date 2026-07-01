from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world"}


@app.post("/{num1}/{num2}")
def add(num1: float, num2: float):
    total = num1 + num2
    return {"total": total}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
