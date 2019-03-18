import funcoes, dados

'''
# test dados module
print(dados.url_entrada)
'''

'''
# test funcoes.clear function
input()
funcoes.clear()
'''

'''
# test user class
usr = funcoes.user()
form = usr.form()
for k in form:
    print(k, form[k], sep='\t')
'''

'''
# test user logout
while True:
    usr = funcoes.user()
    if input("Logout? ") == '1':
        usr.logout()
    form = usr.form()
    for k in form:
        print(k, form[k], sep='\t')
'''
