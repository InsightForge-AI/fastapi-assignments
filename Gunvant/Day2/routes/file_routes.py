from fastapi import APIRouter, UploadFile, File
import pandas as pd

router = APIRouter()

@router.post("File\Boston.csv")
async def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    data = df.head().to_dict()
    return {"preview": data}