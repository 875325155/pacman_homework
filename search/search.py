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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #use stack
    stack = util.Stack()
    state = problem.getStartState()
    stack.push((state, []))
    visited=[]
    # print state
    # for i in problem.getSuccessors(state):
    #     print i
    while not stack.isEmpty():
        current_state, actions = stack.pop()
        if problem.isGoalState(current_state):
            return actions
        if current_state not in visited:
            explored=problem.getSuccessors(current_state)
            visited.append(current_state)
            for pos, dir, step_cost in explored:
                if (pos not in visited):
                    stack.push((pos,actions+[dir]))
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # # use queue
    # queue = util.Queue()
    # state = problem.getStartState()
    # queue.push((state, [], []))
    # while not queue.isEmpty():
    #     current_state, actions, visited = queue.pop()
    #     '''
    #      For a given state, this should return a list of triples, (successor,
    #      action, stepCost), where 'successor' is a successor to the current state,
    #      'action' is the action required to get there, and 'stepCost' is the incremental
    #      cost of expanding to that successor.
    #     '''
    #     for pos, dir, step in problem.getSuccessors(current_state):
    #         if pos not in visited:
    #             # Returns True if and only if the state is a valid goal state.
    #             if problem.isGoalState(pos):
    #                 return actions + [dir]
    #             # if not
    #             queue.push((pos, actions + [dir], visited + [current_state]))
    # queue = util.Queue()
    # state = problem.getStartState()
    # queue.push((state, list()))
    #
    # visited = list()
    # while not queue.isEmpty():
    #     node, actions = queue.pop()
    #
    #     for pos, dir, steps in problem.getSuccessors(node):
    #         if not pos in visited:
    #             visited.append(pos)
    #             if problem.isGoalState(pos):
    #                 return actions + [dir]
    #             queue.push((pos, actions + [dir]))
    # visited = []
    # fringe = util.Queue()
    # fringe.push([(problem.getStartState(), 'STOP', 0)])
    #
    # while not fringe.isEmpty():
    #     current_path = fringe.pop()
    #     current_state = current_path[len(current_path) - 1]
    #
    #     if not current_state[0] in visited:
    #         visited.append(current_state[0])
    #
    #         if problem.isGoalState(current_state[0]):
    #             return map(lambda state: state[1], current_path[1:])
    #
    #         non_visited_states = filter(lambda next_successor: not next_successor[0] in visited,
    #                                     problem.getSuccessors(current_state[0]))
    #
    #         for successor in non_visited_states:
    #             next_item = list(current_path)
    #             next_item.append(successor)
    #             fringe.push(next_item)
    queue = util.Queue()
    state = problem.getStartState()
    queue.push((state, []))
    visited = []
    # print state
    # for i in problem.getSuccessors(state):
    #     print i
    while not queue.isEmpty():
        current_state, actions = queue.pop()
        if problem.isGoalState(current_state):
            return actions
        if current_state not in visited:
            explored = problem.getSuccessors(current_state)
            visited.append(current_state)
            for pos, dir, step_cost in explored:
                if (pos not in visited):
                    queue.push((pos, actions + [dir]))
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    #use PriorityQueue
    # pri_queue=util.PriorityQueue()
    # state=problem.getStartState()
    # #tumple for item,0 for Priority last,just to initialize
    # pri_queue.push((state,[]),0)
    # visited=[]
    # while not pri_queue.isEmpty():
    #     current_state, actions = pri_queue.pop()
    #     if problem.isGoalState(current_state):
    #         return actions
    #     visited.append(current_state)
    #
    #     for pos,dir,steps in problem.getSuccessors(current_state):
    #         if pos not in visited:
    #             next_actions=actions+[dir]
    #             pri_queue.push((pos,next_actions),problem.getCostOfActions(next_actions))
    pri_queue = util.PriorityQueue()
    state = problem.getStartState()
    pri_queue.update((state, [],0),0)
    visited = []
    # print state
    # for i in problem.getSuccessors(state):
    #     print i
    while not pri_queue.isEmpty():
        (current_state, actions,fn) = pri_queue.pop()
        if problem.isGoalState(current_state):
            return actions
        if current_state not in visited:
            explored = problem.getSuccessors(current_state)
            visited.append(current_state)
            for pos, dir, step_cost in explored:
                if (pos not in visited):
                    pri_queue.update((pos, actions + [dir],fn+step_cost),step_cost+fn)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # visited = []
    # fringe = util.PriorityQueue()
    # start = ([(problem.getStartState(), 'STOP', 0)], 0)
    # fringe.push(start, 0)
    # while not fringe.isEmpty():
    #     current_path = fringe.pop()
    #     current_state = current_path[0][len(current_path[0]) - 1]
    #
    #     if not current_state[0] in visited:
    #         visited.append(current_state[0])
    #
    #         if problem.isGoalState(current_state[0]):
    #             return map(lambda state: state[1], current_path[0][1:])
    #
    #         non_visited_states = filter(lambda next_successor: not next_successor[0] in visited,
    #                                     problem.getSuccessors(current_state[0]))
    #
    #         for successor in non_visited_states:
    #             cost = current_path[1] + successor[2]
    #             next_item = (list(current_path[0]), cost)
    #             next_item[0].append(successor)
    #             fringe.push(next_item, cost+heuristic(successor[0],problem))
    #
    pri_queue = util.PriorityQueue()
    state = problem.getStartState()
    pri_queue.update((state, [], 0), 0)
    visited = []
    # print state
    # for i in problem.getSuccessors(state):
    #     print i
    while not pri_queue.isEmpty():
        (current_state, actions, fn) = pri_queue.pop()
        if problem.isGoalState(current_state):
            return actions
        if current_state not in visited:
            explored = problem.getSuccessors(current_state)
            visited.append(current_state)
            for pos, dir, step_cost in explored:
                if (pos not in visited):
                    pri_queue.update((pos, actions + [dir], fn + step_cost), fn + step_cost+nullHeuristic(pos,problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
