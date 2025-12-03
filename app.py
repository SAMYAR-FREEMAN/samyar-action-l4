from fastapi import FastApi , HTTPException

app = FastApi()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/error")
def response_error():
    raise HTTPException(
        status_code=404,
        detail="item not found")