import requests

url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
r = requests.head(url=url)
print(r.headers['link'])
print(r.links["next"])
print(r.links["last"])
