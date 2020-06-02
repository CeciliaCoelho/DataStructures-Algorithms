#O(Vertices + Edges)

from collections import deque

def is_seller(name):
    return (name[-1] == 'm')

def BFSearch(name):
    search_queue = deque()
    search_queue += graph[name]
    checked = []

    while search_queue:
        person = search_queue.popleft()
        if not person in checked:
            if is_seller(person):
                print(person + " has a nice name!")
                return True
            else:
                checked.append(person)
                search_queue += graph[person]
    return False

graph = {}
graph['me'] = ['alice' , 'bob' , 'claire']
graph['bob'] = ['anuj' , 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom' , 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['jonny'] = []
graph['thom'] = []

BFSearch('me')
