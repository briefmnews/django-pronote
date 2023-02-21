install:
	pip install -r test_requirements.txt

coverage:
	pytest --cov=pronote tests

report:
	pytest --cov=pronote --cov-report=html tests