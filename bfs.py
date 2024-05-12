from collections import deque # double ended queue module

# graph definition - hardcoded or retrieved from source
graph = []

# searched condition to meet with a node
def exit_condition():
    print("Eval node")

# Breadth-first Search main algorithm
def bfsearch(starting_node):
    queue = deque() #queue init
    queue += graph[starting_node]
    queued = set()

    while queue:
        node_to_analyze = queue.popleft()
        if not node_to_analyze in queued:
            if exit_condition(node_to_analyze):
                print("Success Message")
                return True
            else:
                queue += graph[node_to_analyze]
                queued.add(node_to_analyze)
    return False

bfsearch(graph["me"])
