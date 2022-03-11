






contatos_arquivo = open("dados/contatos_escrita.csv", encoding='latin_1', mode='w+')

contatos_novos = ['11,Carol,carol@carol.com.br\n',
                  '12,Ana,ana@ana.com.br\n',
                  '13,Tais,tais@tais.com.br\n',
                  '14,Felipe,felipe@felipe.com.br\n']

for contato in contatos_novos:
    contatos_arquivo.write(contato)

contatos_arquivo.flush() #força a inserção antes de fechar o arquivo

contatos_arquivo.seek(0) #volta para o inicio do arquiovo ou no caractere indicado

for linha in contatos_arquivo:
    print(linha,end='')











