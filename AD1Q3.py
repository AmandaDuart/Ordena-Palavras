from random import randint

def gerar_matriz(qtd_linhas, qtd_cols, min, max):
    matriz = []
    for linha in range(qtd_linhas):
        nova_linha = []
        for col in range(qtd_cols):
            nova_linha.append(randint(min,max))
        matriz.append(nova_linha)
    return matriz

def mostrar(vals):
    for linha in vals:
        string_linha = ""
        for coluna in linha:
            string_linha += str(coluna) + " "
        print(string_linha)

def media(matriz):
    soma = 0
    cont = 0
    for x in range(0, len(matriz)):
        for y in range(0, len(matriz[0])):
            cont += 1
            soma += matriz[x][y]

    return "%.1f" % (soma / cont)

def borda_acima_media(matriz, v_media):
    valores_acima_media = []

    for x in range(0, len(matriz)):
        for y in range(0, len(matriz[0])):
            if x == 0:
                if matriz[x][y] > v_media:
                    valores_acima_media.append(matriz[x][y])
            elif x == len(matriz) - 1:
                if matriz[x][y] > v_media:
                    valores_acima_media.append(matriz[x][y])
            else:
                if y == 0 or y == len(matriz[0]) - 1:
                    if matriz[x][y] > v_media:
                        valores_acima_media.append(matriz[x][y])

    for valor in valores_acima_media:
        print(valor)



valores = input().split()
q_linhas = int(valores[0])
q_colunas = int(valores[1])
min = int(valores[2])
max = int(valores[3])
valores =  gerar_matriz(q_linhas, q_colunas, min, max)
print("Conteudo da Matriz")
mostrar(valores)
valor_media = media(valores)
print("Média dos valores sorteados:")
print(valor_media)
print('Relação de Valores nas Bordas Acima da Média:')
borda_acima_media(valores, float(valor_media))
