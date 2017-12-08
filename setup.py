import io
import os.path
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='pelican_shiori',
    description='Shiori theme for Pelican',
    long_description=long_description,
    author='Siddhant Goel',
    author_email='siddhantgoel@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pelican :: Themes',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    install_requires=['cssmin', 'jinja2', 'webassets'],
    packages=['pelican_shiori'],
    url='https://github.com/siddhantgoel/pelican-shiori',
    version='0.2.0',
    license='MIT',
    keywords='python pelican pelican-theme static-site'
)
