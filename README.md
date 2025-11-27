🎮 Space Escape – Demo Game (Python + Pygame)

Space Escape é um jogo 2D desenvolvido em Python utilizando a biblioteca Pygame, criado como atividade prática da disciplina Linguagem de Programação Aplicada (2025).
O objetivo do projeto é demonstrar lógica de programação aplicada ao desenvolvimento de jogos, incluindo eventos, colisões, movimentação e criação de um executável para Windows.

🕹️ Sobre o Jogo

No Space Escape, o jogador controla uma nave espacial que deve desviar de meteoros que caem do topo da tela.
O jogo apresenta:

Controle simples (setas esquerda/direita)

Menu inicial com instruções

Inimigos gerados aleatoriamente

Sistema de colisão

Loop de jogo fluido (60 FPS)

Possibilidade de adicionar sons e novos assets

É uma demo simples, porém totalmente jogável.

📸 Screenshot (opcional)

Se quiser adicionar:

![Screenshot do jogo](./assets/screenshot.png)

✨ Funcionalidades

🚀 Nave controlada pelo jogador

☄️ Meteoros caindo de forma randômica

🖥️ Tela de menu com comandos

🎧 Suporte a áudio (opcional)

🔄 Reinício automático ao colidir

🧩 Uso completo de loops, eventos, colisões e renderização


🛠 Tecnologias Utilizadas

Python 3

Pygame

PyInstaller (para geração do .exe)

Assets de imagens e sons adquiridos online (domínio público)

📁 Estrutura do Projeto
/
├── main.py
├── assets/
│   ├── player.png
│   ├── enemy.png
│   ├── background.png
│   └── menu.png
└── README.md

▶️ Como Executar o Projeto

1️⃣ Instale o Pygame
pip install pygame

2️⃣ Execute o jogo
python main.py

💻 Como Gerar o Executável (.exe)

1️⃣ Instale o PyInstaller
pip install pyinstaller

2️⃣ Gere o executável
pyinstaller --onefile --windowed main.py

3️⃣ Vá até a pasta dist/
dist/
   main.exe

4️⃣ Copie a pasta assets/ para dentro de dist/

🎮 Controles
Tecla	Ação
←	mover para esquerda
→	mover para direita
ENTER	iniciar o jogo

🎯 Objetivo Acadêmico

Este projeto atende aos requisitos da atividade prática:

✔ Jogo 2D

✔ Bibliotecas adequadas (Pygame)

✔ Menu inicial com instruções

✔ Jogável e funcional

✔ Build para Windows

✔ Código original

🤝 Contribuições

Contribuições são bem-vindas!
Sugestões de melhoria, novos obstáculos, sons ou animações podem ser enviados via pull request.

📄 Licença

Este projeto é de uso acadêmico e livre para estudo.