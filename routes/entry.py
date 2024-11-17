from fastapi import APIRouter 

entry_root = APIRouter()

# endpoint 
@entry_root.get("/")
def apiRunning():
    # Let's set the response to a Python dictionary : 
    res = {
        "status" : "ok" ,
        "message" : "Api is runinng"
    }
    return res