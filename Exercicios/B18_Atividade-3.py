"""
Pedro Henrique Jaber Cavalcante
22107003
27/10/2021
"""
"""
1. Crie uma superclasse com o método construtor e pelo menos um atributo.

2. Crie os métodos gets e sets do atributo da superclasse.

3. Crie pelo menos um método funcional na superclasse.

4. Crie uma subclasse com o método construtor e pelo menos dois atributos.

5. Crie os métodos gets e sets dos atributos da superclasse.

6. No método main, teste (use) as classes criadas, crie pelo menos um objeto 
da superclasse e pelo menos um objeto da subclasse.

7. E teste (use) todos os métodos desenvolvidos nas classes.

Prof. Barbosa
"""

import random
import math


class SuperClasse:

    def __init__(self,args_1=0,args_2=0):
        self.args_1 = args_1
        self.args_2 = args_2
        self.args_3 = self.gera_args()

    def __str__(self):
        return f"Super Classe:\n" \
               f"Args 1: {self.args_1:8.2f}\n" \
               f"Args 2: {self.args_2:8.2f}\n" \
               f"Args 3: {self.args_3:8.2f}\n" \
               f"----------------\n"

    def get_args_1(self):
        return self.args_1

    def set_args_1(self,num):
        if type(num) == int or type(num) == float:
            self.args_1 = num
        else:
            print("[Paramentro Do Tipo Errado]")

    def get_args_2(self):
        return self.args_2

    def set_args_2(self, num):
        if type(num) == int or type(num) == float:
            self.args_2 = num
        else:
            print("[Paramentro Do Tipo Errado]")

    def get_args_3(self):
        return self.args_3

    def set_args_3(self, num):
        if type(num) == int or type(num) == float:
            self.args_3 = num
        else:
            print("[Paramentro Do Tipo Errado]")

    def gera_args(self):
        # 1 ** 3 = 2
        return math.log(self.args_2, self.args_1)

class SubClasse(SuperClasse):

    def __init__(self,args_1=0,args_2=0,args_3=0,args_4=0):
        super().__init__(args_1*args_1,args_2*args_2)

        self.args_3 = self.gera_args() + args_3
        self.args_4 = args_4**(self.gera_args() ** self.gera_args())

    def __str__(self):
        return f"SubClasse:\n" \
               f"Args 1: {self.args_1:8.2f}\n" \
               f"Args 2: {self.args_2:8.2f}\n" \
               f"Args 3: {self.args_3:8.2f}\n" \
               f"Args 4: {self.args_4:8.2f}\n" \
               f"----------------\n"

    def get_args_4(self):
        return self.args_4

    def set_args_4(self, num):
        if type(num) == int or type(num) == float:
            self.args_4 = num
        else:
            print("[Paramentro Do Tipo Errado]")

if __name__ == '__main__':

    args1 = random.randint(0,100)
    args2 = random.randint(0,100)
    args3 = random.randint(0,100)
    args4 = random.randint(0,100)

    # sup_classe = SuperClasse(40,60)
    # sub_classe = SubClasse(40,60,24,67)

    sup_classe = SuperClasse(args1, args2)
    sub_classe = SubClasse(args1, args2, args3, args4)

    print(sup_classe)
    print(sub_classe)

    sub_classe.set_args_4(12)

    print("SubClasse:")
    print(sub_classe.get_args_1())
    print(sub_classe.get_args_2())
    print(sub_classe.get_args_3())
    print(sub_classe.get_args_4())
    print("---------------------\n")


    sup_classe.set_args_2(sub_classe.gera_args())
    sub_classe.set_args_1(sub_classe.gera_args())

    print(sup_classe)
    print(sub_classe)









