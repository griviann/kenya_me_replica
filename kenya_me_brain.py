import os, json
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
try:
    from groq import Groq
    groq_client = Groq(api_key=os.getenv("GROQ_API"))
except:
    groq_client=None
def call_ai(prompt,cheap=True):
    model="llama-3.1-8b-instant" if cheap else "llama-3.3-70b-versatile"
    if groq_client:
        try:
            r=groq_client.chat.completions.create(model=model,messages=[{"role":"user","content":prompt}],max_tokens=400)
            return r.choices[0].message.content
        except: pass
    return "Poa mkuu! Tunza bunda!"
def kenya_me_reply(user_text,user_id,is_breaking=False):
    if any(k in user_text.lower() for k in ["ebola","mlipuko"]): is_breaking=True
    if is_breaking:
        p=f"You are Kenya Me pro. No Sheng. MOH/WHO + 719. User:{user_text}"
        pro=call_ai(p,False)
        drafts=[]
        if os.path.exists("drafts_to_review.json"):
            try:
                import json as js
                with open("drafts_to_review.json") as f: drafts=js.load(f)
            except: drafts=[]
        drafts.append({"pro":pro,"time":str(datetime.now()),"query":user_text})
        with open("drafts_to_review.json","w") as f: json.dump(drafts,f,indent=2,ensure_ascii=False)
        return pro
    else:
        p=f"You are Kenya Me Kiambu brother Sheng fun tunza bunda. User:{user_text}"
        return call_ai(p,True)
def scan_trending():
    print(f"SCAN {datetime.now()}")
