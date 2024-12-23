from fastapi import APIRouter, HTTPException
from app.services.embedding_service import process_file
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends
from app.routers.auth import get_current_user

class S3FileProcessRequest(BaseModel):
    bucketName: str
    fileName: str

class ChatResponse(BaseModel):
    humanRequest: str
    aiResponse: str

router = APIRouter()

@router.post("/process")
async def process_embeddings(request: S3FileProcessRequest,current_user: str = Depends(get_current_user)):
    try:
        print("Debug 1: request.bucketName: ",request.bucketName)
        process_file(request.bucketName, request.fileName)
        return {"status": "success", "message": f"File {request.fileName} from AWS S3 {request.bucketName} bucket is processed successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))