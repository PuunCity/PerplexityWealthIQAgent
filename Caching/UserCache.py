def Caching(user, response):
    with open("Caching/cache.txt", "a") as file:
        file.write(f"User: {user},\nSummary: {response}\n\n")
