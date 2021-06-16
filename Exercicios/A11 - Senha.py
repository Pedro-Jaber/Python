from termcolor import colored

senha = 123
senhaD = int(input("Digite a senha:"))
if senhaD == senha: print(colored("Acesso Liberado", 'green'))
else: print(colored("Acesso Negado", 'red'))