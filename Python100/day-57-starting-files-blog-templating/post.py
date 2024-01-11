class Post:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.title = data_dict["title"]
        self.subtitle = data_dict["subtitle"]
        self.body = data_dict["body"]
