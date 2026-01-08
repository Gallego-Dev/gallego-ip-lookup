# Buscador de ip simples
# Gallego-Dev

import requests
import time
import os

def limpar_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
logo = (r"""              .__  .__                        
   _________  |  | |  |   ____   ____   ____  
  / ___\__  \ |  | |  | _/ __ \ / ___\ /  _ \ 
 / /_/  > __ \|  |_|  |_\  ___// /_/  >  <_> )
 \___  (____  /____/____/\___  >___  / \____/ 
/_____/     \/               \/_____/         
                  .__                         
                  |__|_____                   
                  |  \____ \                  
                  |  |  |_> >                 
                  |__|   __/                  
                     |__|                     
      .__                 __                  
      |  |   ____   ____ |  | ____ ________   
      |  |  /  _ \ /  _ \|  |/ /  |  \____ \  
      |  |_(  <_> |  <_> )    <|  |  /  |_> > 
      |____/\____/ \____/|__|_ \____/|   __/  
                              \/     |__|     """)
time.sleep(3)
limpar_logo()
time.sleep(0.3)

print('Informe o ip \nExemplo: 8.8.8.8')
ip = input('ip>')
url = f"http://ip-api.com/json/{ip}"
resposta = requests.get(url).json()
print('='*30)
print(f"IP: {resposta['query']}")
print(f"País: {resposta['country']}")
print(f"Cidade: {resposta['city']}")
print(f"ISP: {resposta['isp']}")
print(f"ASN: {resposta['as']}")
print('='*30)
