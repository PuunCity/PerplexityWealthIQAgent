from datetime import datetime
import pickle

localTime = datetime.now().strftime("%Y-%m-%d -- %H:%M")

# Initial fetch
cache = {}
with open("cache.pkl", "rb") as file:
    cache = pickle.load(file)


def Caching(user, response):    
    if user not in cache:
        cache[user] = [f"({localTime}) {response}"]
        print("created new caching profile!")
    else:
        cache[user].append(f"({localTime}) {response}")
        print("caching data!")

    with open("cache.pkl", "wb") as file: # .pkl is the pickle file extension for storring data and the file is accessed in write binary mode
        pickle.dump(cache, file)
    
def Fetching():
    with open("cache.pkl", "rb") as file:
        if not file:
            print("No data associated to user! (Maybe try creating a query?)")
        loaded_cache = pickle.load(file)
    return loaded_cache