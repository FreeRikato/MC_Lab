def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    """
    Solve the Tower of Hanoi problem

    Parameters:
    n : int
        Number of disks
    from_rod : str
        The initial rod where all disks are placed initially
    to_rod : str
        The target rod where all disks need to be moved
    aux_rod : str
        The auxiliary rod used in the process of moving disks

    Description:
    The function recursively moves the disks between the rods.
    The problem is divided into smaller problems:
    1. Move n-1 disks from the source to auxiliary rod.
    2. Move the nth disk from source to target rod.
    3. Move the n-1 disks from auxiliary to target rod.
    """
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

# Example usage:
# Move 3 disks from rod A to rod C using rod B as auxiliary
tower_of_hanoi(3, 'A', 'C', 'B ')