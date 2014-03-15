#Site do Dev in Cachu 2014

Para subir o ambiente local, crie um virtualenv e instale as dependências rodando:

    $ pip install -r requirements.txt

O site roda no [Tsuru](http://tsuru.io), então não há muito segredo em
utiliza-lo em produção, basta criar a aplicação e utilizar ``git push`` para
deploy.
