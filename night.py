import requests
r = requests.get("https://api.quotable.io/random")
data = r.json()
print(f"🌙 {data['content']} — {data['author']}")
