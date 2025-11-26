
# 📘 Cadastro de Clientes – Sistema XYZ

Um sistema simples de cadastro, consulta, edição e exclusão de clientes, desenvolvido em Python usando Tkinter, CustomTkinter, SQLite e CTkTreeview.
O objetivo é permitir que o comércio "XYZ Comércio" organize melhor os dados dos clientes e encontre informações rapidamente por meio de uma interface gráfica intuitiva.

## 🔌 Como executar na sua máquina
### 1. Instale o Python

Baixe e instale o Python pelo site:
https://www.python.org/downloads/

### 2. Instale as bibliotecas necessárias

No terminal/cmd execute:
```bash
  pip install customtkinter
  pip install https://github.com/JohnDevlopment/CTkTreeview/archive/refs/heads/main.zip
  pip install icecream
```

Obs: Tkinter já vem instalado com o Python.

### 3. Execute o arquivo

Abra o terminal na pasta do projeto e rode:
```bash
python nome_do_seu_arquivo.py
```

O sistema criará automaticamente o banco banco.db e exibirá a interface gráfica.
## 📋 Pré-requisitos do sistema



- Python instalado (3.8+ recomendado)

- Sistema operacional: Windows, Linux ou macOS

- Permissão de escrita na pasta para gerar o banco SQLite

- Arquivo de ícone icone.ico e imagem de sua logo na mesma pasta do arquivo de cadastro

## 🛠️ Tecnologias utilizadas
**💻 Linguagens**

- Python

**📚 Bibliotecas**

- Tkinter (interface gráfica padrão)

- CustomTkinter (interface moderna e estilizada)

- SQLite3 (banco de dados local)

- CTkTreeview (tabela moderna)

**🧰 Editor de código sugerido**

- VS Code

- PyCharm

- Sublime Text

- IDLE (vem com Python)

## 🧱 Arquitetura e funcionalidades
- **✔ Cadastro de novos clientes**

    Campos: Nome, E-mail, Telefone, Endereço

- **✔ Atualização de clientes**

    Permite modificar todos os dados selecionando um registro no Treeview.

- **✔ Exclusão de clientes**

    Remove o registro da base de dados.

- **✔ Exibição dos cadastros**

    Tabela totalmente estilizada com CustomTkinter + CTkTreeview.
    Tema dark.

-  **✔ Banco de dados local**

    O arquivo banco.db é criado automaticamente.


## 🧪 Versão recomendada

- **Python 3.10+**
## Autores

- [@matheusfs16](https://www.github.com/matheusfs16)

