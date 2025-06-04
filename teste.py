nome = 'fernando'
tentativa = 0
resposta = ['_'] * len(nome)
acerto = 0
letras_chutadas = []

while True:
    chute = input("\nFaça seu chute: ").strip().lower()

    if chute in letras_chutadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_chutadas.append(chute)
    tentativa += 1
    

    for indice, letra in enumerate(nome):
        if letra == chute and resposta[indice] == '_':
            resposta[indice] = letra
            acerto += 1
            

    print("Palavra: ", ' '.join(resposta))
    print("Tentativas:", tentativa)

    if acerto == len(nome):
        print("\nParabéns, você ganhou!")
        print("Palavra:", nome)
        break

    if tentativa >= len(nome) + 3: 
        print("\nJogo encerrado, você perdeu.")
        print("Palavra era:", nome)
        break
