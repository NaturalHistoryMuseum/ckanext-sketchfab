# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK
import pytest
from ckan.lib.helpers import url_for
from ckan.tests import factories


@pytest.mark.filterwarnings(u'ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config(u'ckan.plugins', u'sketchfab')
@pytest.mark.usefixtures(u'clean_db', u'with_plugins', u'with_request_context')
class TestSketchfabView(object):

    @pytest.fixture
    def package(self):
        return factories.Dataset()

    @pytest.fixture
    def resource(self, package):
        return factories.Resource(package_id=package[u'id'])

    @pytest.fixture
    def resource_view(self, resource):
        resource_view = factories.ResourceView(
            resource_id=resource[u'id'],
            view_type=u'sketchfab',
            title=u'Image View',
            description=u'A nice view',
            width=200,
            height=400,
            model_url=u'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823'
        )
        return resource_view

    def test_model_url_is_shown(self, package, resource, resource_view, app):
        url = url_for(u'resource.read', id=package[u'name'], resource_id=resource[u'id'])
        result = app.get(url)
        assert resource_view[u'model_url'] in result

    def test_title_description_iframe_shown(self, package, resource, resource_view, app):
        url = url_for(u'resource.read', id=package[u'name'], resource_id=resource[u'id'])
        result = app.get(url)
        assert resource_view[u'title'] in result
        assert resource_view[u'description'] in result
        assert u'iframe' in result

    def test_iframe_attributes(self, package, resource, resource_view, app):
        url = url_for(u'resource.read', id=package[u'name'], resource_id=resource[u'id'])
        result = app.get(url)
        assert u'width="%s"' % resource_view[u'width'] in result
        assert u'height="%s"' % resource_view[u'height'] in result
