from baseclient import BaseClient


class TeamspeakClient(BaseClient):
    def __init__(self,
        api_url: str, 
        api_version: str, 
        api_key: str, 
        store_history: bool = True,
    ):
        super().__init__(api_url, api_version, api_key, store_history)

    def get_clients(self) -> list:
        return self.get_request("/serverinfo")