def check_statement(p, q, r):
    """
    Check and categorize the logical nature of expressions as tautology, contradiction, or contingency.
    
    Parameters:
    p, q, r : bool
        Boolean variables used in logical expressions.

    Description:
    The function evaluates three expressions:
    1. A tautology: An expression that is always true.
    2. A contradiction: An expression that is always false.
    3. A contingency: An expression that is sometimes true and sometimes false.

    It prints the nature of each expression based on the evaluations.
    """
    # Expression for Tautology (always true)
    tautology_expr = (p or not p)
    # Expression for Contradiction (always false)
    contradiction_expr = (p and not p)
    # Expression for Contingency (sometimes true, sometimes false)
    contingency_expr = (p and q) or r

    # Evaluate and print the results
    print("Tautology (always true):", tautology_expr)
    print("Contradiction (always false):", contradiction_expr)
    print("Contingency (sometimes true, sometimes false):", contingency_expr)

# Example usage:
# Test with all combinations of True and False for p, q, and r
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            print(f"\nEvaluating for p={p}, q={q}, r={r}:")
            check_statement(p, q, r)
