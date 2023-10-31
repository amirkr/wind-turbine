test:
	docker exec -ti wind-turbine pytest -vv /wind-turbine/tests/

run:
	docker-compose up --build -d

stop:
	docker-compose down

install:
	pyenv install -s 3.10.6
	$(shell pyenv prefix 3.10.6)/bin/python -m virtualenv env
	./env/bin/pip install -r requirements/requirements.txt
