print("Olá, {nome}, você entrou no chat certo! Serei o seu mentor nessa nova caminhada!")
print("Informe seu nível de conhecimento na área tecnológia voltada a programação e desenvolvimento!")

while True:
  nivel_Formacao = int(input("1 - Iniciante (Sei de absoluto nada)\n2 - Intermediário (já sei a lógica da programação)" \
  "\n3 - Avançado (Já estou trabalhando e procuro me aperfeiçoar)\n4 - Sair\n"))

  if nivel_Formacao ==1:
    print("\nTodo mundo tem um começo! Por isso vou lhe guiar para ter uma base exepcional em programação sem precisar de faculdade.\n" \
    "Sabe qual é o melhor de tudo? Você terá ascesso a conteúdo 100% gratuito.\nAproveitaaaa!!")
    print("Antes de tudo, não se preocupe em qual linguagem seguir, aprenda a base primeiro!")
    print("Bom, preparado para iniciar esse jornada? Você será um profissional incrível se seguir e se for dedicado. 🚀🚀\n" \
    "Acesse todo o conteúdo na ordem.\n")
    print("1º Passo: Curso Em Vídeo:\nLink: https://www.cursoemvideo.com/ \nPython Mundo 1\nPython Mundo 2\nPython Mundo 3")
    print("Aprendeu bem a lógica da coisa? Aprendeu mesmo? Então ta na hora de escolher a linguagem.\nSupunhetamos que você escolheu Java.\n")
    print("2º Passo: Curso Em Vídeo: Link https://www.cursoemvideo.com/ \nJava (POO)")
    print("Até aqui tá tudo ótimo. Se aperfeçoe e vamos para o proximo nível! O intermediário lhe espera.")
  elif nivel_Formacao ==2:
    print("Tá na hora de aprofundar mais.")
    print("1º Passo: Curso Em Vídeo: Link: https://www.cursoemvideo.com/\n Banco de Dados -> MySQL")
    print("2º Passo: Curso Em Vídeo: Link: https://www.cursoemvideo.com/\n Git e GitHub")
    print("3º Passo: YouTube (Fiasco): Link: https://www.youtube.com/watch?v=n8_qrrc8WN4 \nSpring Boot -> FrameWork Java")
    print("Foque e aprenda tudo isso. Após já pode aplicar pra vagas de estágio. 🚀🚀")
  elif nivel_Formacao==3:
    print("Encontre seus defeitos e efetue a correção e nunca pare de estudar! A perfeição e experiência vem com o tempo")
  elif nivel_Formacao ==4:
    break

    