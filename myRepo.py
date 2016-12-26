from datetime import datetime


class Repo:
    id = ""
    date = ""
    owner = ""

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.access_count = 0

    def increment_access_count(self):
        self.access_count += 1
