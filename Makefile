server:
	flask run

init:
	flask db init

migrations:
	flask db migrate

upgrade:
	flask db upgrade