build_dev:
	pipenv install -e .
build_dist:
	pipenv run python setup.py bdist_wheel
