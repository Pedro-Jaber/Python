#
#
#
#
#
#
try:
    contatos = open("dados/contatos.csv", encoding='latin_1')

    # conteudo = contatos.readline(10)
    #
    # print(conteudo)
    #
    # conteudo = contatos.readline()
    #
    # print(conteudo)

    for linha in contatos:
        print(linha,end='')


finally:
    contatos.close()
