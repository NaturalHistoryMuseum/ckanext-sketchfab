#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

import logging
import ckan.plugins as p
import re
from ckanext.sketchfab.logic.validators import is_valid_sketchfab_url

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator(u'ignore_empty')
not_empty = p.toolkit.get_validator(u'not_empty')
is_positive_integer = p.toolkit.get_validator(u'is_positive_integer')


class SketchfabPlugin(p.SingletonPlugin):
    '''Resource view for embedding sketchfab models'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IPackageController, inherit=True)

    def update_config(self, config):
        '''

        :param config: 

        '''
        p.toolkit.add_template_directory(config, u'theme/templates')

    def info(self):
        ''' '''
        return {u'name': u'sketchfab',
                u'title': u'Sketchfab model',
                u'schema': {
                    u'model_url': [ignore_empty, unicode, is_valid_sketchfab_url],
                    u'width': [not_empty, is_positive_integer],
                    u'height': [not_empty, is_positive_integer],
                },
                u'iframed': False,
                u'icon': u'asterisk'}

    def can_view(self, data_dict):
        '''

        :param data_dict: 

        '''
        # Can be added to all resources, regardless of data type
        return True

    def view_template(self, context, data_dict):
        '''

        :param context: 
        :param data_dict: 

        '''
        return u'sketchfab_view.html'

    def form_template(self, context, data_dict):
        '''

        :param context: 
        :param data_dict: 

        '''
        return u'sketchfab_form.html'

    def setup_template_variables(self, context, data_dict):
        '''Setup variables available to templates

        :param context: 
        :param data_dict: 

        '''

        # Model URL can either be specified in the view,
        # or defaults to use the resource URL
        model_url = data_dict[u'resource_view'].get(u'model_url') or data_dict[u'resource'].get(u'url')

        # Replace embed if it exists - added in template anyway
        model_url = re.sub('/embed$', u'', model_url)

        return {
            u'defaults': {
                u'width': 940,
                u'height': 600
            },

            u'model_url': model_url
        }
