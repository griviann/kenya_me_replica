from fastapi import FastAPI, Request
import os, json
from datetime import datetime
import kenya_me_brain as brain
app = FastAPI()
@app.get("/")
def home():
    return {"status":"Kenya Me V16 ALIVE","bunda":"Tunza bunda"}
@app.get("/scan")
def do_scan():
    brain.scan_trending()
    return {"scanned":True}
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    reply = brain.kenya_me_reply(data.get("message",""), data.get("user_id","default"), data.get("is_breaking",False))
    return {"reply":reply}
