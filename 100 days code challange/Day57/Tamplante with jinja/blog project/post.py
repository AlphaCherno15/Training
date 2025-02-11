import requests
class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    def text(self):
        response = requests.get(self.blog_url)
        data = response.json()
        return data