install:
	pipenv install -r ./etc/requirements.txt
	yarn

build:
	./node_modules/.bin/sass --load-path=node_modules static/css/style.scss static/css/style.css
	python3 manage.py collectstatic

run:
	python3 manage.py runserver 0.0.0.0:8000

update-deps:
	yarn upgrade --latest
