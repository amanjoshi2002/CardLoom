from fastapi import APIRouter, File, UploadFile

from core.llm_extractor import llm_extract
from core.ocr import ocr_predict

upload_folder = "uploads"


router = APIRouter(
    prefix="/api/cards",
    tags=["cards"]
)



@router.post("/")
async def scancards(image: UploadFile = File(...)):
    #create uploads folder if it doesn't exist
    import os
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    #save images in uploads folder
    with open(f"{upload_folder}/{image.filename}", "wb") as buffer:
        buffer.write(await image.read())
    
    #pass the image to the ocr function
    result = ocr_predict(f"{upload_folder}/{image.filename}")
    print(result)

    llm_result = llm_extract(result)

    return {"message": "Card scanned successfully", "extracted_text": llm_result}
