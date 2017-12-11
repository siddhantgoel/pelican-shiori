GH_PAGES_BRANCH=gh-pages
INPUT=$(CURDIR)/content
OUTPUTDIR=$(CURDIR)/output

clean:
	rm -f dist/*.tar.gz
	rm -f dist/*.whl
	rm -rf build

build:
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

generate:
	$(PELICAN) $(INPUT) -o $(OUTPUT) -s publishconf.py content

.PHONY: clean build upload
