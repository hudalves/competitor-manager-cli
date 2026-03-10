# Competitor Manager CLI

Sistema desenvolvido em Python para gerenciamento de competidores de artes marciais através do terminal.

O projeto permite cadastrar, visualizar, pesquisar, atualizar e remover competidores de diferentes modalidades de luta.

## Funcionalidades

* Cadastro de competidores
* Remoção de competidores
* Atualização de dados
* Pesquisa por nome
* Listagem completa dos competidores
* Organização em tabela no terminal

## Modalidades suportadas

* Boxe
* Muay Thai
* Jiu Jitsu
* Judô
* MMA

## Informações armazenadas

Cada competidor possui os seguintes dados:

* Modalidade
* Gênero
* RG
* CPF
* Nome
* Idade
* Categoria de peso

## Tecnologias utilizadas

* Python
* Questionary (menus interativos no terminal)
* Tabulate (exibição de tabelas)
* Colorama (cores no terminal)

## Armazenamento de dados

Os dados são armazenados em um arquivo de texto (`dados.txt`) utilizando estrutura simples separada por vírgulas.

## Objetivo do projeto

Este projeto foi desenvolvido no primeiro semestre da graduação com o objetivo de praticar:

* lógica de programação
* manipulação de arquivos
* construção de menus interativos no terminal
* validação de dados de entrada

## Como executar

Clone o repositório:

git clone https://github.com/hudalves/projeto_python

Instale as dependências:

pip install questionary tabulate colorama

Execute o programa:

python main.py

## Possíveis melhorias futuras

* utilização de banco de dados (SQLite ou PostgreSQL)
* criação de API para gerenciamento dos dados
* criação de interface gráfica
* autenticação de usuários
* exportação de dados em CSV ou JSON
