import logging
import ckan.plugins as p
import re
from ckanext.sketchfab.logic.validators import is_valid_sketchfab_url

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')
not_empty = p.toolkit.get_validator('not_empty')
is_positive_integer = p.toolkit.get_validator('is_positive_integer')


class SketchfabPlugin(p.SingletonPlugin):
    """
    Resource view for embedding sketchfab models
    """

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IPackageController, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')

    def info(self):
        return {'name': 'sketchfab',
                'title': 'Sketchfab model',
                'schema': {
                    'model_url': [ignore_empty, unicode, is_valid_sketchfab_url],
                    'width': [not_empty, is_positive_integer],
                    'height': [not_empty, is_positive_integer],
                },
                'iframed': False,
                'icon': 'asterisk'}

    def can_view(self, data_dict):
        # Can be added to all resources, regardless of data type
        return True

    def view_template(self, context, data_dict):
        return 'sketchfab_view.html'

    def form_template(self, context, data_dict):
        return 'sketchfab_form.html'

    def setup_template_variables(self, context, data_dict):
        """Setup variables available to templates"""

        # Model URL can either be specified in the view,
        # or defaults to use the resource URL
        model_url = data_dict['resource_view'].get('model_url') or data_dict['resource'].get('url')

        # Replace embed if it exists - added in template anyway
        model_url = re.sub('/embed$', '', model_url)

        return {
            'defaults': {
                'width': 940,
                'height': 600
            },

            'model_url': model_url
        }
