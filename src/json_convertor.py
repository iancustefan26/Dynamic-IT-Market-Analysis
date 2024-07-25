import json
import heapq

json_file = open("/Users/stefaniancu/DOcuments/VS Code/JobScraperEngine/jsons/locations.json").read(9999999999)
locations = json.loads(json_file)
priority_queue = []

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

def fill_queue():
    global priority_queue,locations
    for loc in locations:
        new = location(loc)
        push(priority_queue, new)


def extract_countries(number):
    fill_queue()
    list = []
    list.append("China")
    global priority_queue
    for x in range(number - 1):
        list.append(pop(priority_queue).name)
    return list

