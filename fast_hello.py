from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
    # return "Hello World!"

if __name__ == '__main__':
    uvicorn.run("fast_hello:app")