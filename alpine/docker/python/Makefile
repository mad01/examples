default: egg

.PHONY: default egg clean

egg:
	python setup.py bdist_egg

clean:
	@rm -rf build dist pikachu.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete
