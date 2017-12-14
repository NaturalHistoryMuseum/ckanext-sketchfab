import paste.fixture
import pylons.config as config
import urlparse

import ckan.model as model
import ckan.tests as tests
import ckan.plugins as plugins
import ckan.lib.helpers as h
import ckanext.pdfview.plugin as plugin
import ckan.lib.create_test_data as create_test_data
import ckan.config.middleware as middleware

from ckan.tests.pylons_controller import PylonsTestCase


class TestSketchfabView(PylonsTestCase):
    def test_gets_dataset_author(self):
        pass

# class TestView(tests.WsgiAppCase):
    @classmethod
    def setup_class(cls):
        cls.config_templates = config['ckan.legacy_templates']
        config['ckan.legacy_templates'] = 'false'
        wsgiapp = middleware.make_app(config['global_conf'], **config)
        cls.app = paste.fixture.TestApp(wsgiapp)

        plugins.load('sketchfab_view')

        create_test_data.CreateTestData.create()

        context = {'model': model,
                   'session': model.Session,
                   'user': model.User.get('testsysadmin').name}
        #
        cls.package = model.Package.get('annakarenina')
        cls.resource_id = cls.package.resources[1].id
        cls.resource_view = {
            'resource_id': cls.resource_id,
            'view_type': 'sketchfab',
            'title': u'Test View',
            'description': u'A nice test view',
            'height': 400,
            'width': 400,
            'model_url': 'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823'
        }
        cls.resource_view = plugins.toolkit.get_action('resource_view_create')(context, cls.resource_view)
#
#     @classmethod
#     def teardown_class(cls):
#         config['ckan.legacy_templates'] = cls.config_templates
#         model.repo.rebuild_db()
#
#     def test_sketchfab_is_shown(self):
#         url = h.url_for(controller='package', action='resource_read', id=self.package.name, resource_id=self.resource_id)
#         result = self.app.get(url)
#         assert self.resource_view['model_url'] in result
#         #

