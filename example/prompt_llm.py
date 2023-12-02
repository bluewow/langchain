from dotenv import load_dotenv

# 환경변수 세팅
load_dotenv("../.env")
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
model = ChatOpenAI()

# ----------------------
# prompt + model to chain
# ----------------------
chain = prompt | model
# print(chain.invoke({"foo": "bears"}))

# ----------------------
#Function Call information
# ----------------------
functions = [
    {
        "name": "joke",
        "description": "A joke",
        "parameters": {
            "type": "object",
            "properties": {
                "setup": {"type": "string", "description": "The setup for the joke"},
                "punchline": {
                    "type": "string",
                    "description": "The punchline for the joke",
                },
            },
            "required": ["setup", "punchline"],
        },
    }
]
chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions)
# print(chain.invoke({"foo": "bears"}, config={}))

# ----------------------
# + parser basic
# ----------------------
chain = prompt | model | StrOutputParser()
# print(chain.invoke({"foo": "bears"}))

# ----------------------
# + parser (json)
# ----------------------
chain = (
    prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonOutputFunctionsParser()
)
# print(chain.invoke({"foo": "bears"}))

# ----------------------
# + parser (json key)
# ----------------------
chain = (
    prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
# print(chain.invoke({"foo": "bears"}))

# ----------------------
# Simplifying input by Runnable #1
# ----------------------
map_ = RunnableParallel(foo=RunnablePassthrough())
chain = (
    map_
    | prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
# print(chain.invoke("bears"))

# ----------------------
# Simplifying input by Runnable #2
# ----------------------
chain = (
    {"foo": RunnablePassthrough()}
    | prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
# print(chain.invoke("bears"))