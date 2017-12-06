from setuptools import setup


setup(
    name='pelican_shiori',
    author='Siddhant Goel',
    author_email='siddhantgoel@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pelican :: Themes',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=['jinja2', 'webassets'],
    package_data={
        'pelican_shiori': [
            'templates/*.html',
            'static/css/**/*.scss',
        ]
    },
    packages=['pelican_shiori'],
    url='https://github.com/siddhantgoel/pelican-shiori',
    version='0.1.0',
)
