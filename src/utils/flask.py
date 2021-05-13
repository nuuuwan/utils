"""Flask (https://en.wikipedia.org/wiki/Flask_(web_framework)) utils."""

import logging
from utils import www


class FlaskClient:
    """Implements FlaskClient.

    Args:
        server_name(str): Name of flask app
        host (str): host
        port (int): port

    .. code-block:: python

        >>> from utils.flask import FlaskClient
        >>> client = FlaskClient('geo', '127.0.0.1', 5000)

    """

    def __init__(self, server_name, host, port):
        """Init."""
        self.host = host
        self.port = port
        self.server_name = server_name

    def get_url(self, cmd, param_list):
        """Get URL.

        Args:
            cmd(str): command
            param_list (list): params

        Assumes URL building convention:
            http://<host>:<port>/<server_name>_server/<cmd>/<params>
            or
            http://<host>:<port>/<cmd>/<params>

        Returns:
            URLs
        """
        return 'http://%s:%d%s/%s/%s' % (
            self.host,
            self.port,
            ('/%s_server' % self.server_name) if self.server_name else '',
            cmd,
            '/'.join(param_list),
        )

    def run(self, cmd, param_list):
        """Run client request.

        Args:
            cmd(str): command
            param_list (list): params

        Returns:
            Flask server response

        .. code-block:: python

            >>> from utils.flask import FlaskClient
            >>> client = FlaskClient('gig', '127.0.0.1', 5000)
            >>> client.run('get_entity', 'LK-11')

        """
        url = self.get_url(cmd, param_list)
        logging.info('utils.flask.FlaskClient.run: %s', url)
        return www.read_json(url)
