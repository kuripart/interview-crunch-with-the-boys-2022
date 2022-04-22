#Author: Nithin Prasad
#Problem: CTCI Ch4 Trees and Graphs, Problem 1
#Description: Given a directed graph, design an algorithm to find out if there is
#  a route between nodes.

class Graph:

    def __init__(self):

        self.adjacencyList = {}

    def add_node(self,nodeElem,nodeConnectionList):

        self.adjacencyList[nodeElem] = nodeConnectionList[:]

    def has_node(self,node):

        if self.adjacencyList.get(node) == None:
            return False
        else:
            return True

    def get_neighbours(self,node):
        '''
        defined as any nodes which have arrows coming in from current node
        '''

        if self.adjacencyList.get(node) != None:
            return self.adjacencyList[node][:]
        else:
            return None

    def print_graph(self):

        print("------------------")
        print("Graph:")
        for elem in self.adjacencyList.keys():
            print(elem,":",self.adjacencyList[elem])


def route_between_nodes(graph, nodeStart, nodeDest):

##    print("-------------------------------------")
    #Returns false if graph doesn't have either start/dest nodes
    if not graph.has_node(nodeStart):
##        print("edge case 1")
        return False

    #Process the neighbours of each node from start -> dest in DFS
    expansionList = [nodeStart]
    goalReached = False

##    print("Expanding...")
##    print("Initial Expansion List:",expansionList)

    while len(expansionList) > 0 and not(goalReached):

        currNode = expansionList.pop(0)

        neighbours = graph.get_neighbours(currNode)

##        print("Expansion List:",expansionList)
##        print("Current Node:",currNode)
##        print("Neighbours:",neighbours)
        
        if neighbours != None:
##            print("In Neighbour evaluation")
            newList = []
            for neighbour in neighbours:
##                print("Single neighbour:",neighbour)
                if neighbour == nodeDest:
##                    print("Goal is reached!?")
                    goalReached = True
                    break
                else:
                    newList.append(neighbour)

            expansionList = newList + expansionList

    if goalReached:
        return True
    else:
        return False
    
############################ NOTES ##############################
# 1) Use VISITED set to prevent cycles etc
# 2) Evaluate DFS vs BFS (pros and cons)


if __name__ == "__main__":

##    testGraph = Graph()
##    
##    testGraph.add_node(1,[2,3])
##    testGraph.add_node(2,[3])
##    testGraph.print_graph()
##    print(testGraph.has_node(1))
##    print(testGraph.has_node(4))
##    print(testGraph.get_neighbours(1))
##    print(testGraph.get_neighbours(3))

    graphA = Graph()
    graphA.add_node(1,[2,3])
    graphA.add_node(2,[3])
    graphA.print_graph()
    print(route_between_nodes(graphA,1,2))
    print(route_between_nodes(graphA,1,3))
    print(route_between_nodes(graphA,2,1))
    print(route_between_nodes(graphA,2,3))
    print(route_between_nodes(graphA,3,1))
    print(route_between_nodes(graphA,3,2))
    print(route_between_nodes(graphA,4,1))
    print(route_between_nodes(graphA,1,4))









    
