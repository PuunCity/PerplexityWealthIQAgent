from datetime import datetime
localTime = datetime.now().strftime("%Y-%m-%d -- %H:%M")

def Caching(user, response):
    with open("Caching/cache.txt", "a") as file:
        file.write(f"User: {user},\nSummary: ({localTime}) {response}\n\n")
 