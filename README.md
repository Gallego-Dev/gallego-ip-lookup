projeto:
  nome: gallego-ip-lookup
  nome_exibicao: Gallego-IP-Lookup 📡
  linguagem: Python 🐍
  versao: "1.0.0"
  finalidade: Educacional / OSINT 🕵️‍♂️
  autor: Gallego-Dev 👨‍💻
  licenca: MIT 📜

arquivos:
  script_principal: gallego_ip_lookup.py
  readme: README.md

cabecalho_comentario: |
  # ==========================================================
  # Gallego-IP-Lookup 📡
  # Autor: Gallego-Dev 👨‍💻
  # Descrição: Ferramenta para consulta de informações públicas de IP
  # Linguagem: Python 🐍
  # Finalidade: Educacional / OSINT 🕵️‍♂️
  # Licença: MIT 📜
  # ==========================================================

descricao: |
  O Gallego-IP-Lookup é uma ferramenta simples em Python para obter
  informações públicas de um endereço IP, como país, cidade,
  provedor de internet (ISP) e ASN, utilizando a API pública
  ip-api.com. Não requer chave de API.

requisitos:
  python: ">=3.8"
  dependencias:
    - requests

instalacao:
  passos:
    - pip install requests

uso:
  comando_execucao: python gallego_ip_lookup.py ▶️
  exemplo_entrada: "8.8.8.8"

exemplo_saida: |
  ==============================
  IP: 8.8.8.8
  País: United States 🇺🇸
  Cidade: Mountain View 🏙️
  ISP: Google LLC 🌐
  ASN: AS15169 Google LLC
  ==============================

observacoes:
  - O IP não revela endereço físico exato 📍
  - VPN, Proxy ou Tor podem mascarar informações 🛡️
  - Uso recomendado apenas para estudos e OSINT básico 📚

aviso_legal: |
  Este projeto é destinado exclusivamente para fins educacionais.
  O autor não se responsabiliza pelo uso indevido das informações.

estrutura_repositorio:
  - gallego-ip-lookup/
  - ├── gallego_ip_lookup.py 🐍
  - ├── README.md 📘
  - └── requirements.txt 📦
