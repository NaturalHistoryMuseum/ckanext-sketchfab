from ckanext.sketchfab.plugin import SketchfabPlugin
from mock import MagicMock


def test_always_visible():
    plugin = SketchfabPlugin()
    assert plugin.can_view(MagicMock())
