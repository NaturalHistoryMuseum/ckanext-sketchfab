#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

import logging
import re

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit
from ckanext.sketchfab.logic.validators import is_valid_sketchfab_url

log = logging.getLogger(__name__)
ignore_empty = toolkit.get_validator('ignore_empty')
not_empty = toolkit.get_validator('not_empty')
is_positive_integer = toolkit.get_validator('is_positive_integer')


class SketchfabPlugin(SingletonPlugin):
    """
    Resource view for embedding sketchfab models.
    """

    implements(interfaces.IConfigurer, inherit=True)
    implements(interfaces.IResourceView, inherit=True)
    implements(interfaces.IPackageController, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'theme/templates')

    def info(self):
        return {
            'name': 'sketchfab',
            'title': 'Sketchfab model',
            'schema': {
                'model_url': [ignore_empty, str, is_valid_sketchfab_url],
                'width': [not_empty, is_positive_integer],
                'height': [not_empty, is_positive_integer],
            },
            'iframed': False,
            'icon': 'asterisk',
        }

    def can_view(self, data_dict):
        # Can be added to all resources, regardless of data type
        return True

    def view_template(self, context, data_dict):
        return 'sketchfab_view.html'

    def form_template(self, context, data_dict):
        return 'sketchfab_form.html'

    def setup_template_variables(self, context, data_dict):
        """
        Setup variables available to templates.
        """

        # Model URL can either be specified in the view,
        # or defaults to use the resource URL
        model_url = data_dict['resource_view'].get('model_url') or data_dict[
            'resource'
        ].get('url')

        # Replace embed if it exists - added in template anyway
        model_url = re.sub('/embed$', '', model_url)

        return {'defaults': {'width': 940, 'height': 600}, 'model_url': model_url}
