from sympy.logic.boolalg import to_cnf, And, Or

# Check if the belief base entails the formula entered
def check_entailment (base, formula):

    clauses = []
    formula_cnf = to_cnf(formula)

    for belief in base:
        belief_cnf = to_cnf(belief.formula)

        if isinstance(belief_cnf, And):
                clauses += list(belief_cnf.args)
        else:
            clauses.append(belief_cnf)

    # Add the negation of the desired formula
    clauses += dissociate(to_cnf(~formula_cnf))

    # Initial check for an empty clause
    if False in clauses:
        return True
    
    result = set()

    while True:
        n = len(clauses)
        clause_pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]

        for clause_i, clause_j in clause_pairs:
            resolved = resolve(clause_i, clause_j)

            # If an empty clause it is obtained
            if False in resolved:
                return True
            
            result = result.union(set(resolved))

        if result.issubset(set(clauses)):
            return False
        
        for result_cl in result:
            if result_cl not in clauses:
                clauses.append(result_cl)

# Implement the PL-Resolution algorithm
def resolve(clause_i, clause_j):

    clauses = []

    d_clause_i = dissociate(clause_i)
    d_clause_j = dissociate(clause_j)

    for i in d_clause_i:
        for j in d_clause_j:

            # If a contradiction it is found, all literals involved are removed
            if i == ~j or ~i == j:
                cleaned_clause = remove_literal(i, d_clause_i) + remove_literal(j, d_clause_j)
                cleaned_clause = list(set(cleaned_clause))

                # Join the resulting clause in belief base
                if len(cleaned_clause) == 0:
                    clauses.append(False)
                elif (len(cleaned_clause)) == 1:
                    clauses.append(cleaned_clause[0])
                else:
                    clauses.append(Or(*cleaned_clause))
    return clauses

# Prepare every clause for PL-Resolution algorithm
def dissociate(formula):
    if len(list(formula.args)) < 2:
        return [formula]
    else:
        return list(formula.args)
    
# Delete a literal from a clause
def remove_literal(literal, clause):
    return [l for l in clause if l != literal]
