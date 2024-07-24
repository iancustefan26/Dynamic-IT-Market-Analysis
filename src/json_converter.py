import json
import heapq

class location:
    def __init__(self, dict):
        self.name = dict.get('canonical_name', [])
        self.population = dict.get('reach', [])
    def __lt__(self, other):
        return self.population < other.population
    
def get_reach(dict):
    return dict.get('reach', [])

def push(queue, item):
    heapq.heappush(queue,item)

def pop(queue):
    heapq.heappop(queue)

json_file = open("/Users/stefaniancu/DOcuments/VS Code/JobScraperEngine/jsons/locations.json").read(9999999999)

locations = json.loads(json_file)

priority_queue = []

for loc in locations:
    if len(priority_queue) > 10:
        push(priority_queue, location(loc))
        pop(priority_queue)
    else:
        push(priority_queue, location(loc))

for i in range(10):
    print(pop(priority_queue))
