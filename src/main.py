#region Imports
from rich import print
from rich.console import Console

from helper import Dotenv
from helper import Logger
from teamspeak import TeamspeakClient

import json
#endregion

#region Setup & ENV
console = Console()
logger = Logger(console)
dotenv = Dotenv()

api_key     = dotenv.get("API_KEY")
api_version = dotenv.get("API_VERSION")
api_url     = dotenv.get("SERVER_ADDRESS")
api_scheme  = dotenv.get("SERVER_SCHEME")
is_dev_env  = bool(dotenv.get("DEV"))
base_url    = f"{api_scheme}://{api_url}"

client = TeamspeakClient(base_url, api_version, api_key, is_dev_env)
#endregion

#region Main
clients = client.get_clients()
print(json.dumps(clients, indent=4))







#endregion

#region Saving History
client.save_history(f"history/{api_url}")
#endregion

