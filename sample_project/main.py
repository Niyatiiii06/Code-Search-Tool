from utils import search_web


def run():
    result = search_web("AI")
    print(result)


run()
class Client:

    def search_web(self, query):
        return query


client = Client()

client.search_web("AI")