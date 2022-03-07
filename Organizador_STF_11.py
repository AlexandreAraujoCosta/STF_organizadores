import dsd

# Importa dados do arquivo indicado como parâmetro
dados = dsd.csv_to_list('InformacoesProcessuais5.txt')

# Coloca os dados em ordem alfabética decrescente
dados.sort(reverse = True)

# Retira o cabeçalho e limita a quantidade inicial de processos
dados = dados[-1:]