import dsd

# importa dados do arquivo indicado como parâmetro
dados = dsd.csv_to_list('InformacoesProcessuais.txt')

# coloca os dados em ordem alfabética decrescente
dados.sort(reverse = True)

# retira o cabeçalho e limita a quantidade inicial de processos
dados = dados[1:11]   