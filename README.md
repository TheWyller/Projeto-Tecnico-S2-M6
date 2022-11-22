# Projeto-Tecnico-S2-M6 - Documentação

Projeto realizado em Django REST framework com Postgres com o intuito de receber um 
arquivo no formato CNAB com diversas transações bancarias e a partir dele adiciona-lo em um banco de dados

## Como Rodar a Aplicação:

Criar um arquivo .env e adicionar informações seguindo o padrão do .env.example

### Rodar aplicação SEM o docker

Descomentar as linhas 96 e 97 do arquivo settings.py
```shell
        # "HOST": "127.0.0.1",
        # "PORT": 5432,
```
        
Comentar as linhas 100 e 101 do arquivo settings.py
```shell
        "HOST": "db",
        "PORT": 5432,
```

*arquivo settings.py se encontra na pasta "_project"

#### Para Iniciar a instalação das dependências e ambientes deve-se:

rodar o seguinte comando:
```shell
        python -m venv venv
```
Para entrar no ambiente virtual basta ultilizar o seguinte comando:
```shell
        .\venv\Scripts\activate (windowns) 
        ou
        source venv/bin/activate (linux)
```
instalar todas as dependências com o seguinte comando:
```shell
        pip install -r requirements.txt
```
Lembre-se de criar o banco de dados no Postgress com os mesmos dados fornecidos no .env

Após criar o banco de dados, rodar os seguintes comandos:
```shell
        python manage.py migrate
```
```shell
        python manage.py create_superuser
```
```shell
        python manage.py create_transactions
```

Para fazer a aplicação inicializar deve-se rodar o servidor com o seguinte comando:
```shell 
        python manage.py runserver
```

---

### Rodar aplicação COM o docker
Comentar as linhas 96 e 97 do arquivo settings.py
```shell
        "HOST": "127.0.0.1",
        "PORT": 5432,
```
        
Descomentar as linhas 100 e 101 do arquivo settings.py
```shell
       # "HOST": "db",
       # "PORT": 5432,
```
  *Levando em consideração que o usuario possuí o docker devidamente instalado.
  
Deve-se rodar o seguinte comando:
```shell
      docker-compose up
```
  
  Ao finalizar os testes da aplicações recomenda-se rodar o seguinte comando:

```shell
      docker-compose down
```

---

## Ao Abrir o LocalHost
  ### A pagina Home possuí um botão para incluir um arquivo.
  
- O Arquivo DEVE estar **nomeado** como **"CNAB"** em formato **.txt**
- O conteúdo deve possuir o formato a seguir:
    3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO
- Cada transação deve estar em uma linha
---   
### Para visualizar todos as informações formatadas deve-se acessar o seguinte link:
```shell
  localhost:8000/api/interpreter/
```
# Testes:

## Testes Unitários e de integração em desenvolvimento

  

  
  


