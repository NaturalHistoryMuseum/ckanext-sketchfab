
#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

import pylons.config as config
import paste.fixture

import ckan.config.middleware as middleware
import ckan.model as model
import ckan.lib.helpers as h
import ckan.lib.create_test_data as create_test_data
import ckan.plugins as p
import ckan.tests as tests




class TestSketchfabView(tests.WsgiAppCase):
    ''' '''
    @classmethod
    def setup_class(cls):
        ''' '''
        cls.config_templates = config[u'ckan.legacy_templates']
        config[u'ckan.legacy_templates'] = u'false'
        wsgiapp = middleware.make_app(config[u'global_conf'], **config)
        cls.app = paste.fixture.TestApp(wsgiapp)

        p.load(u'sketchfab')

        create_test_data.CreateTestData.create()

        context = {u'model': model,
                   u'session': model.Session,
                   u'user': model.User.get(u'testsysadmin').name}

        cls.package = model.Package.get(u'annakarenina')
        cls.resource_id = cls.package.resources[1].id
        cls.resource_view = {
            u'resource_id': cls.resource_id,
            u'view_type': u'sketchfab',
            u'title': u'Image View',
            u'description': u'A nice view',
            u'width': 200,
            u'height': 400,
            u'model_url': u'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823'
        }
        p.toolkit.get_action(u'resource_view_create')(
            context, cls.resource_view)

    def test_model_url_is_shown(self):
        ''' '''
        url = h.url_for(controller=u'package', action=u'resource_read',
                        id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view[u'model_url'] in result

    def test_title_description_iframe_shown(self):
        ''' '''
        url = h.url_for(controller=u'package', action=u'resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view[u'title'] in result
        assert self.resource_view[u'description'] in result
        assert u'iframe' in result.body

    def test_iframe_attributes(self):
        ''' '''
        url = h.url_for(controller=u'package', action=u'resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert u'width="%s"' % self.resource_view[u'width'] in result
        assert u'height="%s"' % self.resource_view[u'height'] in result

