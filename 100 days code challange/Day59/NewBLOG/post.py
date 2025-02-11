import requests
class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    def text(self):
        response = requests.get(self.blog_url)
        data = response.json()
        return data