from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-sketchfab',
    version=version,
    description="",
    long_description="",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.sketchfab'],
    include_package_data=True,
    zip_safe=False,
    author='Ben Scott',
    author_email='ben@benscott.co.uk',
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points= \
        """
            [ckan.plugins]
                sketchfab = ckanext.sketchfab.plugin:SketchfabPlugin
        """,
)
