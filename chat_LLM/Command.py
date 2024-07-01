
from factory import LLMFactory
from factory import LLMFactoryManager
from strategy import BLEUEvaluation
from strategy import ROUGEEvaluation
from strategy import ResponseEvaluator


class Command:
    def execute(self):
        raise NotImplementedError

class Consulta(Command):
    def __init__(self, llm: LLMFactory, prompt: str):
        self.llm = llm
        self.prompt = prompt

    def execute(self):
        return self.llm.criar_LLM(self.prompt)

def cli():
    while True:
        comando = input('Digite 1 para sair ou 2 para continuar: ')
        
        if comando == '2':
            print("\nBem-vindo à interface de consulta de LLMs!")
            prompt = input("Digite sua pergunta: ")
           
           ##### GERAR UMA RESPOSTA COM MODELO LLAMA ##############
            llm = LLMFactoryManager.get_factory(model_name='llama')
            command = Consulta(llm, prompt)
            resposta_llama = command.execute()
            print(f"\nResposta do modelo Llama: {resposta_llama}\n")
            
           ##### GERAR UMA RESPOSTA COM MODELO GEMMA ##############

            llm = LLMFactoryManager.get_factory(model_name='gemma')
            command = Consulta(llm, prompt)
            resposta_gemma = command.execute()
            print(f"\nResposta do modelo gemma: {resposta_gemma}\n")



            llama_response = resposta_llama
            reference_response = resposta_gemma
            gemma_response = resposta_gemma
            reference_response = resposta_gemma

            #nicializando as estratégias
            bleu_strategy = BLEUEvaluation()
            rouge_strategy = ROUGEEvaluation()
            
            # Criando o avaliador com uma estratégia inicial
            evaluator = ResponseEvaluator(bleu_strategy)


            # Avaliando as respostas com a estratégia BLEU
            evaluator.set_strategy(bleu_strategy)
            llama_bleu_score = evaluator.evaluate_response(llama_response, reference_response)
            gemma_bleu_score = evaluator.evaluate_response(gemma_response, reference_response)
            print(f"Llama BLEU score: {llama_bleu_score}")
            print(f"Gemma BLEU score: {gemma_bleu_score}")

            # Avaliando as respostas com a estratégia ROUGE
            evaluator.set_strategy(rouge_strategy)
            llama_rouge_score = evaluator.evaluate_response(llama_response, reference_response)
            gemma_rouge_score = evaluator.evaluate_response(gemma_response, reference_response)
            print(f"Llama ROUGE score: {llama_rouge_score}")
            print(f"Gemma ROUGE score: {gemma_rouge_score}")

        elif comando == '1':
            print('Obrigado por usar os LLMs!')
            break
        else:
            
            print("Entrada inválida. Por favor, digite 1 para sair ou 2 para continuar.")
            break

if __name__ == "__main__":
    cli()
