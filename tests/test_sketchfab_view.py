# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK
import pytest
from ckan.lib.helpers import url_for
from ckan.tests import factories


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config('ckan.plugins', 'sketchfab')
@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
class TestSketchfabView(object):
    @pytest.fixture
    def package(self):
        return factories.Dataset()

    @pytest.fixture
    def resource(self, package):
        return factories.Resource(package_id=package['id'])

    @pytest.fixture
    def resource_view(self, resource):
        resource_view = factories.ResourceView(
            resource_id=resource['id'],
            view_type='sketchfab',
            title='Image View',
            description='A nice view',
            width=200,
            height=400,
            model_url='https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823',
        )
        return resource_view

    def test_model_url_is_shown(self, package, resource, resource_view, app):
        url = url_for('resource.read', id=package['name'], resource_id=resource['id'])
        result = app.get(url)
        assert resource_view['model_url'] in result

    def test_title_description_iframe_shown(
        self, package, resource, resource_view, app
    ):
        url = url_for('resource.read', id=package['name'], resource_id=resource['id'])
        result = app.get(url)
        assert resource_view['title'] in result
        assert resource_view['description'] in result
        assert 'iframe' in result

    def test_iframe_attributes(self, package, resource, resource_view, app):
        url = url_for('resource.read', id=package['name'], resource_id=resource['id'])
        result = app.get(url)
        assert 'width="%s"' % resource_view['width'] in result
        assert 'height="%s"' % resource_view['height'] in result
