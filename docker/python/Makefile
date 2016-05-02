default: egg

.PHONY: default egg clean

egg:
	python setup.py bdist_egg

clean:
	@rm -rf build dist magine_cli.egg-info
	@find . -type f -name '*.pyc' -delete

release-patch:
	./release.sh patch 

release-minor:
	./release.sh minor
	
release-major:
	./release.sh major
