def iniciar():
    print('Olá! Bem-vindo ao Alfredinho, o seu treinador de fim de semana!')
    nome = input('Antes de começarmos, como você gostaria de ser chamado(a)?\n')

    print('---------------------------------------------------------\n'
          f'É um prazer, {nome}!\n'
          'Como está seu humor?')

    humor = int(input('---------------------------------------------------------\n' 
                      '1. Estou cansado e só quero relaxar\n'
                      '2. Quero me divertir e estar com amigos\n'
                      '3. Estou cheio de energia e quero uma aventura\n'
                      '4. Estou me sentindo criativo e quero fazer algo cultural\n'
                      '---------------------------------------------------------\n'))

    print('Quanto tempo disponível você tem? ')
    tempo = int(input('---------------------------------------------------------\n'
                      '1. Tenho apenas uma hora\n'
                      '2. Tenho a tarde livre\n'
                      '3. O dia todo está livre\n'
                      '---------------------------------------------------------\n'))

    print('Qual seu orçamento? ')
    orcamento = int(input('---------------------------------------------------------\n'
                          '1. Menos de R$ 50,00\n'
                          '2. Até R$ 100,00\n'
                          '3. Sem limite, quero aproveitar ao máximo\n'
                          '---------------------------------------------------------\n'))

    print('Quais são seus interesses culturais? ')
    int_cult = int(input('---------------------------------------------------------\n'
                         '1. Cinema\n'
                         '2. Música\n'
                         '3. Artes\n'
                         '4. Gastronomia\n'
                         '---------------------------------------------------------\n'))

    if humor == 1 and tempo == 1 and orcamento == 1 and int_cult == 1:
        print('Você pode ir ao Cinema São Luiz! Lá, poderá conferir alguns curta metragens e se divertir gastando pouco. '
              'No caminho, apreciará as belas vistas de Recife.')
    elif humor == 2 and tempo == 2 and orcamento == 2 and int_cult == 2:
        print('A tarde pode ser animada com atrações musicais como shows e eventos em bares. Vá ao Cais da Alfândega com atrações '
              'variadas, seguido da Orquestra Bravo no Marco Zero com apresentação gratuita.')
    elif humor == 3 and tempo == 3 and orcamento == 3 and int_cult == 3:
        print('Comece o dia na praia de Boa Viagem, depois visite o Paço do Frevo e termine com um passeio de catamarã no Capibaribe!')
    elif humor == 2 and tempo == 3 and orcamento == 3 and int_cult == 4:
        print('Sugestão gastronômica:\n'
              '• Quina do Futuro | $$$ | ★ 4.5\n'
              '• Nez Bistrô | $$$ | ★ 4.5\n'
              '• Chiwake | $$$$ | ★ 4.5\n'
              'Depois, divirta-se no Cais Rooftop | $$$ | ★ 4.0')
    else:
        print('Sugestões gerais com base nas suas escolhas:\n'
              '• Praia de Boa Viagem\n'
              '• Catamarã pelo Rio Capibaribe\n'
              '• Parque da Jaqueira\n'
              '• Cinema no Shopping Tacaruna\n'
              '• Paço do Frevo')

    print('\nDeseja voltar para o menu principal?')
    opcao = input('1. Sim\n2. Não\n')

    if opcao == "1":
        return  
    elif opcao == "2":
        print("Encerrando... 👋")
        exit()
