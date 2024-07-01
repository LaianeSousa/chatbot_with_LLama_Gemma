from langchain_groq import ChatGroq
from dotenv import find_dotenv, load_dotenv
from langchain_core.prompts import ChatPromptTemplate


load_dotenv(find_dotenv())
#Definir classes de configuração para armazenar os parâmetros específicos de cada LLM.
# 1. Classes de Configuração:
class LLMConfig:
    def __init__(self, **kwargs):
        self.params = kwargs
        
# -----------------------------------------------------------------------------------------------

class llama3_config(LLMConfig):
    def __init__(self, model_name):
        super().__init__(model_name = model_name)
        
# -----------------------------------------------------------------------------------------------

class gemma_config(LLMConfig):
    def __init__(self, model_name):
        super().__init__(model_name=model_name)



### 2. Interface Abstrata e Fábricas Concretas



class LLMFactory():
    def criar_LLM(self, prompt: str) -> str:
        raise NotImplementedError

class Llama3Factory(LLMFactory):
    def __init__(self, config: llama3_config):
        self.config = config

    def criar_LLM(self, prompt: str):
        llama = ChatGroq(temperature=0, model=self.config.params['model_name'])
        system = "Você é um assistente"
        human = prompt
        prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        chain = prompt_template | llama
        resposta_llama = chain.invoke({"prompt": human})
        return resposta_llama.content

class GemmaFactory(LLMFactory):
    def __init__(self, config: gemma_config):
        self.config = config

    def criar_LLM(self, prompt: str) -> str:
        gemma = ChatGroq(temperature=0, model=self.config.params['model_name'])
        system = "Você é um assistente"
        human = prompt
        prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        chain = prompt_template | gemma
        resposta_gemma = chain.invoke({"prompt": human})
        return resposta_gemma.content


### 3. Gerenciador de Fábricas
class LLMFactoryManager:
    
    def get_factory(model_name: str) -> LLMFactory:
        if model_name == 'llama':
            config1 = llama3_config(model_name = "llama3-70b-8192")
            return Llama3Factory(config1)
        
        elif model_name == 'gemma':
            config2 = gemma_config(model_name='gemma-7b-it')
            return GemmaFactory(config2)
        
        else:
           raise ValueError(f"Modelo {model_name} não é suportado.")
