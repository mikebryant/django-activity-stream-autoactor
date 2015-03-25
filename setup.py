"""Setup file for django-activity-stream-autoactor."""
from setuptools import setup, find_packages

from actstream_autoactor.version import __VERSION__

setup(
    name='django-activity-stream-autoactor',
    version=__VERSION__,
    packages=find_packages(),
    author='Mike Bryant',
    author_email='mike@mikebryant.me.uk',
    description='Automatic provision of actors for django-activity-stream',
    long_description=open('README.rst').read(),
    url='https://github.com/mikebryant/django-activity-stream-autoactor/',
    install_requires=[
        'django',
        'django-autoconfig',
    ],
    tests_require=[
        'django-setuptest',
        'mock',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
