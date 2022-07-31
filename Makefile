PYTHON?=/usr/bin/python3
PIPENV?=/usr/bin/pipenv
YARN?=/usr/bin/yarn

install:
	$(PIPENV) install -r ./etc/requirements.txt
	$(YARN)

build:
	./node_modules/.bin/sass --load-path=node_modules static/css/style.scss static/css/style.css
	$(PYTHON) manage.py collectstatic

run:
	$(PYTHON) manage.py runserver 0.0.0.0:8000

update-deps:
	$(YARN) upgrade --latest
