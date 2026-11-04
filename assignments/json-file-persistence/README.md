# 📘 Atividade: Persistência de Dados com JSON

## 🎯 Objetivo

Pratique a leitura e a gravação de dados em arquivos JSON com Python. Você vai criar um pequeno gerenciador de tarefas cujos dados continuam disponíveis depois que o programa é encerrado.

## 📝 Tarefas

### 🛠️ Representar as Tarefas como Dados

#### Descrição
Crie uma lista de tarefas em que cada tarefa seja representada por um dicionário. Cada tarefa deve ter um título e indicar se já foi concluída.

#### Requisitos
O programa concluído deve:

- Representar cada tarefa com os campos `title` e `completed`.
- Usar uma lista para armazenar várias tarefas.
- Criar pelo menos duas tarefas de exemplo e exibi-las.


### 🛠️ Carregar Tarefas de um Arquivo JSON

#### Descrição
Salve a lista em um arquivo chamado `tasks.json` e carregue os dados desse arquivo quando o programa iniciar. Se o arquivo ainda não existir, comece com uma lista vazia.

#### Requisitos
O programa concluído deve:

- Usar o módulo `json` para ler e escrever dados.
- Criar `tasks.json` ao salvar a lista pela primeira vez.
- Tratar a ausência do arquivo sem encerrar o programa com erro.


### 🛠️ Manter as Alterações entre Execuções

#### Descrição
Permita adicionar tarefas e marcar uma tarefa como concluída. Depois de cada alteração, salve a lista no arquivo para que ela possa ser recuperada na próxima execução.

#### Requisitos
O programa concluído deve:

- Permitir adicionar uma tarefa com `completed` inicialmente igual a `False`.
- Permitir marcar uma tarefa existente como concluída.
- Salvar as alterações em `tasks.json` e carregá-las corretamente ao iniciar o programa novamente.