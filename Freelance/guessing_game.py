def jogo_de_adivinhacao(secreto, start=1, end=1000):
    tentativas = 0

    while start <= end:
        tentativas += 1 #guesses counter
        chute = (start + end) // 2 #the guess

        if chute == secreto:
            print(f'Tentativa {tentativas}: chute = {chute} -> Acertou!') #shows in which try it was found and the guess
            print(f'\nNúmero descoberto: {secreto}') #prints the number if guessed right
            print(f'Total de tentativas: {tentativas}') #the total number of tries
            return tentativas

        elif chute < secreto:
            print(f'Tentativa {tentativas}: chute = {chute} -> O número é maior') #guess < number 
            start = chute + 1
        else:
            print(f'Tentativa {tentativas}: chute = {chute} -> O número é menor') #guess > number
            end = chute - 1

    print('Número fora do intervalo informado.') #if the number wasn't found
    return -1

jogo_de_adivinhacao(10)