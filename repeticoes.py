#nao esta funcionando corretamente, preserva duas linhas ao inves de uma

linhas_vistas = set() #Conjuntos de linhas já vistas.
arq_out = open("relatos_sem_repeticao.txt", "w", encoding='utf8') #Abre o arquivo de escrita

for line in open("relatos_com_repeticao.txt", "r", encoding='utf8'):
    if line not in linhas_vistas: #se a linha não está dentro do conjunto linhas_vistas
        arq_out.write(line)
        linhas_vistas.add(line) #O item de comparação se trata do conjunto linhas vistas
arq_out.close()