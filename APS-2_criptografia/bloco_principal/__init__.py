from cifra_e_decifra import *
 # importação da funcionalidade de cifra e decifra.
import re
 # importação, do método para remover números de string.


def string(text):
    while True:
        msg = input(text) # msg, é a mensagem do bloco prin(), text é o contéudo da mensagem do prin()...
        remove_numeros = re.sub(r'[0-9]+', '', msg)
         # remove_numeros, é a variável, que armazena o método para retirar os números da string.
         # em seguida, ele substitui os números por espaço vázio.
         # e o terceiro passo, é chamar a variável que vai ter o seu conteúdo alterado.
        if remove_numeros:
            tirar_espaco = remove_numeros.replace(' .', '.')
             # tirar_espaco, serve para tirar um espaço a mais, quando é digitado um número real, como por exemplo 5.5...
            return tirar_espaco # retorna o resultado de tirar_espaco.
        elif '' in msg:
            print('\nNão teve digitação. Tente novamente! \n') # se der um enter, sem digitar nada, ou digitar números inteiros, aparece essa frase e vai pedir para digitar a mensagem novamente.
        else:
            return msg # se não tiver números na mensagem, vai retornar a mensagem normalmente !


# bloco principal.
def prin():
    print(f'\n{"Atenção, não digite Números !!!":^49}')
    print(f'{"Porque números, serão ignorados.":^49}\n')

    mensagem = string('Digite sua mensagem, com no máximo 128 caracteres: ')
     # aqui é para especificar o limite de caracteres, da mensagem. E escreve na tela, a mensagem cifrada e decifrada, se tiver até 128 caracteres.
    if len(mensagem) <= 128:
        print(f'\nSua mensagem cifrada será: {cifra(mensagem, lista3)}')
        print(f'\nSua mensagem decifrada será: {decifra(mensagem, lista3)}')
    else:
        print('\nSua mensagem, passou do limite de caracteres, que é 128')
        prin()
         # Se a mensagem passar de 128 caracteres, vai ser exibido esse print.
         # E vai reiniciar o programa, pedindo para digitar uma nova mensagem.
    while True:
        continua = str(input('\nDeseja Cripitografar uma nova mensagem [Sim / Não]? ')).strip().upper()
         # aqui é a parte da repetição, na qual, pergunta se o usuário deseja continuar ou não.
        if continua == 'SIM':
            prin() # se a resposta for sim, vai ser executado o programa novamente.
        elif continua == 'NÃO':
            print('\nFinalizando...'), sleep(1)
            print('Programa finalizado.')
            exit() # agora se digitar Não, vai aparecer Finalizando... com o efeito do sleep de 1s, e vai sair do programa com o exit()...
        else:
            print('\nValor Inválido. Digite Sim ou Não.')
             # se digitar qualquer coisa diferente de sim ou não, vai aparecer este print, e vai executar a pergunta novamente.
