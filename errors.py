class NoConnection(Exception):
    def __init__(self):
        super(NoConnection, self).__init__("No Connection between nodes!")

class NodeDoesNotExist(Exception):
    def __init__(self, id: int):
        super(NodeDoesNotExist, self).__init__(f"Node with id {id} does not exist")