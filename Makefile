GH_PAGES_BRANCH=gh-pages
INPUT=$(CURDIR)/content
OUTPUT=$(CURDIR)/output
PELICAN?=pelican

clean:
	rm -f dist/*.tar.gz
	rm -f dist/*.whl
	rm -rf build

build:
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

publish:
	$(PELICAN) $(INPUT) -o $(OUTPUT) -s publishconf.py

github: publish
	ghp-import -m "Generate Pelican site" -b $(GH_PAGES_BRANCH) $(OUTPUT)
	git push origin $(GH_PAGES_BRANCH)

.PHONY: clean build upload publish github
