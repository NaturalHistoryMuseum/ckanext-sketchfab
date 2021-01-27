from ckanext.sketchfab.plugin import SketchfabPlugin
from unittest.mock import MagicMock


def test_always_visible():
    plugin = SketchfabPlugin()
    assert plugin.can_view(MagicMock())
