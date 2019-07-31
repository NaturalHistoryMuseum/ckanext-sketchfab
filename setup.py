#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

from setuptools import setup, find_packages

version = u'0.1'

setup(
    name=u'ckanext-sketchfab',
    version=version,
    description=u'',
    long_description=u'',
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords=u'',
    license=u'',
    packages=find_packages(exclude=[u'ez_setup', u'examples', u'tests']),
    namespace_packages=[u'ckanext', u'ckanext.sketchfab'],
    include_package_data=True,
    zip_safe=False,
    author=u'Ben Scott',
    author_email=u'ben@benscott.co.uk',
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points= \
        u'''
            [ckan.plugins]
                sketchfab = ckanext.sketchfab.plugin:SketchfabPlugin
        ''',
)