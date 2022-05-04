class NoConnection(Exception):
    def __init__(self):
        super(NoConnection, self).__init__("No Connection between nodes!")