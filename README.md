📂 Organizador de Arquivos

Um organizador de arquivos desenvolvido em Python para automatizar a organização de arquivos em pastas, reduzindo a necessidade de realizar esse processo manualmente.

O projeto identifica os arquivos presentes em um diretório e os organiza de acordo com suas extensões, tornando a estrutura de pastas mais limpa e facilitando a localização dos arquivos.

🎯 Objetivo

O projeto foi desenvolvido com o objetivo de praticar Python, manipulação de arquivos e automação de tarefas, criando uma solução simples para um problema comum do dia a dia.

A ideia é transformar uma tarefa repetitiva em um processo automatizado.

⚙️ Como funciona

O programa realiza basicamente as seguintes etapas:

Define o diretório que será organizado.
Percorre os arquivos encontrados nesse diretório.
Identifica a extensão de cada arquivo.
Determina a categoria correspondente.
Verifica se a pasta da categoria existe.
Cria a pasta quando necessário.
Move o arquivo para a pasta correspondente.
Exemplo

Antes da execução:

Downloads/
├── documento.pdf
├── imagem.png
├── foto.jpg
├── musica.mp3
├── planilha.xlsx
└── arquivo.txt

Depois da execução:

Downloads/
├── Documentos/
│   ├── documento.pdf
│   ├── planilha.xlsx
│   └── arquivo.txt
│
├── Imagens/
│   ├── imagem.png
│   └── foto.jpg
│
└── Músicas/
    └── musica.mp3

🛠️ Tecnologias utilizadas
Python
OS
shutil

📚 Conceitos praticados

Durante o desenvolvimento do projeto foram utilizados conceitos importantes de programação, como:

Variáveis
Condicionais
Estruturas de repetição
Funções
Manipulação de strings
Listagem de diretórios
Manipulação de arquivos e pastas
Organização de código
Automação de tarefas

🚀 Como executar
1. Clone o repositório
git clone URL_DO_REPOSITORIO
2. Acesse a pasta do projeto
cd nome-do-projeto
3. Execute o programa
python organizador.py

Antes de executar, verifique o diretório configurado no programa para evitar mover arquivos de uma pasta incorreta.

💡 Possíveis melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

Interface gráfica para facilitar a utilização;
Configuração das categorias pelo usuário;
Suporte para mais tipos de arquivos;
Registro das movimentações realizadas;
Tratamento de arquivos duplicados;
Opção para desfazer uma organização;
Configuração do diretório através de argumentos no terminal;
Sistema de logs para registrar erros e operações realizadas.
📌 Status

Concluído — versão inicial

O projeto cumpre seu objetivo principal de automatizar a organização de arquivos por categorias e também serviu como prática de Python e manipulação do sistema de arquivos.

👨‍💻 Autor

Desenvolvido por Arthur Lima como parte da minha jornada de aprendizado em programação e desenvolvimento de projetos utilizando Python.
