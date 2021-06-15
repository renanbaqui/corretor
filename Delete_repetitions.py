linhas_vistas = set()#Conjuntos de linhas já vistas.
arq_out = open("D:/relatos_revisados_S_Rep.txt", "w", encoding='utf8') #Abre o arquivo de escrita

for line in open("D:/relatos_revisados.txt", "r", encoding='utf8'):
    if line not in linhas_vistas: #se a linha não está dentro do conjunto linhas_vistas
        arq_out.write(line)
        linhas_vistas.add(line) #O item de comparação se trata do conjunto linhas vistas
arq_out.close()
