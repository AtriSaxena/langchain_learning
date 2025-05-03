from langchain_community.document_loaders import WebBaseLoader 
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=apple&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=87959fa2-9a09-4a5f-875c-dc43ba0d62aa.MOBG6VF5Q82T3XRS.SEARCH&ppt=hp&ppn=homepage&ssid=o204yehcf40000001746260908531&qH=1f3870be274f6c49'

loader = WebBaseLoader(url)

docs = loader.load() 

chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))