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
    
    # extrai e trata o campo cln_CC
    cln_CC = dsd.extrair(html_CC,
                              '<div id="divImpressao"><div><h3><strong>',
                              '</strong>').upper()
    
    cln_CC = dsd.remover_acentos(cln_CC)

    # extrai e trata o campo origem_CC
    origem_CC = dsd.extrair(html_CC,
                              'Origem:</td><td><strong>',
                              '</strong>').upper()
    
    origem_CC = dsd.remover_acentos(origem_CC)
    
    # extrai e trata o campo entrada_CC
    entrada_CC = dsd.extrair(html_CC,
                              'Distribuído:</td><td><strong>',
                              '</strong>').upper()
    
    entrada_CC = dsd.remover_acentos(entrada_CC)
    
    # extrai e trata o campo relator_CC
    relator_CC = dsd.extrair(html_CC,
                              'Relator:</td><td><strong>',
                              '</strong>').upper()
    
    relator_CC = dsd.remover_acentos(relator_CC)
    
    # extrai e trata o campo requerente_CC
    requerente_CC = dsd.extrair(html_CC,
                              'Requerente: <strong>',
                              '</strong>').upper() 
    
    requerente_CC = dsd.remover_acentos(requerente_CC)
    
    # extrai e trata o campo requerido_CC
    requerido_CC = dsd.extrair(html_CC,
                              'Requerido :<strong>',
                              '</strong>').upper()
    
    requerido_CC = dsd.remover_acentos(requerido_CC)

    # extrai e trata o campo dispositivo_CC
    dispositivo_CC = dsd.extrair(html_CC,
                              'Legal Questionado</b></strong><br /><pre>',
                              '</pre>')
    
    # extrai e trata o campo fundamento_CC
    fundamento_CC = dsd.extrair(html_CC,
                              'Constitucional</b></strong><br /><pre>',
                              '</pre>').upper() 
    
    fundamento_CC = dsd.remover_acentos(fundamento_CC)
    
    # extrai e trata o campo resultado_liminar_CC
    resultado_liminar_CC = dsd.extrair(html_CC,
                              'Resultado da Liminar</b></strong><br /><br />',
                              '<br />').upper()
    
    resultado_liminar_CC = dsd.remover_acentos(resultado_liminar_CC)
    
    # extrai e trata o campo resultado_final_CC
    resultado_final_CC = dsd.extrair(html_CC,
                              'Resultado Final</b></strong><br /><br />',
                              '<br />').upper()
    
    resultado_final_CC = dsd.remover_acentos(resultado_final_CC)
    
    # extrai e trata o campo monocratica_final_CC
    monocratica_final_CC = dsd.extrair(html_CC,
                        'Decisão Monocrática Final</b></strong><br /><pre>',
                        '</pre>')
    
    # extrai e trata o campo indexacao_CC
    indexacao_CC = dsd.extrair(html_CC,
                              'Indexação</b></strong><br /><pre>',
                              '</pre>').upper()
    
    indexacao_CC = dsd.remover_acentos(indexacao_CC)
    
    
    # define os dados a serem gravados
    dados_processo =    [processo,
                        incidente,
                        cln_CC,
                        origem_CC,
                        entrada_CC,
                        relator_CC,
                        requerente_CC,
                        requerido_CC,
                        dispositivo_CC,
                        fundamento_CC,
                        resultado_liminar_CC,
                        resultado_final_CC,
                        monocratica_final_CC,
                        indexacao_CC]
    
    # armazena os dados na lista (para facilitar vizualização dos testes)
    dados_totais.append(dados_processo)
    
    # grava csv
    print (f'Processando {processo}')
    dsd.write_csv_header(arquivo,
                        '''processo,
                        incidente,
                        cln_CC,
                        origem_CC,
                        entrada_CC,
                        relator_CC,
                        requerente_CC,
                        requerido_CC,
                        dispositivo_CC,
                        fundamento_CC,
                        resultado_liminar_CC,
                        resultado_final_CC,
                        monocratica_final_CC,
                        indexacao_CC''')
    dsd.write_csv_row(arquivo,dados_processo)

print (f'Gravado arquivo {arquivo}')