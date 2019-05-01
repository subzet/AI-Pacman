# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    "Definimos la frontera como una Pila de la librería util"
    frontera = util.Stack()
    "Ingresamos a la pila el nodo inicial"
    frontera.push((problem.getStartState(),[],[]))

    i = 0

    while not frontera.isEmpty():
        print("----------------------------------")
        i += 1
        print("Paso n: ", i)

        "Tomamos el primer nodo de la pila"
        nodo, acciones, visitados = frontera.pop()
        print("Nodo quitado de la frontera: ",nodo)

        "Si el nodo es un estado objetivo devolvemos el camino trazado"
        if problem.isGoalState(nodo):
            print("Nodo objetivo alcanzado! generando camino")
            print(acciones)
            print("----------------------------------")
            return acciones

        "Por cada hijo en los estados sucesores del estado para el nodo actual, agregamos los  nodos a la pila, priorizando el más profundo"
        for hijo, direccion, pasos in problem.getSuccessors(nodo):
            if not hijo in visitados:
                print("Nodo agregado a la frontera: ", hijo)
                frontera.push((hijo, acciones + [direccion], visitados + [nodo]))

        print("Nodos ya visitados:,",visitados)
    """util.raiseNotDefined()"""

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    "Definimos la frontera como una cola que utilizaremos para el problema"
    frontera = util.Queue()

    frontera.push((problem.getStartState(),[],[]))

    i = 0

    while not frontera.isEmpty():
        print("----------------------------------")
        i += 1
        print("Paso n: ", i)
        "Tomamos el primer nodo de la cola"
        nodo, acciones, visitados = frontera.pop()
        print("Nodo quitado de la frontera: ", nodo)

        if problem.isGoalState(nodo):
            print("Nodo objetivo alcanzado! generando camino")
            print(acciones)
            print("----------------------------------")
            return acciones

        for hijo, direccion, pasos in problem.getSuccessors(nodo):
            if not hijo in visitados:
                print("Nodo agregado a la frontera: ", hijo)
                "Si no fue visitado Agregamos el nodo a la frontera, la direccion para llegar allí a las acciones y el nodo actual a nodo visitados"
                frontera.push((hijo, acciones + [direccion], visitados + [nodo]))

        print("Nodos ya visitados:,", visitados)
        """util.raiseNotDefined()"""

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "Definimos la frontera como una cola con prioridad"
    frontera = util.PriorityQueue();

    "Añadimos el primer nodo del problema con un costo de 0"
    frontera.push((problem.getStartState(),[], 0  ), 0 )
    visitados = []

    i = 0

    while not frontera.isEmpty():
        print("----------------------------------")
        i += 1
        print("Paso n: ", i)

        nodo, acciones, costoActual = frontera.pop()
        print("Nodo quitado de la frontera: ", nodo, " con un costo de: ", costoActual)
        visitados.append(nodo)

        if problem.isGoalState(nodo):
            print("Nodo objetivo alcanzado! generando camino. Costo: ", costoActual)
            print(acciones)
            print("----------------------------------")
            return acciones

        for hijo,direccion,costo in problem.getSuccessors(nodo):
            if hijo not in visitados:
                print("Nodo agregado a la frontera: ", hijo, "Costo de explorar hijo: ", costoActual + costo)
                frontera.push((hijo, acciones + [direccion] , costoActual + costo), costoActual + costo)




    """util.raiseNotDefined()"""

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    "Definimos la frontera como una cola con prioridad"
    frontera = util.PriorityQueue();

    "Añadimos el primer nodo del problema con un costo de 0"
    frontera.push((problem.getStartState(),[], 0 + heuristic(problem.getStartState(),problem) ), 0 + heuristic(problem.getStartState(),problem) )
    visitados = []

    i = 0

    while not frontera.isEmpty():
        print("----------------------------------")
        i += 1
        print("Paso n: ", i)

        nodo, acciones, costoActual = frontera.pop()
        print("Nodo quitado de la frontera: ", nodo, " costo acumulado de exploracion: ", costoActual)
        visitados.append(nodo)

        if problem.isGoalState(nodo):
            print("Nodo objetivo alcanzado! generando camino. Costo acumulado: ", costoActual)
            print(acciones)
            print("----------------------------------")
            return acciones

        for hijo,direccion,costo in problem.getSuccessors(nodo):
            if hijo not in visitados:
                costoheuristico = heuristic(hijo, problem)
                print("Nodo agregado a la frontera: ", hijo)
                print("Costo acumulado de exploración: ", costoActual)
                print("Costo real de explorarlo: ", costo)
                print("Costo heuristico de explorarlo: ", costoheuristico)
                print("Costo total de exploracion: ", costo + costoActual + costoheuristico)
                print("************************************")
                frontera.push((hijo, acciones + [direccion], costoActual + costo + costoheuristico), costoActual+costo+costoheuristico)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
