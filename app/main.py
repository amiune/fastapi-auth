from typing import Union
from fastapi import FastAPI, File, UploadFile, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.firebase import get_firebase_user
from app.supabase import get_supabase_user

app = FastAPI()
# allow cross domain ajax calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/firebase_user")
async def hello_firebase_user(user = Depends(get_firebase_user)):
    return {"msg":"Hello firebase user","uid":user['uid']} 

@app.post("/supabase_user")
async def hello_supabase_user(user = Depends(get_supabase_user)):
    return {"msg":"Hello supabse user","uid":user.id} 