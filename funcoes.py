from os import system

def clear():
    Sop = input("Sistema operacional (W|M|L): ").upper()
    if Sop == 'W':
        clearscreen = system('cls')
    else:
        clearscreen = system('clear')

class user:

    def __init__(self):

        self.f = open("userData.txt")
        self.line = self.f.readline()
        self.f.seek(0)

        if self.line == '':
            self.login()

        self.linha = str(self.f.readline()).split('&')
        self.f.close()
        self.Submit = self.linha[0].split('=')
        self.Submit = self.Submit[1]

        self.LOGIN = self.linha[0].split('=')
        self.LOGIN = self.LOGIN[1]

        self.SENHA = self.linha[0].split('=')
        self.SENHA = self.SENHA[1]

        self.TIPO_USU = self.linha[0].split('=')
        self.TIPO_USU = self.TIPO_USU[1]


    def form(self):
        return {"Submit": self.Submit,
        "LOGIN": self.LOGIN,
        "SENHA": self.SENHA,
        "TIPO_USU": self.TIPO_USU}

    def login(self):
        from getpass import getpass
        f = open("userData.txt", mode='w')
        self.linha = input("Form data: ")
        f.write(self.linha)


    def logout(self):
        f = open("userData.txt", mode='w')
        f.write('')
        f.close()
