from setuptools import setup


setup(
    name='pelican_shiori',
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
    install_requires=['jinja2', 'webassets'],
    packages=['pelican_shiori'],
    url='https://github.com/siddhantgoel/pelican-shiori',
    version='0.1.0',
    license='MIT',
    keywords='python pelican pelican-theme static-site'
)
