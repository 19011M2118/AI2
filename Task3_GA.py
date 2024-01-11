#0 is start 1 is normal 5 is a wall 7 is end
#0 1 and 7 can be traversed
import math
from queue import Queue
graph = (   #5        10        15        20        25        30        35          40
    (5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5),#0
    (5,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,5),#1
    (5,5,5,5,5,5,5,1,5,5,5,5,5,1,5,5,5,5,5,1,5,5,5,1,5,5,5,5,5,5,5,5,5,1,5,1,5,1,5,5,5),#2
    (5,1,1,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5),#3
    (5,1,5,5,5,5,5,5,5,5,5,1,5,5,5,1,5,1,5,5,5,1,5,5,5,5,5,1,5,1,5,5,5,5,5,1,5,5,5,1,5),#4
    (5,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,1,1,5,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,5,1,5),#5
    (5,5,5,5,5,1,5,5,5,1,5,5,5,5,5,5,5,5,5,1,5,5,5,5,5,5,5,1,5,5,5,5,5,5,5,5,5,5,5,1,5),#6
    (5,1,1,1,5,1,1,1,5,1,1,1,1,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5),#7
    (5,1,5,1,5,5,5,1,5,5,5,5,5,5,5,5,5,1,5,1,5,1,5,5,5,1,5,5,5,5,5,5,5,5,5,1,5,5,5,5,5),#8
    (5,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5),#9
    (5,1,5,5,5,5,5,5,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,1,5,1,5,1,5),#10
    (5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,5,1,1,1,5,1,5,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,5),#11
    (5,1,5,1,5,5,5,1,5,1,5,5,5,5,5,1,5,5,5,5,5,1,5,1,5,5,5,5,5,1,5,5,5,5,5,1,5,5,5,1,5),#12
    (5,1,5,1,1,1,5,1,5,1,5,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,1,1,5,7,1,1,5),#13
    (5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5),#14
)
#replace 1 with 5
#replace 0 with 1
width=41
height=15
#print("first step")

#this is used to find neighbours that can be traversed
def can_traverse(graph,location):
    (x,y)=location
    return graph[x][y] != 5
#this is also to find neighbours that can be traversed
def inBounds(graph,location):
        (x, y) = location
        return 0 <= x < width and 0 <= y <height
real_nodes1=[]
#only neighbours that are not walls and that are inbounds can be traversed
#this is the neighbours function
def neighbors(graph,location):
        (x, y) = location
        nodes = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        real_nodes=[]
        #filters out the nodes that are inbounds and those that can be passed
        for i in range(4):
            if (inBounds(graph,nodes[i]) and can_traverse(graph,nodes[i])):
                real_nodes.append(nodes[i])
        return real_nodes
real_nodes1=neighbors(graph,(0,2))
#print(real_nodes1)
#neighbours function takes the graph and the location and gives possible neighbours that are both in bounds and can be traversed


#00 = down
#10 = left
#01 = right
#11 = up
start=(1,1)
goal=(13,37)
list_moves=['00','10','01','11']
def run_chromosome(chromosome,graph,location):
    (x, y) = location
    graph1=graph
    if chromosome=='00':
        x=x+1
        new_location=(x,y)
    elif chromosome=='10':
        y=y-1
        new_location=(x,y)
    elif chromosome=='01':
        y=y+1
        new_location=(x,y)
    elif chromosome=='11':
        x=x-1
        new_location=(x,y)
    else:
        print("invalid chromosome")
    return new_location

print("This will take a long time to run")
#this is the population, includes all traversable nodes
def population(graph,start,goal):
    (x, y) = start
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        (x,y) = current
        if (x,y) == goal:
            break
        for next in neighbors(graph,current):
            frontier.put(next)
            came_from[next] = current
        #print(current)
    return came_from.keys()
global_population=population(graph,start,goal)
print(global_population)
#this prints all the traversable nodes
traversed_nodes=[]
print("4th step")


def fitness(chromosome):
        if run_chromosome(chromosome,graph,start) in global_population:
            new_location=run_chromosome(chromosome,graph,start)
            traversed_nodes.append(new_location)
            #print(new_location)
            for i in range(15):
                if run_chromosome(chromosome,graph,new_location) in global_population:
                    new_location=run_chromosome(chromosome,graph,new_location)
                    traversed_nodes.append(new_location)
        return 1.0 - math.dist(new_location, goal)
list1=[]
list1.append('00')
list1.append('01')
list1.append('11')
print("Least distance after 1st generation from the fitness function is:")
print(max(list1))
max_list1=max(list1)
index_variable=list1.index(max_list1)
print(list_moves[index_variable])
fitness(list_moves[index_variable])
print(traversed_nodes)
print("\n\n\n")
#1st generation runs each direction once
#2nd generation runs from the closest nodes after running generation 1
traversed_nodes2=[]
def fitness2(chromosome):
        if run_chromosome(chromosome,graph,(3,4)) in global_population:
            new_location=run_chromosome(chromosome,graph,(3,4))
            traversed_nodes2.append("separation character")
            traversed_nodes2.append(new_location)
            #print(new_location)
            for i in range(15):
                if run_chromosome(chromosome,graph,new_location) in global_population:
                    new_location=run_chromosome(chromosome,graph,new_location)
                    traversed_nodes2.append(new_location)
        return 1.0 - math.dist(new_location, goal)
def crossover(chromosome):
    if chromosome=='00':
        chromosome=="'01'"
    elif chromosome=='01':
        chromosome=="'10'"
    elif chromosome=='10':
        chromosome=="'01'"
    elif chromosome=='11':
        chromosome=="'00'"
    else:
        print("invalid move")
    return chromosome
def genetic_algorithm(graph,start,goal,chromosome):
    (x, y) = start
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        (x,y) = current
        if (x,y) == goal:
            break
        for next in neighbors(graph,current):
            frontier.put(next)
            came_from[next] = current
    crossover(chromosome)
    fitness2(chromosome)
    return traversed_nodes2
path=genetic_algorithm(graph,start,goal,'00')
    



