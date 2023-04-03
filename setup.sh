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

echo "[*]instalando recursos e dependências aguarde[*]"
apt update -y;apt install python3 -y;pip3 install --upgrade pip;pip3 install requests

echo "[!] instalação finalizada executando ferramenta...[!]"

python3 scankit.py