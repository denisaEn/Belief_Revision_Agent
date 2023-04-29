from sympy.logic.boolalg import to_cnf

def entailment (base, formula):

    clauses = []
    formula_cnf = to_cnf(formula)

    for belief in base:
        belief_cnf = to_cnf(belief.formula)

        if isinstance(belief_cnf, And):
                clauses += list(belief_cnf.args)
        else:
            clauses.append(belief_cnf)

    clauses += dissociate(to_cnf(~formula_cnf))

    if False in clauses:
        return True
    
    result = set()

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]

        for clause_i, clause_j in pairs:
            aux = resolve(clause_i, clause_j)
            if False in aux:
                return True
            
            result = result.union(set(aux))

        if result.issubset(set(clauses)):
            return False
        
        for result_cl in result:
            if result_cl not in clauses:
                clauses.append(result_cl)

def resolve(clause_i, clause_j):

    clauses = []

    d_clause_i = dissociate(clause_i)
    d_clause_j = dissociate(clause_j)

    for i in d_clause_i:
        for j in d_clause_j:
            if i == ~j or ~i == j:
                resolved = remove_literal(i, d_clause_i) + remove_literal(j, d_clause_j)
                resolved = list(set(resolved))

                if len(resolved) == 0:
                    clauses.append(False)
                elif (len(resolved)) == 1:
                    clauses.append(resolved[0])
                else:
                    clauses.append(Or(*resolved))
    return clauses

def dissociate(formula):
    if len(list(formula.args)) < 2:
        return [formula]
    else:
        return list(formula.args)
    

def remove_literal(literal, clause):
    return [l for l in clause if l != literal]
