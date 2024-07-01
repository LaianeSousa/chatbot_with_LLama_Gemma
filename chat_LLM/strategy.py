from abc import ABC, abstractmethod
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu

#Definindo a Interface de Estratégia:
class avalicao_strategy(ABC):
    @abstractmethod
    def avaliacao(self, resposta_model: str, resposta_reference: str) -> float:
        pass

#Implementando Concretamente as Estratégias:



class BLEUEvaluation(avalicao_strategy):
    
    def avaliacao(self, resposta_model: str, resposta_reference: str) -> float:
        reference = resposta_reference.split()
        candidate = resposta_model.split()
        score = sentence_bleu(reference, candidate)
        return score
        

class ROUGEEvaluation(avalicao_strategy):
    def __init__(self):
        self.rouge = Rouge()

    def avaliacao(self, resposta_model: str, resposta_reference: str) -> float:
        scores = self.rouge.get_scores(resposta_model, resposta_reference)
        return scores[0]['rouge-l']['f']


# Criar a Classe Contexto para Avaliação:
class ResponseEvaluator:
    # CONSTRUTOR
    def __init__(self, strategy: avalicao_strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: avalicao_strategy):
        self.strategy = strategy

    def evaluate_response(self, model_response: str, reference_response: str) -> float:
        return self.strategy.avaliacao(model_response, reference_response)
    


