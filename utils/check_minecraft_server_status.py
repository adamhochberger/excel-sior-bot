import os
import socket
from datetime import datetime

from mcstatus import JavaServer
from dotenv import load_dotenv

load_dotenv()

IP = os.getenv('SERVER_IP')
PORT = os.getenv('SERVER_PORT')

SERVER_OFFLINE_MESSAGE = f"The server is offline, or unavailable."


def check_minecraft_server_status():
    server = JavaServer.lookup(address=f"{IP}:{PORT}", timeout=5)

    try:
        status = server.status()
        query = server.query()

        player_count = status.players.online
        player_max = status.players.max
        player_names = query.players.names

        player_name_string = f'{", ".join(player_names)}' if player_count > 0 else "None"
        current_datetime = datetime.now()
        datetime_string = current_datetime.strftime("%Y/%m/%d %H:%M:%S")

        result_message = f"As of {datetime_string}\n: " + \
                         f"The server currently has {player_count}/{player_max} players\n" + \
                         f"Players: {player_name_string}\n" + \
                         f"MOTD: {query.motd}"
    except socket.timeout:
        result_message = SERVER_OFFLINE_MESSAGE

    return result_message
