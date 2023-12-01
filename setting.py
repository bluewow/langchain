from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(temperature=0.2, max_tokens=2048, model_name='gpt-3.5-turbo-16k')