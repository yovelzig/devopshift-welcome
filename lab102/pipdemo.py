import httpx

respone = httpx.get("https://jsonplaceholder.typicode.com/users")
users = respone.json()
for user in users:
    print(user["name"])