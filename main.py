from cspbase import *
from testcase import *
from model import *
import itertools
import traceback
import time
import math

from propagators import *
#numtree = 0
#heuristic = "MRV"

class AlberiSolver:

    def __init__(self, board, model, propagator, heur, trees, priority):
        self.numtree = trees
        self.heuristic = heur
        self.board = board
        self.model = model
        # Time the model creation
        model_start_time = time.time()
        cspmodel = model(board, priority, self.numtree)
        model_finish_time = time.time()
        self.model_creation_time = model_finish_time - model_start_time
        self.varlist = cspmodel[1]
        self.csp = cspmodel[0]
        self.dim = len(self.varlist)
        self.propagator = propagator
        self.heuristic = heur
        self.runtime = 1000000000

    def print_solution(self):
        for row in self.varlist:
            print([var.get_assigned_value() for var in row])

    def run(self):
        print("Puzzle: {} by {}, {} trees".format(self.dim, self.dim, self.numtree))
        print("Model creation time: {}".format(self.model_creation_time))
        # create backtracking routine
        bt = BT(self.csp, self.heuristic)
        #bt.trace_on()
        starttime = time.time()
        bt.bt_search(self.propagator)
        self.runtime = time.time() - starttime
        self.print_solution()

def routinetest(board, numtree):
    models = [alberi_model_1, alberi_model_2]
    ms = ["alberi_model_1", "alberi_model_2"]
    orders = [0,1]
    props = [prop_BT, prop_FC, prop_GAC, prop_alberi]
    ps = ["prop_FC", "prop_GAC", "prop_alberi"]
    heuristics = ["MAV", "MRV"]


    print("===========Compare routines===========")
    mintime = 100000000
    minroutine = [0,0,0,0]
    maxtime = 0
    maxroutine = [0,0,0,0]
    for i in range(0,len(models)):
        for j in range(0,len(orders)):
            for k in range(0,len(props)):
                for m in range(0,len(heuristics)):
                    print("--model:{}-priority:{}-prop:{}-heur:{}".format(ms[i],str(orders[j]),ps[k],heuristics[m]))
                    alberi = AlberiSolver(board, models[i], props[k], heuristics[m], numtree, orders[j])
                    alberi.run()
                    if alberi.runtime < mintime:
                        mintime = alberi.runtime
                        minroutine = [i,j,k,m]
                    if alberi.runtime > maxtime:
                        maxtime = alberi.runtime
                        maxroutine = [i,j,k,m]

    print("Fastest routine: {} average time: {}".format(minroutine, mintime))
    print("Slowest routine: {} average time: {}".format(maxroutine, maxtime))


def test():
    dic_1tree = dict()
    dic_1tree[5] = [solveable_1tree3, solveable_1tree4]
    dic_1tree[6] = [solveable_1tree1, solveable_1tree2]
    dic_ltree[7] = [solveable_1tree5]
    dic_2trees = dict()
    dic_2trees[9] = [solveable_2tree1, solveable_1tree2]
    dic_2trees[10] = [solveable_2tree3]

    for b_size in dic_1tree:
        numtree = 1
        for board in dic_1tree[b_size]:

            print("board size: " + b_size)
            print("number of trees: " + numtree)

            models = [alberi_model_1, alberi_model_2]
            ms = ["alberi_model_1", "alberi_model_2"]
            orders = [0, 1]
            props = [prop_BT, prop_FC, prop_GAC, prop_alberi]
            ps = ["prop_FC", "prop_GAC", "prop_alberi"]
            heuristics = ["MAV", "MRV"]
            print("===========Compare routines===========")
            mintime = 100000000
            minroutine = [0, 0, 0, 0]
            maxtime = 0
            maxroutine = [0, 0, 0, 0]
            for i in range(0, len(models)):
                for j in range(0, len(orders)):
                    for k in range(0, len(props)):
                        for m in range(0, len(heuristics)):
                            print("--model:{}-priority:{}-prop:{}-heur:{}".format(ms[i], str(orders[j]), ps[k], heuristics[m]))
                            alberi = AlberiSolver(board, models[i], props[k], heuristics[m], numtree, orders[j])
                            alberi.run()
                            if alberi.runtime < mintime:
                                mintime = alberi.runtime
                                minroutine = [i, j, k, m]
                            if alberi.runtime > maxtime:
                                maxtime = alberi.runtime
                                maxroutine = [i, j, k, m]
            print("Fastest routine: {} average time: {}".format(minroutine, mintime))
            print("Slowest routine: {} average time: {}".format(maxroutine, maxtime))


    for b_size in dic_2trees:
        numtree = 2
        for board in dic_2trees[b_size]:

            print("board size: " + b_size)
            print("number of trees: " + numtree)

            models = [alberi_model_1, alberi_model_2]
            ms = ["alberi_model_1", "alberi_model_2"]
            orders = [0, 1]
            props = [prop_BT, prop_FC, prop_GAC, prop_alberi]
            ps = ["prop_FC", "prop_GAC", "prop_alberi"]
            heuristics = ["MAV", "MRV"]
            print("===========Compare routines===========")
            mintime = 100000000
            minroutine = [0, 0, 0, 0]
            maxtime = 0
            maxroutine = [0, 0, 0, 0]
            for i in range(0, len(models)):
                for j in range(0, len(orders)):
                    for k in range(0, len(props)):
                        for m in range(0, len(heuristics)):
                            print("--model:{}-priority:{}-prop:{}-heur:{}".format(ms[i], str(orders[j]), ps[k],
                                                                                  heuristics[m]))
                            alberi = AlberiSolver(board, models[i], props[k], heuristics[m], numtree, orders[j])
                            alberi.run()
                            if alberi.runtime < mintime:
                                mintime = alberi.runtime
                                minroutine = [i, j, k, m]
                            if alberi.runtime > maxtime:
                                maxtime = alberi.runtime
                                maxroutine = [i, j, k, m]
            print("Fastest routine: {} average time: {}".format(minroutine, mintime))
            print("Slowest routine: {} average time: {}".format(maxroutine, maxtime))


if __name__ == '__main__':
    routinetest(solveable_1tree1, 1)