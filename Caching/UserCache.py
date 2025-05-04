from datetime import datetime
import pickle

localTime = datetime.now().strftime("%Y-%m-%d -- %H:%M")

def Caching(user, response):
    cache = {}    
    
    if user in cache:
        cache[user].append(f"({localTime}) {response}")
    cache[user] = (f"({localTime}) {response}") 

    with open("cache.pkl", "wb") as file: # .pkl is the pickle file extension for storring data and the file is accessed in write binary mode
        pickle.dump(cache, file)
    
def Fetching(user):
    with open("cache.pkl", "rb") as file:
        loaded_cache = pickle.load(file)
    return loaded_cache