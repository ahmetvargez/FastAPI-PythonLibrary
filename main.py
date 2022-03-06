from fastapi import FastAPI
app = FastAPI()
# FastAPI is a really good library and I will use this as backend side of my applications
@app.get("/")
async def getRoot():
    return {"message": "Hello World"}    
@app.get("/author")
async def getAuthor():
    return {"Author": "Ahmet Vargez"}