from fastapi import FastAPI, HTTPException

app = FastAPI()

x = False
if x:
    pass
else:
    with open("error.txt", "w") as f:
        f.write("Daaraann mizanannnnnnnn")

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/error")
def response_error():
    raise HTTPException(
        status_code=404,
        detail="item not found")