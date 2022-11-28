from unittest.mock import MagicMock

import pytest
from ckan.plugins import toolkit

from ckanext.sketchfab.logic.validators import is_valid_sketchfab_url


class TestIsValidSketchfabURL(object):
    def test_valid(self):
        url = 'https://sketchfab.com/models/f157e030b89b4682bcc6ea808533c823'
        assert is_valid_sketchfab_url(url, MagicMock())

    def test_invalid1(self):
        url = 'https://sketchfab.com/'
        with pytest.raises(toolkit.Invalid):
            is_valid_sketchfab_url(url, MagicMock())

    def test_invalid2(self):
        url = 'https://data.nhm.ac.uk/'
        with pytest.raises(toolkit.Invalid):
            is_valid_sketchfab_url(url, MagicMock())
