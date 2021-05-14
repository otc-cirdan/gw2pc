node_modules/.bin/sass --load-path=node_modules static/css/style.scss static/css/style.css
zappa update prod
zappa manage prod "collectstatic --noinput"
