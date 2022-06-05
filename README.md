# 🪞 MitMirror

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE) [![CI](https://github.com/Claayton/mitmirror-api/actions/workflows/main.yaml/badge.svg)](https://github.com/rochacbruno/dynaconf/actions/workflows/main.yml)![GitHub issues](https://img.shields.io/github/issues/claayton/mitmirror-api.svg) ![GitHub stars](https://img.shields.io/github/stars/claayton/mitmirror-api.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/claayton/mitmirror-api.svg) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)

<p align="left"><img src="docs/img/beeatmirror.jpg" alt="mitmirror logo" width="320" height="205"></p>

## 📋 Features

- API para rede social focada em desenvolvimento pessoal
- Desenvolvida em Python/FastApi
- Realizar CRUD de usuários
- Autenticação e Autorização utilizando JWT
- Hospedada em https://mitmirror.herokuapp.com

## 🚀 Quick start

### Com Docker:

Com docker tudo fica mais simples, é só rodar o comandoa seguir e a API ja deverá estar setada em https://0.0.0.0:8080

    docker-compose up --build

### Sem Docker:

O projeto foi desenvolvido em um sistema operacional `linux mint 20.03`, na versão `versão 3.10.2` do python, as instruções deverão funcionar em qualquer sistema baseado no ubuntu e em qualquer versão do python acima da 3.8, mas é recomendado que utilize um ambiente o mais semelhante possível para evitar conflitos (de preferência utilizar o docker, principalmente se for rodar no windows).

Eu utilizei `pyenv` para instalar o python, mas vocẽ pode utilizar o [site oficial](https://www.python.org/downloads/) se preferir.

### __Ambiente virtual__

É uma boa prática criar um ambiente virtual para isolar o projeto da sua maquina e evitar conflitos, utilize o comando a seguir para instalar o `virtualenv` caso ainda não tenha instalado:
```
 sudo pip3 install virtualenv
```
Agora configure seu `ambiente virtual` para evitar possiveis conflitos:
```
python3 -m venv venv 
```
*Em seguida você deverá `ativar` esse ambiente:*
```
source venv/bin/activate 
```
*Agora instale as `bibliotecas e pacotes` necessários para rodar o projeto:*
```
pip3 install -r requirements.txt
```
*Você vai precisar de um arquivo para alocar suas `variáveis de ambiente` e `segredos`, use o comando abaixo para criá-lo e exportar as variáveis:*
```
echo 'MARIADB_USER=testedb
MARIADB_PASSWORD=teste
MARIADB_ROOT_PASSWORD=teste' > .env &&
echo 'SECRET_KEY="teste"
CONNECTION_STRING = "mysql+pymysql://root:teste@testedb/mitmirror_database?charset=utf8mb4"' > .secrets.toml

```

*🎉 O projeto ja está configurado e pronto para ser testado em modo de desenvolvedor:*
```
python3 run.py
```

## ⚙️ Tests

Utilizar para esse projeto o pytest para fazer os testes necessários, para executar os testes utilize:

```
  # Rodar o testes da forma padrão + cobertura:
  pytest --cov

  # Rodar os testes + cobertura, mostrando os detalhes caso ocorra algum erro:
  pytest -v --cov

```

## 📋 Documentação

Acessar `/docs` ou `/redoc` para visualizar as documentações geradas automaticamente pelo FastApi.