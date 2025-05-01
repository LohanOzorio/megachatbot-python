print("Olá {nome}, você entrou no chat certo! Serei seu conselheiro! Aproveitando...")
bairro = str(input("Qual bairro você mora? "))

print("Uau, eu tambem moro no {bairro}! Mas eu estou aqui para lhe ajudar! Então vamos lá.")

while True:
  print("-=" * 20)
  decisao = int(input("O que você gostaria de resolver?\n1 - Serviços Públicos\n2 - Eventos Culturais\n3 - Vagas de Emprego\n" \
  "4 - Diretrizes de Cidadania\n5 - Sair e Voltar ao lobby\n"))
  if decisao == 5:
    print("Chamdo encerrado!")
    break

  if decisao == 1:
    print("-=" * 20)
    print("Serviços Públicos\nO que gostaria de fazer? ")
    servicos_Publicos = int(input("1 - Pagar conta de água\n2 - Pagar conta de luz\n3 - Pagar IPTU\n4 - Pagar IPVA\n5 - Declarar IR\n6 - Voltar\n"))
    if servicos_Publicos == 1:
      print("Conta de água: Pagamento realizado com sucesso!")
    elif servicos_Publicos == 2:
      print("Conta de luz: Pagamento realizado com sucesso!")
    elif servicos_Publicos == 3:
      print("Conta IPTU: Pagamento realizado com sucesso!")
    elif servicos_Publicos == 4:
      print("Conta IPVA: Pagamento realizado com sucesso!")
    elif servicos_Publicos == 5:
      print("Declaração do Imposto de Renda: Realizado com sucesso!")
    elif servicos_Publicos == 6:
      print("Voltando...")   
  elif decisao == 2:
    print("-=" * 20)
    print("Eventos Culturais\nO que gostaria de fazer? ")
    eventos_Culturais = int(input("1 - Ingressos Show no Classic Hall\n2 - Ingressos Paixão de Cristo\n3 - Ingressos Cinema\n4 - Ingressos Museus\n5 - Voltar\n"))
    if eventos_Culturais == 1:
      print("Ingressos para o Classic Hall: Comprados com sucesso.")
    elif eventos_Culturais == 2:
      print("Ingressos para a Paixão de Cristo: Comprados com sucesso.")
    elif eventos_Culturais == 3:
      print("Ingressos para o Cinema: Comprados com sucesso.")
    elif eventos_Culturais == 4:
      print("Ingressos para visitar o museu: Comprados com sucesso.")
    elif eventos_Culturais == 5:
      print("Voltando...")
  elif decisao == 3:
    print("-=" * 20)
    print("Vagas de Emprego:\nEscolha e se candidate.\nEmpresas com vagas abertas")
    vagas_Emprego = int(input("1 - Itaú\n2 - Bradesco\n3 - Senac\n4 - Accenture\n5 - Deloitte\n6 - Voltar\n"))
    if vagas_Emprego == 1:
      print("Parabéns, você foi escolhido e o Itaú recebe você de braços abertos! ")
    elif vagas_Emprego ==2:
      print("Parabéns, você foi escolhido e o Bradesco recebe você de braços abertos! ")
    elif vagas_Emprego ==3:
      print("Parabéns, você foi escolhido e o Senac recebe você de braços abertos! ")
    elif vagas_Emprego ==4:
      print("Parabéns, você foi escolhido e a Accenture recebe você de braços abertos! ")
    elif vagas_Emprego ==5:
      print("Parabéns, você foi escolhido e a Deloitte recebe você de braços abertos! ")
    elif vagas_Emprego ==6:
      print("Voltando...")
  elif decisao == 4:
    print("-=" * 20)
    print("Realize o seu dever de ser cidadão:")
    cidadao = int(input("Diretrizes de Cidadania:\n1 - Emitir Passaporte\n2 - Alistamento Militar\n3 - Emitir CNH\n4 - Situação do Titulo de Eleitor\n5 - Voltar\n"))
    if cidadao == 1:
      print("Passaporte emitido.")
    elif cidadao == 2:
      print("Vá para o Quartel mais próximo e se aprensente para o serviço obritatório.")
    elif cidadao ==3:
      print("CNH emitada.")
    elif cidadao ==4:
      print("Titulo de Eleitor regularizado. Não venda seu voto, é crime!")
    elif cidadao ==5:
      print("Voltando...")
  else:
    print("Notei o tempo de ausencia e por isso encerrei o chamado!")

  




















