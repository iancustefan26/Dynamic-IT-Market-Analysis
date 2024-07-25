import json
import heapq

class location:
    def __init__(self, dict):
        self.name = dict.get('canonical_name', [])
        self.population = dict.get('reach', [])
    def __lt__(self, other):
        return self.population > other.population
    
def get_reach(dict):
    return dict.get('reach', [])

def push(queue, item):
    heapq.heappush(queue,item)

def pop(queue):
    return heapq.heappop(queue)

json_file = open("/Users/stefaniancu/DOcuments/VS Code/JobScraperEngine/jsons/locations.json").read(9999999999)

locations = json.loads(json_file)

priority_queue = []

for loc in locations:
    new = location(loc)
    push(priority_queue, new)
    #print(new.name, new.population)

for x in range (100):
    temp = pop(priority_queue)
    print(temp.name, temp.population)