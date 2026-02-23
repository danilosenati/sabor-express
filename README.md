# 🍽️ Sabor Express

![Alura](https://img.shields.io/badge/Curso-Alura-blue?logo=data:image/png;base64,iVBORw0KGgo=)
![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python)
![Status](https://img.shields.io/badge/status-em%20estudo-green)

Sistema simples de gerenciamento de restaurantes desenvolvido em
**Python**, executado via terminal (CLI).\
O projeto permite cadastrar restaurantes, listar registros e alternar o
status de ativação.

📚 **Projeto desenvolvido durante o curso de Python oferecido pela
Alura**, com foco na consolidação de fundamentos da linguagem e boas
práticas de organização de código.

------------------------------------------------------------------------

## 📌 Objetivo do Projeto

Este projeto foi desenvolvido com fins de prática para reforçar
conceitos fundamentais de:

-   Estruturas de dados (listas e dicionários)
-   Funções em Python
-   Estruturas condicionais
-   Laços de repetição
-   Manipulação de entrada do usuário
-   Organização de código modular
-   Controle de fluxo de aplicação

------------------------------------------------------------------------

## ⚙️ Funcionalidades

O sistema oferece as seguintes opções no menu principal:

1.  **Cadastrar restaurante**
    -   Nome
    -   Categoria
    -   Status (ativo ou inativo)
2.  **Listar restaurantes**
    -   Exibe todos os restaurantes cadastrados
    -   Mostra nome, categoria e status (ativado/desativado)
3.  **Modificar estado do restaurante**
    -   Permite alternar entre ativo e desativado
4.  **Sair do sistema**

------------------------------------------------------------------------

## 🧱 Estrutura de Dados

Os restaurantes são armazenados em uma lista de dicionários:

``` python
restaurantes = [
    {"Nome": "Boa Muqueca", "Categoria": "Baiana", "status_ativo": True}
]
```

Cada restaurante possui:

-   `Nome`
-   `Categoria`
-   `status_ativo` (booleano)

------------------------------------------------------------------------

## 💻 Tecnologias Utilizadas

-   Python 3
-   Terminal (CLI)

------------------------------------------------------------------------

## 📚 Conceitos Trabalhados

-   Manipulação de listas
-   Dicionários
-   Estrutura `if/elif/else`
-   Tratamento de exceções (`try/except`)
-   Modularização com funções
-   Uso do `__name__ == "__main__"`

------------------------------------------------------------------------

## 🚀 Melhorias Futuras

Algumas melhorias que podem ser implementadas:

-   Validação real do tipo booleano no cadastro
-   Persistência de dados em arquivo (JSON ou banco de dados)
-   Interface gráfica
-   Refatoração orientada a objetos
-   Compatibilidade com Linux/Mac (uso de `clear` em vez de `cls`)

------------------------------------------------------------------------

## 👨‍💻 Autor

Danilo Barros\
Estudante de Sistemas de Informação.
