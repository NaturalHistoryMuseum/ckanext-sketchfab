# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

import ckantest.helpers.routes
from ckantest.models import TestBase

from ckan.tests import factories


class TestSketchfabView(TestBase):
    plugins = [u'sketchfab']

    @classmethod
    def setup_class(cls):
        super(TestSketchfabView, cls).setup_class()
        cls.package = cls.data_factory().package()
        cls.resource = factories.Resource(package_id=cls.package[u'id'])
        cls.resource_view = factories.ResourceView(
            resource_id=cls.resource[u'id'],
            view_type=u'sketchfab',
            title=u'Image View',
            description=u'A nice view',
            width=200,
            height=400,
            model_url=u'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823')

    def test_model_url_is_shown(self):
        url = ckantest.helpers.routes.resource_read(self.package, self.resource)
        result = self.app.get(url)
        assert self.resource_view[u'model_url'] in result

    def test_title_description_iframe_shown(self):
        url = ckantest.helpers.routes.resource_read(self.package, self.resource)
        result = self.app.get(url)
        assert self.resource_view[u'title'] in result
        assert self.resource_view[u'description'] in result
        assert u'iframe' in result.unicode_body

    def test_iframe_attributes(self):
        url = ckantest.helpers.routes.resource_read(self.package, self.resource)
        result = self.app.get(url)
        assert u'width="%s"' % self.resource_view[u'width'] in result
        assert u'height="%s"' % self.resource_view[u'height'] in result
