def relation1(p, q):
    """
    First relation: Logical AND
    Evaluates if both p and q are True.

    Parameters:
    p, q : bool
        Boolean variables.

    Returns:
    bool
        True if both p and q are True, False otherwise.
    """
    return p and q

def relation2(p, q):
    """
    Second relation: Using De Morgan's Law
    Evaluates the equivalence of NOT (NOT p OR NOT q) to p AND q.

    Parameters:
    p, q : bool
        Boolean variables.

    Returns:
    bool
        True if NOT (NOT p OR NOT q) holds, False otherwise.
    """
    return not (not p or not q)

def are_equivalent():
    """
    Check if the two logical relations are equivalent for all boolean combinations.

    Returns:
    bool
        True if the relations are equivalent for all combinations, False otherwise.
    """
    values = [True, False]
    for p in values:
        for q in values:
            if relation1(p, q) != relation2(p, q):
                return False
    return True

# Example usage:
equivalent = are_equivalent()
print(f"The relations are equivalent: {equivalent}")
