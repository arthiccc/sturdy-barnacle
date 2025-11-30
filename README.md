# sturdy-barnacle

Python "Quote of the Night" CLI
What you’ll do: Write a Python script that fetches a random inspirational quote from an API and prints it in your terminal.

Steps:

Install Python: pkg install python

Install requests: pip install requests

Create quote.py:
```py
python
import requests
r = requests.get("https://api.quotable.io/random")
data = r.json()
print(f"🌙 {data['content']} — {data['author']}")
```
Run: python quote.py
