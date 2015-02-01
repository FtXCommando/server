import pytest
import mock
import pytestqt

from PySide import QtNetwork

from GameConnection import GameConnection
from games import Game

import logging
logging.getLogger("GameConnection").setLevel(logging.DEBUG)

@pytest.fixture()
def game_socket():
    return mock.Mock(spec=QtNetwork.QTcpSocket)

@pytest.fixture()
def host_game_connection(game_socket):
    conn = GameConnection(game_socket)
    conn.player = mock.Mock()
    conn.player.getAction = mock.Mock(return_value="HOST")
    return conn

def test_handleAction_PlayerOption(host_game_connection):
    game = mock.Mock(spec=Game(1))
    host_game_connection.game = game
    host_game_connection.handleAction('PlayerOption', [1, 'Color', 2])
    game.setPlayerOption.assert_called_once_with(1, 'Color', 2)

def test_handleAction_GameOption(host_game_connection):
    game = mock.Mock(spec=Game(1))
    host_game_connection.game = game
    host_game_connection.handleAction('PlayerOption', [1, 'Color', 2])
    game.setPlayerOption.assert_called_once_with(1, 'Color', 2)

