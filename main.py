import requests
from bs4 import BeautifulSoup as bs
import dados, funcoes

#Página inicial - Pegar dados do usuário

usr = funcoes.user()

with requests.Session() as s:
    TELA_INICIAL = s.post(dados.url_inicio, headers=dados.user_agent)
    print(TELA_INICIAL.status_code)
    GERA_CHAVE = s.get(dados.url_chave, params=dados.params_gera_chave, headers=dados.header_chave)
    print(GERA_CHAVE.status_code)
    VALIDA_LOGIN = s.post(dados.url_valida, headers=dados.header_valida, data=usr.form())
    print(VALIDA_LOGIN.status_code)
    TELA_DE_ENTRADA = s.get(dados.url_entrada, headers=dados.header_entrada)
    print(TELA_DE_ENTRADA.status_code)
    VALIDA_BOLETIM = s.get("https://academico.iff.edu.br/qacademico/alunos/boletim/index.asp", headers=dados.header_entrada)
    print(VALIDA_BOLETIM.status_code)
    BOLETIM = s.get("https://academico.iff.edu.br/qacademico/index.asp?t=2032", headers=dados.header_entrada)
    print(BOLETIM.text)
