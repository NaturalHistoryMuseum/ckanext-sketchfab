from unittest.mock import MagicMock

from ckanext.sketchfab.plugin import SketchfabPlugin


def test_always_visible():
    plugin = SketchfabPlugin()
    assert plugin.can_view(MagicMock())
