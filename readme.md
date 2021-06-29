# Antes de dar start no projeto

- [1] Criar um arquivo chamado ``__dev__.py`` ou ``__production__`` **dentro da pasta `./code/`**.
- [2] Depois disso criado rode ``docker-compose build``.
- [3] Quando o ***build terminar*** rode  ``docker-compose up --remove-orphans`` ou ``docker-compose up --remove-orphans -d``.
- [4] Para parar a execução use ``Ctrl+C`` e depois ``docker-compose down``.

# Executando Gravação de dados no banco

- Quando o passo dois estiver sendo executado, abra uma nova guia no terminal do **Pycharm** e execute "**dentro da pasta `./code`**" ``python manage.py makemigrations``.
- Quando terminar o comando acima execute ``python manage.py migrate``.
- Depois execute ``python manage.py runserver``

# Você tem um PORTAINER

- **Lembre-se de entrar no endereço ``http://localhost:9000`` para acessar o portainer, se não ele desliga
  automáticamente depois de 5min.**
    
- **Sua API vai estar rodando no endereço ``http://localhost:8000``. Para acessar as urls,
  verifique os arquivos ``./code/proj/urls.py``, ``./code/salesman/urls.py`` e ``./code/vehicle/urls.py``.**


## COM ISSO VOCÊ TERÁ UMA API DJANGO RODANDO EM SUA MÁQUINA COM O DOCKER SENDO O SERVIDOR DO DATABASE

###### Developer: Pedro Augusto Barbosa Aparecido, (+35) 99915-7614.
###### Email: pedro007augustobarbosa@gmail.com.
###### GitHub Profile: [GitHub] https://github.com/Pedro-Augusto-Barbosa-Aparecido?tab=repositories
