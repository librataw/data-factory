init:
	# create venv
	python3 -m venv env; \
	# source env
	. env/bin/activate; \
	pip3 install -r requirements.txt; \

test:
	. env/bin/activate; \
	# run unit test
	python3 -m unittest discover tests; \

docs:
	# create html documentation using sphinx
	cd docs && make html && cd ..; \

install:
	# create venv
	python3 -m venv env; \
	# source env
	. env/bin/activate; \
	# install all necessary packages
	pip3 install -r requirements.txt; \

erd:
	java -jar bin/schemaSpy_5.0.0.jar -t pgsql -db places -host localhost -s public -u etl_user -p password -o erd -dp bin/postgresql-42.2.2.jar

.PHONY: init test docs install erd
