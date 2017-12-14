ckanext-sketchfab
=============
CKAN extension for embedding Sketchfab URLs as views.

A Sketchfab resource can be added to either:

a) A resource with a Sketchfab URL
b) Any resource. In which case Sketchfab URL is specified when view os created. 

This allows us to add a Sketchfab model view on top of the raw 3D Data. 

Tests
-----
nosetests --ckan --with-pylons=/etc/ckan/default/development.ini ckanext/sketchfab/tests/