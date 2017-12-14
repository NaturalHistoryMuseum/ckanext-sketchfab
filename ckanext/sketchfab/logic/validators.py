#!/usr/bin/env python
# encoding: utf-8
"""
Created by 'bens3' on 2013-06-21.
Copyright (c) 2013 'bens3'. All rights reserved.
"""
import re
from ckan.common import _
import ckan.lib.navl.dictization_functions as df

Invalid = df.Invalid
Missing = df.Missing


def is_valid_sketchfab_url(value, context):
    '''
    Validate Sketchfab URL
    @param value:
    @type value:
    @param context:
    @type context:
    @return:
    @rtype:
    '''

    pattern = 'http[s]?:\/\/[w+3.]?sketchfab.com\/models\/[0-9a-z]+'
    if re.search(pattern, value, re.IGNORECASE):
        return value

    raise Invalid(_('Not a valid Sketchfab model URL'))