#Bot check Bypass
#str_header = input("Cole aqui os headers: ") #Próxima versão headers automáticos

user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

params_gera_chave = {"form": {"LOGIN":201619110466, "SENHA":201619110466, "TIPO_USU":1, "SUBMIT":"OK"}, "action": "/qacademico/lib/validalogin.asp"}

header_valida_boletin = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "keep-alive",
"Cookie": "__utmz=115131543.1552797514.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASPSESSIONIDCSDCTRTA=FHGGHNJDAOLHIIGDJIKPKFOG; __utmc=115131543; __utma=115131543.151265915.1552797514.1552927579.1552941263.5; __utmt=1; __utmb=115131543.9.10.1552941263",
"Host": "academico.iff.edu.br",
"Referer": "https://academico.iff.edu.br/qacademico/index.asp?t=2000",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

header_boletin = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "keep-alive",
"Cookie": "__utmz=115131543.1552797514.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASPSESSIONIDCSDCTRTA=FHGGHNJDAOLHIIGDJIKPKFOG; __utmc=115131543; __utma=115131543.151265915.1552797514.1552927579.1552941263.5; __utmt=1; __utmb=115131543.9.10.1552941263",
"Host": "academico.iff.edu.br",
"Referer": "https://academico.iff.edu.br/qacademico/index.asp?t=2000",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

header_chave = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "keep-alive",
"Cookie": "__utmz=115131543.1552797514.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASPSESSIONIDCSDCTRTA=FHGGHNJDAOLHIIGDJIKPKFOG; __utmc=115131543; __utma=115131543.151265915.1552797514.1552924546.1552927579.4; __utmt=1; __utmb=115131543.11.10.1552927579",
"Host": "academico.iff.edu.br",
"Referer": "https://academico.iff.edu.br/qacademico/index.asp?t=1001",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

header_valida = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Content-Length": "159",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "__utmz=115131543.1552797514.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASPSESSIONIDCSDCTRTA=FHGGHNJDAOLHIIGDJIKPKFOG; __utma=115131543.151265915.1552797514.1552799863.1552924546.3; __utmc=115131543; __utmt=1; __utmb=115131543.1.10.1552924546",
"Host": "academico.iff.edu.br",
"Origin": "https://academico.iff.edu.br",
"Referer": "https://academico.iff.edu.br/qacademico/index.asp?t=1001",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

header_entrada = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "__utmz=115131543.1552797514.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASPSESSIONIDCSDCTRTA=FHGGHNJDAOLHIIGDJIKPKFOG; __utmc=115131543; __utma=115131543.151265915.1552797514.1552927579.1552941263.5; __utmt=1; __utmb=115131543.3.10.1552941263",
"Host": "academico.iff.edu.br",
"Referer": "https://academico.iff.edu.br/qacademico/index.asp?t=1001",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

url_inicio = "https://academico.iff.edu.br/qacademico/index.asp?t=1001"
url_chave = "https://academico.iff.edu.br/qacademico/lib/rsa/gerador_chaves_rsa.asp?form=frmLogin&action=%2Fqacademico%2Flib%2Fvalidalogin%2Easp"
url_valida = "https://academico.iff.edu.br/qacademico/lib/rsa/gerador_chaves_rsa.asp?form=frmLogin&action=%2Fqacademico%2Flib%2Fvalidalogin%2Easp"
url_entrada = "https://academico.iff.edu.br/qacademico/index.asp?t=2000"
url_valida_boletin = "https://academico.iff.edu.br/qacademico/alunos/boletim/index.asp"
url_boletin = "https://academico.iff.edu.br/qacademico/index.asp?t=2032"
