linhas_vistas = set() #Conjuntos de linhas já vistas.
arq_out = open("relatos_sem_repeticao.txt", "w", encoding='utf8') # abre o arquivo de escrita (ou cria caso nao exista)

for line in open("relatos_com_repeticao.txt", "r", encoding='utf8'):
    if line not in linhas_vistas: # se a linha não está dentro do conjunto linhas_vistas, escreve no arquivo
        arq_out.write(line)
        linhas_vistas.add(line) # adiciona a linha iterada ao conjunto de linhas vistas
arq_out.close()