import dsd

# Importa dados do arquivo indicado como parâmetro
dados = dsd.csv_to_list('InformacoesProcessuais.txt')

# Coloca os dados em ordem alfabética decrescente
dados.sort(reverse = True)

# Retira o cabeçalho e limita a quantidade inicial de processos
dados = dados[1:]

# Define arquivo a gravar
arquivo = 'STF_total.txt'
dsd.limpar_arquivo(arquivo)
dsd.limpar_arquivo('dispositivos_CC.txt')

# Cria lista para armazenar todos os dados
dados_totais = []


# Iteração para extrair os dados de cada processo
for item in dados:
    
    # Redefine variáveis
    processo = 'NA'
    incidente = 'NA'
    pedido_de_liminar_CC =  'NA'
    origem_CC =  'NA'
    entrada_CC =  'NA'
    relator_CC =  'NA'
    requerente_tipo_CC =  'NA'
    fundamento_CC =  'NA'
    resultado_liminar_CC =  'NA'
    orgao_liminar_CC =  'NA'
    resultado_final_CC =  'NA'
    orgao_resultado_final_CC =  'NA'
    monocratica_final_CC =  'NA'
    indexacao_CC =  'NA'
    prevencao_CC =  'NA'
    
    # Defindo campos já individualizados
    processo = item[0]
    incidente = item[1]
    data_extracao = item[2]
    html_CC = item[3]
    html_IP = item[4]
    informacoes = item[5]  
    partes = item[6] 
    andamentos = item[7]  
    recursos = item[8] 

    
    
    # Extrai dados do campo html_CC
    if ('ADI' in processo or
        'ADPF' in processo or
        'ADO' in processo or 
        'ADC' in processo):
    
        ## Extrai e trata o campo cln_CC
        
        pedido_de_liminar_CC = dsd.extrair(html_CC,
                                  '<div id="divImpressao"><div><h3><strong>',
                                  '</strong>').upper()
        ### Remove acentos
        pedido_de_liminar_CC = dsd.remover_acentos(pedido_de_liminar_CC)
        ### Extrai a informação sobre pedido de liminar na petição inicial
        if '(MED. LIMINAR)' in pedido_de_liminar_CC:
        	pedido_de_liminar_CC = 'SIM'
        ### Reduz o nome da ação para a sigla ADI
        pedido_de_liminar_CC = pedido_de_liminar_CC.replace(
            'ACAO DIRETA DE INCONSTITUCIONALIDADE',
            'ADI')
    
    
        # Extrai e trata o campo origem_CC  
        origem_CC = dsd.extrair(html_CC,
                                  'Origem:</td><td><strong>',
                                  '</strong>').upper()
        ### Remove acentos
        origem_CC = dsd.remover_acentos(origem_CC)
    
        
        ## Extrai e trata o campo entrada_CC
        entrada_CC = dsd.extrair(html_CC,
                                  'Distribuído:</td><td><strong>',
                                  '</strong>').upper() 
        ### Remove acentos
        entrada_CC = dsd.remover_acentos(entrada_CC)
        entrada_CC = entrada_CC.replace('-','/')
        entrada_CC = dsd.ajustar_mes(entrada_CC)
        
        
        ## Extrai e trata o campo relator_CC
        relator_CC = dsd.extrair(html_CC,
                                  'Relator:</td><td><strong>',
                                  '</strong>').upper()    
        ### Remove acentos
        relator_CC = dsd.remover_acentos(relator_CC)
        ### Exclui o trecho MINISTRO/A e variações
        relator_CC = relator_CC.replace('MINISTRO','')
        relator_CC = relator_CC.replace('MINISTRA','')
        relator_CC = relator_CC.replace('MIINISTRO','')
        relator_CC = relator_CC.replace('MIMISTRO','')
        relator_CC = relator_CC.replace('MININISTRO','')
        
        
        ## Extrai e trata o campo requerente_CC
        requerente_CC = dsd.extrair(html_CC,
                                  'Requerente: <strong>',
                                  '</strong>').upper() 
        ### Remove acentos
        requerente_CC = dsd.remover_acentos(requerente_CC)
        ### Corrige dados fora do padrão
        requerente_CC = requerente_CC.replace('103 ','103,')
        requerente_CC = requerente_CC.replace('103 ','103.')
        ### Extrai o inciso com o tipo do requerente
        if '103,' in requerente_CC:
            requerente_CC = requerente_CC.split('103,')[1]
            ### limpa o tipo do requerente
            requerente_CC = requerente_CC.strip()
            requerente_CC = requerente_CC.strip('0')
            requerente_CC = requerente_CC.strip(')')
        # Converte o campo requerente em tipo de requerente
        requerente_tipo_CC = requerente_CC
        
    
        ## Extrai e trata o campo dispositivo_CC
        dispositivo_CC = dsd.extrair(html_CC,
                                  'Legal Questionado</b></strong><br /><pre>',
                                  '</pre>')
        
        
        # Extrai e trata o campo fundamento_CC
        fundamento_CC = dsd.extrair(html_CC,
                                  'Constitucional</b></strong><br /><pre>',
                                  '</pre>').upper() 
        ### Remove acentos
        fundamento_CC = dsd.remover_acentos(fundamento_CC)
        # Limpa o campo
        fundamento_CC = fundamento_CC.replace('- ART','ART')
        fundamento_CC = fundamento_CC.strip('\n')
        # Gera lista de fundamentos
        fundamento_CC = fundamento_CC.split('\n')
       
        
        ## Extrai e trata o campo resultado_liminar_CC
        resultado_liminar_CC = dsd.extrair(html_CC,
                            'Resultado da Liminar</b></strong><br /><br />',
                            '<br />').upper()    
        ### Remove acentos
        resultado_liminar_CC = dsd.remover_acentos(resultado_liminar_CC)
        ### Define campo para identificar decisões monocráticas
        orgao_liminar_CC = 'NA'
        ### Corrige dados fora do padrão
        resultado_liminar_CC = resultado_liminar_CC.replace('MONOACRATICA',
                                                            'MONOCRATICA')
        resultado_liminar_CC = resultado_liminar_CC.replace('LIMINAR ','')
        ### Gera campo órgão nos casos de decisão monocrática
        if 'DECISAO MONOCRATICA - ' in resultado_liminar_CC:
            resultado_liminar_CC = resultado_liminar_CC.replace(
                                                    'DECISAO MONOCRATICA -','')
            orgao_liminar_CC = 'MONOCRATICA'
       
            
        # Extrai e trata o campo resultado_final_CC
        resultado_final_CC = dsd.extrair(html_CC,
                                  'Resultado Final</b></strong><br /><br />',
                                  '<br />').upper()
        ### Remove acentos
        resultado_final_CC = dsd.remover_acentos(resultado_final_CC)
        ### Define o campo orgao
        orgao_resultado_final_CC = 'NA'
        ### Corrige dados fora do padrão
        resultado_final_CC = resultado_final_CC.replace('MONOCRATICO',
                                                            'MONOCRATICA')
        ### Gera campo orgao
        if 'DECISAO MONOCRATICA - ' in resultado_final_CC:
            resultado_final_CC = resultado_final_CC.replace(
                'DECISAO MONOCRATICA -','')
            orgao_resultado_final_CC = 'MONOCRATICA'
        
        
        # Extrai e trata o campo monocratica_final_CC
        monocratica_final_CC = dsd.extrair(html_CC,
                        'Decisão Monocrática Final</b></strong><br /><pre>',
                        '</pre>')
        
        
        ## Extrai e trata o campo indexacao_CC
        indexacao_CC = dsd.extrair(html_CC,
                                  'Indexação</b></strong><br /><pre>',
                                  '</pre>').upper()
        ### Remove acentos
        indexacao_CC = dsd.remover_acentos(indexacao_CC)
        ### Cria o campo prevenção
        prevencao_CC = 'NA'
        ### Limpa o campo indexação de textos indevidos
        indexacao_CC = indexacao_CC.replace('<BR />','')
        ### Gera o dado sobre prevenção e adapta o campo indexação
        if 'PREVENCAO' in indexacao_CC:
            prevencao_CC = dsd.extrair(indexacao_CC, 'PREVENCAO - ', '\n')
            indexacao_CC = dsd.extrair(indexacao_CC, prevencao_CC,'')
    
    
    # Define os dados a serem gravados
    dados_processo =    [processo,
                        incidente,
                        pedido_de_liminar_CC,
                        origem_CC,
                        entrada_CC,
                        relator_CC,
                        requerente_tipo_CC,
                        fundamento_CC,
                        resultado_liminar_CC,
                        orgao_liminar_CC,
                        resultado_final_CC,
                        orgao_resultado_final_CC,
                        monocratica_final_CC,
                        indexacao_CC,
                        prevencao_CC]
    
    # Grava csv
    print (f'Processando {processo}')
    dsd.write_csv_header(arquivo,
                        '''processo,
                        incidente,
                        pedido_de_liminar_CC,
                        origem_CC,
                        entrada_CC,
                        relator_CC,
                        requerente_tipo_CC,
                        fundamento_CC,
                        resultado_liminar_CC,
                        orgao_liminar_CC,
                        resultado_final_CC,
                        orgao_resultado_final_CC,
                        monocratica_final_CC,
                        indexacao_CC,
                        prevencao_CC''')
    dsd.write_csv_row(arquivo,dados_processo)
    
    # Grava o arquivo com os dispositivos legais impugnados
    dsd.write_csv_header('dispositivos_CC.txt','processo,dispositivo')
    dsd.write_csv_row('dispositivos_CC.txt',[processo,dispositivo_CC])

# Grava mensagem de finalização do progama com êxito
print (f'Gravado arquivo {arquivo}')