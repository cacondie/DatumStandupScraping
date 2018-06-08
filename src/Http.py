import requests as r

class Http:
    def get_page(self, address):
        return r.get(address)