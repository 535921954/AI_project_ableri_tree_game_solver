#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

'''
This file will contain different constraint propagators to be used within
bt_search.

propagator == a function with the following template
    propagator(csp, newly_instantiated_variable=None)
        ==> returns (True/False, [(Variable, Value), (Variable, Value) ...])

    csp is a CSP object---the propagator can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    newly_instaniated_variable is an optional argument.
    if newly_instantiated_variable is not None:
        then newly_instantiated_variable is the most
        recently assigned variable of the search.
    else:
        propagator is called before any assignments are made
        in which case it must decide what processing to do
        prior to any variables being assigned. SEE BELOW

    The propagator returns True/False and a list of (Variable, Value) pairs.

    Returns False if a deadend has been detected by the propagator.
        in this case bt_search will backtrack
    Returns True if we can continue.

    The list of variable values pairs are all of the values
    the propagator pruned (using the variable's prune_value method).
    bt_search NEEDS to know this in order to correctly restore these
    values when it undoes a variable assignment.

    NOTE propagator SHOULD NOT prune a value that has already been
    pruned! Nor should it prune a value twice

    PROPAGATOR called with newly_instantiated_variable = None
        PROCESSING REQUIRED:
            for plain backtracking (where we only check fully instantiated
            constraints) we do nothing...return (true, [])

            for forward checking (where we only check constraints with one
            remaining variable) we look for unary constraints of the csp
            (constraints whose scope contains only one variable) and we
            forward_check these constraints.

            for gac we establish initial GAC by initializing the GAC queue with
            all constaints of the csp

    PROPAGATOR called with newly_instantiated_variable = a variable V
        PROCESSING REQUIRED:
            for plain backtracking we check all constraints with V (see csp
            method get_cons_with_var) that are fully assigned.

            for forward checking we forward check all constraints with V that
            have one unassigned variable left

            for gac we initialize the GAC queue with all constraints containing
            V.
'''

from cspbase import *

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''Do forward checking.  That is, check constraints with only one
    uninstantiated variable, and prune appropriately.  (i.e., do not prune a
    value that has already been pruned; do not prune the same value twice.)
    Return if a deadend has been detected, and return the variable/value pairs
    that have been pruned.  See beginning of this file for complete description
    of what propagator functions should take as input and return.

    Input: csp, (optional) newVar.
        csp is a CSP object---the propagator uses this to
        access the variables and constraints.

        newVar is an optional argument.
        if newVar is not None:
            then newVar is the most recently assigned variable of the search.
            run FC on all constraints that contain newVar.
        else:
            propagator is called before any assignments are made in which case
            it must decide what processing to do prior to any variable
            assignment.

    Returns: (boolean,list) tuple, where list is a list of tuples:
             (True/False, [(Variable, Value), (Variable, Value), ... ])

        boolean is False if a deadend has been detected, and True otherwise.

        list is a set of variable/value pairs that are all of the values the
        propagator pruned.
    '''

#IMPLEMENT
    prune_list = []
    constraints = []

    if newVar is not None:
        constraints = csp.get_cons_with_var(newVar)
    else:
        constraints = csp.get_all_cons()
    for c in constraints:
        # Find constraint with only one uninstantiated variable
        if c.get_n_unasgn() == 1:
            # Get the uninstantiated variable
            var = c.get_unasgn_vars()[0]
            # Get its current domain
            curdom = var.cur_domain()
            for d in curdom:
                # Try to assign value d to variable
                var.assign(d)
                # Check if assigning d to var violates c
                vals = []
                vars = c.get_scope()
                for asvar in vars:
                    vals.append(asvar.get_assigned_value())
                if not c.check(vals):
                    if var.in_cur_domain(d):
                        prune_list.append((var, d))
                        var.prune_value(d)
                # Undo assignment
                var.unassign()
            # If the domain of d is wiped out, a deadend is found
            if not var.cur_domain():
                return False, prune_list
    # If checking on all constraints pass, we succeed.
    return True, prune_list

def prop_GAC(csp, newVar=None):
    '''Do GAC propagation, as described in lecture. See beginning of this file
    for complete description of what propagator functions should take as input
    and return.

    Input: csp, (optional) newVar.
        csp is a CSP object---the propagator uses this to access the variables
        and constraints.

        newVar is an optional argument.
        if newVar is not None:
            do GAC enforce with constraints containing newVar on the GAC queue.
        else:
            Do initial GAC enforce, processing all constraints.

    Returns: (boolean,list) tuple, where list is a list of tuples:
             (True/False, [(Variable, Value), (Variable, Value), ... ])

    boolean is False if a deadend has been detected, and True otherwise.

    list is a set of variable/value pairs that are all of the values the
    propagator pruned.
    '''

#IMPLEMENT
    constraints = []
    prune_list = []

    if newVar is not None:
        constraints = csp.get_cons_with_var(newVar)
    else:
        constraints = csp.get_all_cons()
    while constraints:
        c = constraints.pop()
        # Get list of unasigned variables
        vars = c.get_unasgn_vars()
        # For each unasigned variable check its GAC
        for var in vars:
            curdom = var.cur_domain()
            for d in curdom:
                # Try assigning d to variable
                # var.assign(d)
                # Do GAC check on assignment
                if not c.has_support(var, d):
                    if var.in_cur_domain(d):
                        prune_list.append((var, d))
                        var.prune_value(d)
                        for newcon in csp.get_cons_with_var(var):
                            if not newcon in constraints:
                                constraints.append(newcon)
            # If variable domain is emptied, a deadend is reached
            if not var.cur_domain():
                return False, prune_list


    # If check on all variables in all constraints pass, return True
    return True, prune_list


def prop_alberi(csp, newVar=None):
    """
    Due to the nature of this puzzle, we can make the row/column/park
    constraints filled as soon as the total number of trees in a constraint
    reaches the global variable numtree.
    """
    # prepare a list for constraints and a list for pruned values
    constraints = []
    prune_list = []
    
    # for each constraint affected by this newVar, put the constraint in
    # the list. If there is no new variable, put all constraints in the list
    if newVar is not None:
        constraints = csp.get_cons_with_var(newVar)
    else:
        constraints = csp.get_all_cons()


    # Then all constraints are dealt as follows:
    while constraints:
        c = constraints.pop()
        # Get list of unasigned variables
        # If the constraint is of type o and new assigned value is 1
        # Add all assigned values up. If it reaches numtree, then prune "1" from
        # all unassigned values in the constraint. Then add all affected constraints
        # to the constraint list like in GAC. If DWO, return false and pruned list
        # Otherwise, do nothing.
        # Do GAC
        if c.get_type() == 'o' and newVar and newVar.get_assigned_value() == 1:
            curval = 0
            for var in c.get_scope():
                if var.is_assigned():
                    curval += var.get_assigned_value()
            if curval == c.numtree:
                unasign_vars = c.get_unasgn_vars()
                for var in unasign_vars:
                    if var.in_cur_domain(1):
                        prune_list.append((var, 1))
                        var.prune_value(1)
                        for newcon in csp.get_cons_with_var(var):
                            if not newcon in constraints:
                                constraints.append(newcon)
                # If variable domain is emptied, a deadend is reached
                if not var.cur_domain():
                    return False, prune_list
        else:
            # Otherwise, do GAC
            vars = c.get_unasgn_vars()
            # For each unasigned variable check its GAC
            for var in vars:
                curdom = var.cur_domain()
                for d in curdom:
                    # Try assigning d to variable
                    # var.assign(d)
                    # Do GAC check on assignment
                    if not c.has_support(var, d):
                        if var.in_cur_domain(d):
                            prune_list.append((var, d))
                            var.prune_value(d)
                            for newcon in csp.get_cons_with_var(var):
                                if not newcon in constraints:
                                    constraints.append(newcon)
                # If variable domain is emptied, a deadend is reached
                if not var.cur_domain():
                    return False, prune_list

    # If check on all variables in all constraints pass, return True
    return True, prune_list