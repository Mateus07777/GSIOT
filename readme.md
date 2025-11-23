🌿 Projeto Bem-Estar – API

API em Python desenvolvida para analisar dados de bem-estar, oferecendo um índice de saúde, risco de burnout e feedback inteligente com base nas informações enviadas pelo usuário.

👤 Autores

Mateus Teni Pierro – RM555125

Heitor Romero da Rocha – RM558301

Leonardo Bianchi – RM558576

📌 Visão Geral

A API recebe quatro entradas principais:

•
humor

•
foco

•
pausas

•
horas_trabalhadas

E retorna:

•
✔ índice de bem-estar

•
✔ risco de burnout

•
✔ feedback automático

•
✔ dados recebidos

Esta aplicação foi projetada para integração com apps mobile, dashboards ou sistemas de análise de comportamento.

🌐 Deploy da API

A API está hospedada no Render com deploy automático a partir da branch main.

🔗 URL Base

👉 https://projeto-bem-estar-api.onrender.com

Ao acessar a URL base, você verá uma página de status confirmando que a API está online.

🔐 Autenticação

Nenhuma autenticação é exigida. A API está totalmente aberta para testes.

🗄 Banco de Dados

Este projeto não utiliza banco externo. Todos os cálculos são processados em memória.

🧱 Estrutura do Projeto

Plain Text


projeto_bem_estar/
│
├── api/
│   ├── templates/       # Arquivos HTML
│   │   └── index.html   # Página de status da API
│   ├── app.py           # Rotas e inicialização da API
│   ├── services.py      # Lógica de negócio (cálculos )
│   ├── .env             # Variáveis de ambiente (uso local)
│   └── requirements.txt # Dependências
│
├── venv/                # Ambiente virtual (não enviado ao GitHub)
├── .gitignore
└── README.md            # Documentação do projeto


⚙️ Como Executar o Projeto Localmente

1.
Criar ambiente virtual

2.
Ativar ambiente virtual

•
Windows:

•
Linux/Mac:



3.
Instalar dependências

4.
Rodar a API

📡 Rotas da API

✔ GET /

Verifica se a API está online. Esta rota agora retorna uma página HTML de status.

✔ POST /analyze-checkin

Analisa dados de bem-estar enviados pelo usuário.

📤 Exemplo de Requisição

POST https://projeto-bem-estar-api.onrender.com/analyze-checkin

Body (JSON ):

JSON


{
  "humor": 3,
  "foco": 2,
  "pausas": 2,
  "horas_trabalhadas": 9
}


📥 Exemplo de Resposta (200 OK)

JSON


{
  "dados_recebidos": {
    "foco": 2,
    "horas_trabalhadas": 9,
    "humor": 3,
    "pausas": 2
  },
  "feedback_ia": "Percebo que seu bem-estar está um pouco abaixo do ideal...",
  "indice_bem_estar": 2.33,
  "risco_burnout": 1.2
}


📘 Descrição dos Campos Enviados

Campo
Tipo
Descrição
humor
int (1–5)
Avaliação emocional do dia
foco
int (1–5)
Nível de concentração
pausas
int (0–5)
Quantidade de pausas realizadas
horas_trabalhadas
int
Horas totais de trabalho no dia


🧠 Lógica de Cálculo

📊 Índice de Bem-Estar (0–5)

Calculado com base em:

•
humor

•
foco

•
pausas

•
Penalizações por carga excessiva

Quanto maior o valor → melhor o bem-estar.

🔥 Risco de Burnout (0–3)

Baseado em:

•
Excesso de horas trabalhadas

•
Baixos níveis de humor

•
Pausas insuficientes

Quanto maior o valor → maior o risco.

🧪 Como Testar no Postman

1.
Clique em New → Request.

2.
Escolha o método POST.

3.
Use a URL: https://projeto-bem-estar-api.onrender.com/analyze-checkin

4.
Vá em Body → Raw → JSON.

5.
Envie o corpo da requisição:

6.
Clique em Send.

