from cspbase import *
#import itertool


"""
The models is specified here. We test two different ways to impose the
constraints. Model 1 takes adjacency constraints as ternary, a.k.a. in any
2 by 2 area there is at most 1 tree planted. Model 2 has binary adjacency
constraints which will benefit forward checking pruning but requires way more
space and time to initialize.
"""

def alberi_model_1(board, priority, numtree):
    """
    This function takes a 2d array input as the board. This file must have
    n rows, each with n characters, e.g.
    
    [[AAABBB],
     [ACDEEB],
     [CCDDEF],
     [CCDDFF],
     [CCDDFF],
     [DDDDFF]]
    #key => different value,
    Each different character (like A) represents an area (a park). It also
    takes an integer numtree which represents how many trees are there in
    each row/column/park.
    
    It builds a CSP model with these parameters.
    """
    # Initialize variable list by reading the list
    cons=[]
    v_list = []
    v_board = []
    for a in range(len(board)):
        v_row = []
        for b in range(len(board)):
            if priority:
                newvar = Variable("V{}{}".format(a,b),[1,0])
            else:
                newvar = Variable("V{}{}".format(a,b),[0,1])
            v_list.append(newvar)
            v_row.append(newvar)
        v_board.append(v_row)
    # Create CSP object
    csp = CSP("alberi1",v_list)
    # Impose park constraints
    # e.g. building a library that takes the character
    parknames = []
    parks = dict()
    row = 0
    value = 0
    for c in board:
        col = 0
        for d in c:
            if d not in parknames:
                parknames.append(d)
                parks[d] = [(row,col)]
                
            else:
                parks[d].append((row,col))
            col+=1
            value+=1
        row+=1

    # as key and a list of tuples as value.
    # e.g.
    # The board above should yield
    # {A: [(0,0),(0,1),...,(1,0)],...,F: [(2,5),(3,3)...(5,5)]}
    # After building a library each library value translates to a scope
    # in the variable list
    #parkcons = []
    # print(csp.get_all_vars())
    for e in parknames:
        parkscope = [v_board[tup[0]][tup[1]] for tup in parks[e]]
        cons.append(Constraint("ParkCon-{}".format(e),parkscope,'o',numtree))
    # Impose row constraints
    #row_cons = []
    row_n = 0
    for k in v_board:
        rowscope = k
        row_n += 1
        cons.append(Constraint("RowCon-{}".format(row_n),rowscope,'o',numtree))
    # Impose column constraints
    #col_cons = []
    col_n = 0
    for aa in range(len(v_board)):
        colscope = []
        for bb in range(len(v_board)):
            colscope.append(v_board[bb][col_n])
        cons.append(Constraint("ColCon-{}".format(col_n),colscope,'o',numtree))
        col_n+=1
    # Impose adjacency constraints for each 2 by 2 grid area, named after the
    # upper left grid
    for i in range(len(v_board)-1):
        for j in range(len(v_board)-1):
            cons.append(Constraint(
                "ADCONS-({},{})".format(i,j),[v_board[i][j],
                                          v_board[i][j+1],
                                          v_board[i+1][j],
                                          v_board[i+1][j+1]],'a',numtree))
    for c in cons:
        csp.add_constraint(c)
    return csp, v_board


def alberi_model_2(board, priority, numtree):
    """
    This function takes a 2d array input as the board. This file must have
    n rows, each with n characters, e.g.
    
    [[AAABBB],
     [ACDEEB],
     [CCDDEF],
     [CCDDFF],
     [CCDDFF],
     [DDDDFF]]
    
    Each different character (like A) represents an area (a park). It also
    takes an integer numtree which represents how many trees are there in
    each row/column/park.
    
    It builds a CSP model with these parameters.
    
    * Unlike model 1, this model implements the adjacency constraints as
      binary constraints. It will benefit forward checking but make GAC slower
    """
    
    # Create CSP object
    # Initialize variable list by reading the list
    cons=[]
    v_list = []
    v_board = []
    for a in range(len(board)):
        v_row = []
        for b in range(len(board)):
            if priority:
                newvar = Variable("V{}{}".format(a,b),[1,0])
            else:
                newvar = Variable("V{}{}".format(a,b),[0,1])
            v_list.append(newvar)
            v_row.append(newvar)
        v_board.append(v_row)
    # Create CSP object
    csp = CSP("alberi1",v_list)
    # Impose park constraints
    # e.g. building a library that takes the character
    parknames = []
    parks = dict()
    row = 0
    value = 0
    for c in board:
        col = 0
        for d in c:
            if d not in parknames:
                parknames.append(d)
                parks[d] = [(row,col)]

            else:
                parks[d].append((row,col))
            col+=1
            value+=1
        row+=1

    # as key and a list of tuples as value.
    # e.g.
    # The board above should yield
    # {A: [(0,0),(0,1),...,(1,0)],...,F: [(2,5),(3,3)...(5,5)]}
    # After building a library each library value translates to a scope
    # in the variable list
    #parkcons = []
    # print(csp.get_all_vars())
    for e in parknames:
        parkscope = [v_board[tup[0]][tup[1]] for tup in parks[e]]
        cons.append(Constraint("ParkCon-{}".format(e),parkscope,'o',numtree))
    # Impose row constraints
    #row_cons = []
    row_n = 0
    for k in v_board:
        rowscope = k
        row_n += 1
        cons.append(Constraint("RowCon-{}".format(row_n),rowscope,'o',numtree))
    # Impose column constraints
    #col_cons = []
    col_n = 0
    for aa in range(len(v_board)):
        colscope = []
        for bb in range(len(v_board)):
            colscope.append(v_board[bb][col_n])
        cons.append(Constraint("ColCon-{}".format(col_n),colscope,'o',numtree))
        col_n+=1
    #Impose adjacency constraints for each pair of ajdacent grids
    for i in range(len(v_board)):
            for j in range(len(v_board)):
                if j<len(v_board)-1:
                    cons.append(Constraint(
                    "ADCONS{}{}".format(i,j),[v_board[i][j],
                                              v_board[i][j+1]],'a',numtree))
                if i<len(v_board)-1:
                    cons.append(Constraint(
                    "ADCONS{}{}".format(i,j),[v_board[i][j],
                                              v_board[i+1][j]],'a',numtree))

                if i<len(v_board)-1 and j<len(v_board)-1:
                    cons.append(Constraint(
                    "ADCONS{}{}".format(i,j),[v_board[i][j],
                                              v_board[i+1][j+1]],'a',numtree))
                if i>0 and j<len(v_board)-1:
                    cons.append(Constraint(
                    "ADCONS{}{}".format(i,j),[v_board[i][j],
                                              v_board[i-1][j+1]],'a',numtree))
                
    for c in cons:
        csp.add_constraint(c)
    return csp, v_board
    