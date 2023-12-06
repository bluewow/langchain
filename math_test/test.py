from dotenv import load_dotenv

# 환경변수 세팅
load_dotenv("../.env")

from operator import itemgetter
from data import *
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

default_prompt = ChatPromptTemplate.from_messages([
    # ("system", "풀이과정을 생략하고 정답만 출력해줘"),
    ("human", "{question}")
])

llm = ChatOpenAI(temperature=0,
                 max_tokens=4096,
                 model='gpt-4-1106-preview',
                 streaming=True,
                 callbacks=[StreamingStdOutCallbackHandler()])

chain = (
    {"question": RunnablePassthrough()}
    | default_prompt
    | llm
)

# print("--------------1번--------------\n")
# print(chain.invoke({"question": p1}))
# print("--------------2번--------------\n")
# print(chain.invoke({"question": p2}))
# print("--------------3번--------------\n")
# print(chain.invoke({"question": p3}))
# print("--------------4번--------------\n")
# print(chain.invoke({"question": p4}))
# print("--------------5번--------------\n")
# print(chain.invoke({"question": p5}))
# print("--------------6번--------------\n")
# print(chain.invoke({"question": p6}))
# print("--------------7번--------------\n")
# print(chain.invoke({"question": p7}))
# print("--------------8번--------------\n")
# print(chain.invoke({"question": p8}))
# print("--------------9번--------------\n")
# print(chain.invoke({"question": p9}))
# print("--------------10번--------------\n")
# print(chain.invoke({"question": p10}))
# print("--------------11번--------------\n")
# print(chain.invoke({"question": p11}))
# print("--------------12번--------------\n")
# print(chain.invoke({"question": p12}))
# print("--------------13번--------------\n")
# print(chain.invoke({"question": p13}))
# print("--------------14번--------------\n")
# print(chain.invoke({"question": p14}))
# print("--------------15번--------------\n")
# print(chain.invoke({"question": p15}))
# print("--------------16번--------------\n")
# print(chain.invoke({"question": p16}))
# print("--------------17번--------------\n")
# print(chain.invoke({"question": p17}))
# print("--------------18번--------------\n")
# print(chain.invoke({"question": p18}))
# print("--------------19번--------------\n")
# print(chain.invoke({"question": p19}))
# print("--------------20번--------------\n")
# print(chain.invoke({"question": p20}))
# print("--------------21번--------------\n")
# print(chain.invoke({"question": p21}))
# print("--------------22번--------------\n")
# print(chain.invoke({"question": p22}))