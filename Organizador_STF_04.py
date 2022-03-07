import dsd

# importa dados do arquivo indicado como parâmetro
dados = dsd.csv_to_list('InformacoesProcessuais.txt')

# coloca os dados em ordem alfabética decrescente
dados.sort(reverse = True)

# retira o cabeçalho e limita a quantidade inicial de processos
dados = dados[1:51]

# define arquivo a gravar
arquivo = 'STF_total.txt'
dsd.limpar_arquivo(arquivo)

#cria lista para armazenar todos os dados
dados_totais = []

# iteração para extrair os dados de cada processo
for item in dados:
    
    # defindo campos já individualizados
    processo = item[0]
    incidente = item[1]
    
    # extrai dados do campo html_CC
    html_CC = item[4]
    
    cln = dsd.extrair(html_CC,
                              '<div id="divImpressao"><div><h3><strong>',
                              '</strong>')

    origem = dsd.extrair(html_CC,
                              'Origem:</td><td><strong>',
                              '</strong>')
    
    entrada = dsd.extrair(html_CC,
                              'Entrada no STF:</td><td><strong>',
                              '</strong>')
    
    
    relator = dsd.extrair(html_CC,
                              'Relator:</td><td><strong>',
                              '</strong>')
    
    
    # define os dados a serem gravados
    dados_processo = [processo,
                      incidente,
                      cln,
                      origem,
                      entrada,
                      relator]
    
    # armazena os dados na lista (para facilitar vizualização dos testes)
    dados_totais.append(dados_processo)
    
    # grava csv
    print (f'Processando {processo}')
    dsd.write_csv_header(arquivo,'''processo,
                      incidente,
                      cln,
                      origem,
                      entrada,
                      relator''')
    dsd.write_csv_row(arquivo,dados_processo)

print (f'Gravado arquivo {arquivo}')