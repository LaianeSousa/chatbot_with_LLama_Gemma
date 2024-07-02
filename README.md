
# CHATBOT 

![Capa do Projeto](https://github.com/LaianeSousa/chatbot_with_LLama_Gemma/blob/main/chat_LLM/__pycache__/Banner%20para%20Linkedin%20Tecnologia%20em%20Preto.png?raw=true)



## Descrição do projeto:
O projeto tem como finalidade a criação de chatbot com dois modelos de LLm (Large Language Models), modelo llama3-70b-8192 que é um modelo desenvolvido pela Meta AI e o Gemma-7B-IT é um modelo de linguagem desenvolvido pela GROQ. 

Ao fazer uma pergunta gerará duas respostas. A primeira respostas corresponde ao modelo llama3 e a outra respostas será do modelo Gemma. Logo, você poderá comparar as duas resposta e verificar se corresponde suas expectativas. 

É importante resaltar que esse projeto foi criado para fins didáticos. Fique a vontade para fazer suas contribuições.

## 🔨 Funcionalidades do projeto:

**É utilizado padrão de projeto:** 

1- Factory Method para a criação de objetos de conexão com APIs de forma abstrata e flexível; 

2- O padrão Command foi utilizado para encapsular a solicitação como um objeto, permitindo parametrizar clientes com diferentes solicitações;

3- o padrão Strategy utilizado para avaliação das 
respostas dos modelos.

## Como executar o projeto

Siga as etapas abaixo para executar o projeto em sua máquina local:

Execute os seguintes comandos a partir da pasta raiz do projeto:


### Clone este repositório

```bash
git clone <https://github.com/LaianeSousa/chatbot_with_LLama_Gemma.git>
```

Este link pode ser encontrado no botão verde acima `Code`.

### Instale as dependências

```bash
pip install langchain
pip install langchain-groq

```
## Estrutura de Pastas

A estrutura de pastas do projeto é organizada da seguinte maneira:

```text
/
|-- chat_LLM/
|   |-- Command.py
|   |-- Factory.py
|   |-- Strategy.py
|   |-- Readme.md
```




## Licença

Este projeto está sob licença. Consulte [LICENSE](LICENSE.md) para obter mais informações.

## Voltar ao topo

[⬆ Voltar ao topo](#título)



