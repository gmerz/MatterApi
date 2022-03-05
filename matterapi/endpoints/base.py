from ..client.base import BaseClient


class ApiBaseClass:
    def __init__(self, client: BaseClient, skip_response_parsing: bool = False):
        self.client = client
        self.skip_response_parsing = skip_response_parsing
