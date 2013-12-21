#!/usr/bin/env python
import re
import os
import ConfigParser
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version, _ = info.get('version', '0.0.1').split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = []
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append(
            'trytond_%s >= %s.%s, < %s.%s' % (
                dep, major_version, minor_version,
                major_version, minor_version + 1
            )
        )
requires.append(
    'trytond >= %s.%s, < %s.%s' %
    (major_version, minor_version, major_version, minor_version + 1)
)

setup(
    name='trytond_hr',
    version=info.get('version'),
    description="Tryton HR Management module boilerplate",
    author="Prakash Pandey",
    author_email='prakashpp.pandey@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Tryton',
        'Topic :: Office/Business',
    ],
    packages=[
        'trytond.modules.hr',
        'trytond.modules.hr.tests',
    ],
    package_dir={
        'trytond.modules.hr': '.',
        'trytond.modules.hr.tests': 'tests',
    },
    package_data={
        'trytond.modules.hr': info.get('xml', [])
                + ['tryton.cfg', 'locale/*.po', 'tests/*.rst', '*.odt']
                + ['i18n/*.pot', 'i18n/pt_BR/LC_MESSAGES/*', 'view/*.xml'],
    },
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    hr = trytond.modules.hr
    """,
    test_suite='tests.suite',
    test_loader='trytond.test_loader:Loader',
)
