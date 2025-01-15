#Write a recursive solution to the Tower of Hanoi puzzle for n disks.
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case: move one disk directly
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3, 'A', 'C', 'B')  # A, B, and C are the names of the rods