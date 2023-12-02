from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv

# 환경변수 세팅
load_dotenv(".env")

from setting import chatModel

app = FastAPI(
    title="LangChain Server",
    description="A simple api server using Langchain's Runnable interfaces",
)


from category_chain import category_chain

# LangChain 을 FastAPI 라우트에 추가하는 함수
add_routes(app, category_chain, path="/category_chain")
add_routes(app, chatModel, path="/openai")

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
