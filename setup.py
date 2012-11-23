"""
pycri-urltitle
-------------

Plugin for resolving <title>-elements from URLs.
"""
from setuptools import setup


setup(
    name='pycri-urltitle',
    version='0.1.0',
    url='https://github.com/xintron/pycri-urltitle',
    license='BSD',
    author='Marcus Carlsson',
    author_email='carlsson.marcus@gmail.com',
    description='Title-resolver for URLs',
    long_description=__doc__,
    packages=['pycri_urltitle'],
    provides='pycri_urltitle',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'pycri',
        'lxml'
    ],
    classifiers=[
        'Environment :: Console',
        'Framework :: pycri',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
