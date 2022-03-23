from B05_ClassAluno import Aluno





if __name__ == '__main__':
    """
    aluno1 = Aluno('Paulo', 1000.00, 21)

    print("Aluno 1: ")
    print(f"Nome:       {aluno1.get_nome()}")
    print("Mensalida: ", aluno1.get_mensalidade())
    print("Idade:     ", aluno1.get_idade())
    print(aluno1)
    """

    print("----Criando Aluno----")
    nome        = input("Nome: ")
    mensalidade = input("Mensalidade: ")
    idade       = input("Idade: ")

    aluno_novo = Aluno(nome.capitalize(), mensalidade, idade)

    print("\nAluno Registrado ")
    aluno_novo.mostra_dados()
    #print(f"Nome:      {aluno_novo.get_nome()}")
    #print(f"Mensalida: {aluno_novo.get_mensalidade()}")
    #print(f"Idade:     {aluno_novo.get_idade()}")
    print(aluno_novo)

    """
    aluno_novo.set_nome("Top")
    aluno_novo.set_mensalidade(2.00)
    aluno_novo.set_idade(31)

    print("\nAluno Registrado ")
    print(f"Nome:      {aluno_novo.get_nome()}")
    print(f"Mensalida: {aluno_novo.get_mensalidade()}")
    print(f"Idade:     {aluno_novo.get_idade()}")
    print(aluno_novo)
    """








