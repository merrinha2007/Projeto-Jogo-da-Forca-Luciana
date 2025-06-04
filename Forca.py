possiveis_nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana', 'Lucas', 'Mariana', 'Nathalia', 'Otávio', 'Paulo', 'Quesito', 'Rafael', 'Sofia', 'Talita', 'Urbano', 'Vitor', 'Wagner', 'Xavier', 'Yago', 'Zacarias']
import random as rd
def exibir_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        ''',
        '''
           -----
           |   |
           |   O
           |  /|
           |
           -
        ''',
        '''
           -----
           |   |
           |   O
           |   |
           |
           -
        ''',
        '''
           -----
           |   |
           |   O
           |
           |
           -
        ''',
        '''
           -----
           |   |
           |
           |
           |
           -
        ''',
        '''
           -----
           
           
           
           
           
        '''
    ]
    return estagios[tentativas]

def escolher_nome():
    nome_escolhido = rd.choice(possiveis_nomes)
    print(nome_escolhido)
    tamanho_nome = len(nome_escolhido)
    return nome_escolhido, tamanho_nome

def Jogar(nome_escolhido):
   
   
   chute = input("Digite uma letra: ").strip().lower()
   for chute in escolher_nome():
       if chute in nome_escolhido == True:
           print(chute)
           
   return chute


