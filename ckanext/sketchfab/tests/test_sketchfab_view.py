# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

from ckan import plugins
from ckan.plugins import toolkit
from ckan.tests import factories, helpers


class TestSketchfabView(helpers.FunctionalTestBase):
    ''' '''

    @classmethod
    def _apply_config_changes(cls, cfg):
        # for testing views the plugin has to be loaded like this
        cfg['ckan.plugins'] = u'sketchfab'

    @classmethod
    def setup_class(cls):
        ''' '''
        super(TestSketchfabView, cls).setup_class()
        cls.app = helpers._get_test_app()
        helpers.reset_db()
        if not plugins.plugin_loaded(u'sketchfab'):
            plugins.load(u'sketchfab')

    @classmethod
    def teardown_class(cls):
        ''''''
        if plugins.plugin_loaded(u'sketchfab'):
            plugins.unload(u'sketchfab')

    def setup(self):
        self.user = factories.Sysadmin()
        self.package = factories.Dataset(user=self.user)
        self.resource = factories.Resource(user=self.user, package_id=self.package[u'id'])
        self.resource_view = factories.ResourceView(
            resource_id=self.resource[u'id'],
            view_type=u'sketchfab',
            title=u'Image View',
            description=u'A nice view',
            width=200,
            height=400,
            model_url=u'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823')

    def teardown(self):
        helpers.reset_db()

    def test_model_url_is_shown(self):
        ''' '''
        url = toolkit.url_for('resource.read',
                              id=self.package['name'], resource_id=self.resource['id'])
        result = self.app.get(url)
        assert self.resource_view[u'model_url'] in result

    def test_title_description_iframe_shown(self):
        ''' '''
        url = toolkit.url_for('resource.read',
                              id=self.package['name'], resource_id=self.resource['id'])
        result = self.app.get(url)
        assert self.resource_view[u'title'] in result
        assert self.resource_view[u'description'] in result
        assert u'iframe' in result.unicode_body

    def test_iframe_attributes(self):
        ''' '''
        url = toolkit.url_for('resource.read',
                              id=self.package['name'], resource_id=self.resource['id'])
        result = self.app.get(url)
        assert u'width="%s"' % self.resource_view[u'width'] in result
        assert u'height="%s"' % self.resource_view[u'height'] in result
