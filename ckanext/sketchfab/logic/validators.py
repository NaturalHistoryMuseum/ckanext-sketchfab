#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-sketchfab
# Created by the Natural History Museum in London, UK

import re
from ckan.common import _
import ckan.lib.navl.dictization_functions as df

Invalid = df.Invalid
Missing = df.Missing


def is_valid_sketchfab_url(value, context):
    '''Validate Sketchfab URL

    :param value:
    :param context:
    :returns:

    '''

    pattern = u'http[s]?:\/\/[w+3.]?sketchfab.com\/models\/[0-9a-z]+'
    if re.search(pattern, value, re.IGNORECASE):
        return value

    raise Invalid(_(u'Not a valid Sketchfab model URL'))
