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
    tamanho_nome = len(nome_escolhido)
    return nome_escolhido, tamanho_nome

def Jogar():
   
   chute = input("Digite uma letra: ").strip().lower()
   return chute

def tentativa_atual(chute, nome_escolhido):
    
    for chute in nome_escolhido:
        