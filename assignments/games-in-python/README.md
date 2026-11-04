
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa um jogo da Forca em Python para praticar manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória.

## 📝 Tarefas

### 🛠️ Construir um Jogo da Forca

#### Descrição
Crie um jogo em que o jogador tenta adivinhar uma palavra oculta, informando uma letra por vez. O jogo deve atualizar o progresso a cada palpite e terminar quando a palavra for descoberta ou as tentativas incorretas acabarem.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Mostrar as letras descobertas e ocultar as demais, por exemplo, `_ _ _`.
- Aceitar palpites de letras e atualizar o progresso da palavra.
- Rastrear e exibir as tentativas incorretas restantes.
- Encerrar quando o jogador adivinhar a palavra ou esgotar as tentativas.
- Exibir uma mensagem indicando vitória ou derrota.

Exemplo de interação:

```text
Palavra: _ _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: a
Palavra: _ a _ a _ a
Tentativas restantes: 6
Digite uma letra: x
Palavra: _ a _ a _ a
Tentativas restantes: 5
...
Parabéns! Você descobriu a palavra: banana 🎉
```