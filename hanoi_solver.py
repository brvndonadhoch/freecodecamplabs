def hanoi_solver(number):
    moves = []
    
    rods = [
        list(range(number, 0, -1)),#rod1
        [],#rod2
        [],#rod3
    ]

    moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(n, source, target, auxillary):
        if n == 0:
            return
        move_disks(n-1, source, auxillary, target)

        disk = rods[source].pop()
        rods[target].append(disk)

        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
        
        move_disks(n - 1, auxillary, target, source)

    
    move_disks(number, 0, 2, 1)    
    return"\n".join(moves)