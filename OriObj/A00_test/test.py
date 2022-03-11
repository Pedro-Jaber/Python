


class Test:

    def __init__(self, num1, num2, str3):
        self.__var1 = num1
        self.__var2 = num2
        self.__var3 = str3

    def __str__(self):
        return f"num1 = {self.__var1}\nnum2 = {self.__var2}\nnum3 = {self.__var3}\n"

    @property
    def var1(self):
        return self.__var1

    @var1.setter
    def var1(self, num):
        self.__var1 = num + 5


if __name__ == '__main__':
    test = Test(1,2,3)

    print(test)

    test.var1 = 10

    print(test)



































