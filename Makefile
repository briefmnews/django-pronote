install:
	pip install -r test_requirements.txt

coverage:
	pytest --cov=pronote tests

report:
	pytest --cov=pronote --cov-report=html tests

release:
	git tag -a $(shell python -c "from pronote import __version__; print(__version__)") -m "$(m)"
	git push origin --tags