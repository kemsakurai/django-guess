import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-guess',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'guess': ['templates/includes/*.html'],
    },
    license='MIT License',
    description='A simple Django package to enabling data-driven user-experiences on the web',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/kemsakurai/django-guess',
    author='Ken Sakurai',
    author_email='sakurai.kem@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'pandas>=0.23.4',
        'Google2Pandas>=0.1.1',
        'numpy>=1.13.3',
    ]
)
