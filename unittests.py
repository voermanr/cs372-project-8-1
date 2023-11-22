import unittest
import select_server
import socket
from unittest.mock import patch, MagicMock


class TestSelectServer(unittest.TestCase):
    def test_client_connected_message(self):
        test_port = 54690
        test_socket = MagicMock()

        test_socket.getpeername.return_value = ('127.0.0.1', 54690)
        self.assertEqual(select_server.client_connected_message(test_socket),
                         "('127.0.0.1', 54690): connected")


if __name__ == '__main__':
    unittest.main()
