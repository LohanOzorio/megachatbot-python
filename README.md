# 🤖 Chat Bot: EcoBot

## 🔹 Introdução

Este projeto consiste em um chatbot chamado EcoBot, desenvolvido para educar os usuários sobre práticas sustentáveis e oferecer dicas personalizadas para reduzir o impacto ambiental em suas vidas diárias. O EcoBot visa resolver a falta de conhecimento prático e a dificuldade em aplicar princípios de sustentabilidade no cotidiano, tornando a informação acessível e adaptada às necessidades de cada usuário. Ele é projetado para qualquer pessoa interessada em adotar um estilo de vida mais ecológico, seja em casa ou no trabalho.

## 🔹 Recursos e Funcionalidades

*   **Educação sobre Sustentabilidade:** O EcoBot fornece informações detalhadas sobre práticas sustentáveis em diversas áreas, como consumo de energia, gestão de resíduos, alimentação e transporte.
*   **Dicas Personalizadas:** Com base nas respostas do usuário sobre seus hábitos e rotina, o EcoBot oferece dicas customizadas para reduzir o impacto ambiental, como sugestões de produtos ecológicos, alternativas de transporte sustentável e formas de economizar energia.
*   **Informações sobre Reciclagem:** O bot informa sobre como reciclar diferentes tipos de materiais e encontrar pontos de coleta próximos ao usuário.
*   **Cálculo de Pegada Ecológica:** O EcoBot pode ajudar a calcular a pegada ecológica do usuário, fornecendo uma estimativa do impacto ambiental de seus hábitos e sugerindo formas de reduzi-la.
*   **Desafios e Campanhas:** O bot propõe desafios e campanhas para incentivar a adoção de práticas sustentáveis e promover a conscientização ambiental.

## 🔹 Tecnologias Utilizadas

*   🐍 **Python:** A linguagem de programação principal utilizada para desenvolver a lógica do chatbot. Escolhida pela sua simplicidade, versatilidade e grande número de bibliotecas disponíveis.
*   💬 **Terminal:** Usado para interagir com o chatbot em formato de texto.

## 🔹 Pré-requisitos e Instalação

Antes de executar o EcoBot, você precisará ter o Python instalado em seu sistema.

1.  **Instale o Python:**

    *   Se você ainda não tem o Python, baixe a versão mais recente em [python.org](https://www.python.org/downloads/).
    *   Durante a instalação, certifique-se de marcar a opção "Add Python to PATH" para que o Python possa ser executado a partir da linha de comando.

2.  **Clone o repositório:**

    Abra o terminal e execute o seguinte comando para clonar o repositório do projeto:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd EcoBot
    ```

    *Substitua `<URL_DO_REPOSITORIO>` pelo endereço do repositório do seu projeto.*

3.  **Instale as dependências (se houver):**

    Se o projeto tiver dependências listadas em um arquivo `requirements.txt`, execute o seguinte comando para instalá-las:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o chatbot:**

    Para iniciar o EcoBot, execute o seguinte comando:

    ```bash
    python eco_bot.py
    ```

    *Substitua `eco_bot.py` pelo nome do arquivo principal do seu chatbot.*

## 🔹 Como Usar

Após a instalação, execute o script Python principal (`eco_bot.py`). O chatbot iniciará no terminal e exibirá uma mensagem de boas-vindas. Siga as instruções exibidas para interagir com o bot.

**Fluxo de Conversa de Exemplo:**

1.  **Bot:** Olá! Sou o EcoBot, seu assistente pessoal para práticas sustentáveis. Quer saber como reduzir seu impacto ambiental?
2.  **Usuário:** Sim, quero.
3.  **Bot:** Ótimo! Para começar, qual área te interessa mais: energia, resíduos, alimentação ou transporte?
4.  **Usuário:** Energia.
5.  **Bot:** Perfeito! Você sabia que pequenas mudanças podem fazer uma grande diferença? Por exemplo, trocar lâmpadas incandescentes por LED pode economizar até 75% de energia. Quer saber mais dicas sobre como economizar energia em casa?

## 🔹 Exemplos de Código

```python
def eco_bot():
    print("Olá! Sou o EcoBot, seu assistente pessoal para práticas sustentáveis.")
    print("Quer saber como reduzir seu impacto ambiental?")

    resposta = input("Sim ou Não? ").lower()

    if resposta == "sim":
        print("Ótimo! Para começar, qual área te interessa mais: energia, resíduos, alimentação ou transporte?")
        area = input("Escolha uma área: ").lower()

        if area == "energia":
            print("Você sabia que pequenas mudanças podem fazer uma grande diferença? Por exemplo, trocar lâmpadas incandescentes por LED pode economizar até 75% de energia.")
            print("Quer saber mais dicas sobre como economizar energia em casa?")
        elif area == "resíduos":
            print("Reduzir, reutilizar e reciclar são as chaves para uma gestão de resíduos eficiente.")
        elif area == "alimentação":
            print("Alimentos orgânicos e de produção local são ótimas opções para uma alimentação mais sustentável.")
        elif area == "transporte":
            print("Opte por andar de bicicleta, usar transporte público ou compartilhar caronas sempre que possível.")
        else:
            print("Área não reconhecida. Por favor, escolha entre energia, resíduos, alimentação ou transporte.")
    else:
        print("Sem problemas! Se precisar de ajuda no futuro, estou aqui.")

eco_bot()
```

*Este é um exemplo básico do fluxo de conversa do EcoBot.*

## 🔹 Estrutura de Diretórios

```
EcoBot/
├── eco_bot.py         # Arquivo principal do chatbot
├── README.md          # Documentação do projeto
└── ...
```

## 🔹 Contribuição

Contribuições são sempre bem-vindas! Se você tiver alguma ideia de melhoria, correção de bugs ou novas funcionalidades, siga os passos abaixo:

1.  Faça um fork do repositório.
2.  Crie uma branch com a sua alteração: `git checkout -b minha-alteracao`
3.  Faça as alterações e commit: `git commit -m "Adiciona nova funcionalidade"`
4.  Envie para o seu repositório forkado: `git push origin minha-alteracao`
5.  Abra um pull request no repositório original.

## 🔹 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
