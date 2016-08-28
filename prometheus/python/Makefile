default: wheel

.PHONY: default wheel clean

wheel:
	python3 setup.py sdist bdist_wheel

clean:
	@rm -rf build dist *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete
