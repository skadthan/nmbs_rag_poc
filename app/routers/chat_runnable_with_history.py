import inspect
from fastapi import APIRouter, HTTPException
from app.services.chat_runnable_with_history_service import process_rag
from pydantic import BaseModel
from app.services import chat_contextual as cc

from fastapi import APIRouter, HTTPException
from app.services.rag_chain_service import get_rag_chain, get_chain_with_history
from app.models.rag_models import RAGRequest, RAGResponse

router = APIRouter()

@router.post("/contextualbot", response_model=RAGResponse)

async def contexctual_chatbot(request: RAGRequest):
    try:
        test_response=cc.contexctual_chat_invoke()
        print("test_response: ", test_response)
        response = await process_rag(request)
         # If output is a coroutine, await it again
        if inspect.iscoroutine(response):
            response =  await response

        print("after inspect", response)
        print("response:  :  :", response)
        return {"humanRequest":request.query, "aiResponse": response.answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
