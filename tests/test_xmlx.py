"""Test."""
import io
import unittest

from utils.xmlx import _, style


class TestXMLX(unittest.TestCase):
    """Test."""

    def test_log_metric(self):
        """Test."""
        head = _('head')
        body = _(
            'body',
            [
                _('h1', 'This is header 1', style(font_family='Georgia')),
                _('p', 'This is a paragraph'),
                _(
                    'div',
                    [
                        _('span', 'This is a span in a div'),
                        _(
                            'a',
                            'This is a a(link) in a div',
                            dict(
                                href='https://pypi.org/project/utils-nuuuwan'
                            ),
                        ),
                    ],
                ),
            ],
        )
        html = _('html', [head, body])
        actual_file = '/tmp/utils.tests.test_xmlx.html'
        html.store(actual_file)

        expected_file = 'tests/test_xmlx_example1.html'
        self.assertListEqual(
            list(io.open(actual_file)),
            list(io.open(expected_file)),
        )
