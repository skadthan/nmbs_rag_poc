from fastapi import FastAPI
from app.routers import chat, embeddings, chat_session_history,iam_info,chat_runnable_with_history, auth, batch_embeddings,create_user_chat_session,get_user_chat_sessions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/nmbs/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace with specific domains for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(auth.router,prefix="/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/chat", tags=["Chatbot"])
app.include_router(chat_runnable_with_history.router,prefix="/chat", tags=["ContextualChatBot"])
app.include_router(embeddings.router, prefix="/embeddings", tags=["Embeddings"])
app.include_router(batch_embeddings.router,prefix="/batchembeddings", tags=["Embeddings"])
app.include_router(chat_session_history.router,prefix="/session",tags=["ChatSession"])
app.include_router(create_user_chat_session.router,prefix="/session",tags=["ChatSession"])
app.include_router(get_user_chat_sessions.router,prefix="/session",tags=["ChatSession"])
app.include_router(iam_info.router, prefix="/iam",tags=["GetIAMInfo"])



@app.get("/")
async def root():
    return {"message": "Welcome to the Nimbus Cabalities Statement AI RAG API Service!"}
