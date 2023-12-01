from dotenv import load_dotenv
# 환경변수 세팅
load_dotenv(".env")

from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from test_chain import test_chain
from category_chain import category_chain
from langchain.chat_models import ChatOpenAI
    
app = FastAPI(
    title="LangChain Server",
    description="A simple api server using Langchain's Runnable interfaces",
)
model = ChatOpenAI(temperature=0.2, max_tokens=2048, model_name='gpt-3.5-turbo-16k')

# LangChain 을 FastAPI 라우트에 추가하는 함수
add_routes(app, test_chain, path="/test")
add_routes(app, category_chain, path="/category_chain")
add_routes(app, model, path="/openai")

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
