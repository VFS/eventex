Eventex
=======

Sistema de Eventos para o curso WTTD.

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:vfs/eventex.git eventex
cd eventex
python -m venv .eventexenv
source .eventexenv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy?
1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=MINHA_SECRET_KEY
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```