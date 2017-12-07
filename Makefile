clean:
	rm -f dist/*.tar.gz
	rm -f dist/*.whl
	rm -rf build

build:
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

.PHONY: clean build upload
