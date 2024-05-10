from random import randint


def interface_usuario(opcoes):
    '''
    Função que apresenta as opções e pergunta para o jogador a opção pretendida
    Retorna um inteiro.
    '''
    for indice, opcao in enumerate(opcoes):
        print(f'{indice} = {opcao}')

    entrada_usuario = int(input('Qual sua opção? '))
    return entrada_usuario

def escolha_computador(conteudo):
    "funcao que gera a escolha aleatoria de uma opcao dentre as disponiveis. retorna um inteiro aleatorio"
    entrada_computador = randint(0, len(conteudo) - 1)
    return entrada_computador

def verifica_resultado(escolhas, jogador, computador):

    "funcao que verifica quem ganhou e retorna uma string"

    if jogador == computador:
        return 'empatou!!'
    elif (jogador == 00 and computador == len(escolhas) - 1) or (
            jogador > computador and not (jogador == len(escolhas) - 1 and computador == 0)):
        return 'voce ganhou!!'
    return 'voce perdeu!'

def jogar():
    print("bem vindo ao pedra, papel e tesoura. Preparase!")

    #define as opcoes e pergunta a cada um a sua escolha
    lista_opcoes = ['pedra', 'papel', 'tesoura']
    resultado_jogador = interface_usuario(lista_opcoes)
    resultado_computador = escolha_computador(lista_opcoes)

    # representacao visual no terminal qual foi a opcao escolhida por cada um
    print(f'      sua escolha: {lista_opcoes[resultado_jogador]}')
    print(f'escolha do computador: {lista_opcoes[resultado_computador]}')

    # checa o resultado entre as duas opcoes e mostra o ganhador
    resultado = verifica_resultado(lista_opcoes, resultado_jogador, resultado_computador)
    print(f'\n{resultado}')

def main():
    # forca um loop e jogos até o jogador decidir parar,
    jogar_novamente = ''
    while jogar_novamente.lower() != 'n':
        jogar()
        print(f'voce gostaria de jogar novamente? ')
        jogar_novamente = input('digite \'s\' para um sim ou \'n\' para um não: ')


# aqui inicia a execucao do programa

main()