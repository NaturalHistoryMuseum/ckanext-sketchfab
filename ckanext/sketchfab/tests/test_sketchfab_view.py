# import ckan
# from ckan.tests.pylons_controller import PylonsTestCase

import pylons.config as config
import paste.fixture

import ckan.config.middleware as middleware
import ckan.model as model
import ckan.lib.helpers as h
import ckan.lib.create_test_data as create_test_data
import ckan.plugins as p
import ckan.tests as tests


# import ckan.plugins as p
# import nose
#
# from ckanext.twitter.lib import (parsers as twitter_parsers)
# from ckanext.twitter.tests.helpers import Configurer, DataFactory
#
# eq_ = nose.tools.eq_


class TestSketchfabView(tests.WsgiAppCase):
    @classmethod
    def setup_class(cls):
        cls.config_templates = config['ckan.legacy_templates']
        config['ckan.legacy_templates'] = 'false'
        wsgiapp = middleware.make_app(config['global_conf'], **config)
        cls.app = paste.fixture.TestApp(wsgiapp)

        p.load('sketchfab')

        create_test_data.CreateTestData.create()

        context = {'model': model,
                   'session': model.Session,
                   'user': model.User.get('testsysadmin').name}

        cls.package = model.Package.get('annakarenina')
        cls.resource_id = cls.package.resources[1].id
        cls.resource_view = {
            'resource_id': cls.resource_id,
            'view_type': u'sketchfab',
            'title': u'Image View',
            'description': u'A nice view',
            'width': 200,
            'height': 400,
            'model_url': 'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823'
        }
        p.toolkit.get_action('resource_view_create')(
            context, cls.resource_view)

    def test_model_url_is_shown(self):
        url = h.url_for(controller='package', action='resource_read',
                        id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view['model_url'] in result

    def test_title_description_iframe_shown(self):
        url = h.url_for(controller='package', action='resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view['title'] in result
        assert self.resource_view['description'] in result
        assert 'iframe' in result.body

    def test_iframe_attributes(self):
        url = h.url_for(controller='package', action='resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert 'width="%s"' % self.resource_view['width'] in result
        assert 'height="%s"' % self.resource_view['height'] in result

