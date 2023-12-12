from fastapi import FastAPI, HTTPException ,UploadFile ,File,Depends
from storage.database_mongo import mongodb
from storage.database_pg import get_db
from fastapi.responses import StreamingResponse
from io import BytesIO
from crud import querydata
from sqlalchemy.orm import Session
from models import properties
from storage.database_pg import engine

properties.Base.metadata.create_all(bind=engine)

app = FastAPI()

COLLECTION_NAME = "profile"

# MongoDB connection

collection = mongodb[COLLECTION_NAME]

@app.post("/register")
async def upload_image(full_name:str, password:str ,email:str,phone:str,image: UploadFile = File(...),db:Session = Depends(get_db)):
    data = querydata.post_user(db,full_name,password,email,phone)
    if data:
        image_data = await image.read()
        image_info = {"user_id":data,"name": image.filename, "content_type": image.content_type, "image": image_data}
        result = collection.insert_one(image_info)

        return {"Profile Created",str(result.inserted_id)}
    raise HTTPException(status_code=403, detail="Email ID is Already Exist")



@app.get("/users")
async def index(db:Session = Depends(get_db)):
    data = querydata.get_user(db)
    for i in data:
        
        i.profile_pic = 'http://localhost:8000/profile/image/'+str(i.id)
    return data

@app.get("/profile/image/{user_id}/")
async def get_image(user_id: int):
    image_data =  collection.find_one({"user_id": user_id})
    if image_data:
        content_type = image_data["content_type"]
        image_bytes = image_data["image"]
        return StreamingResponse(BytesIO(image_bytes), media_type=content_type)
    else:
        raise HTTPException(status_code=404, detail="Image not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)