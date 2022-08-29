'''
猶記得申請 CMU 時做過這個題目
'''


def solution(N, S, T):
    # intial map has 0 in all cells -- this may not be necessary
    # if we do not check the boundries for ships and attackes
    battle_field = [[0 for i in range(N)] for j in range(N)]

    # compute all ship areas
    ship_zones = place_ships(S)
    # compute all attack cells
    attacked_cells = attack(T)

    result = check_damage(ship_zones, attacked_cells)
    return result


def check_damage(ship_zones, attacked_cells):
    sunk_count = 0
    hit_count = 0

    for zone in ship_zones:
        top_left = zone[0]
        bottom_right = zone[1]

        # check sunk
        # if all cells for a ship are included in the attaecked cell, then sunk
        is_sunk = True
        for x in range(top_left[0], bottom_right[0]+1):
            for y in range(top_left[1], bottom_right[1]+1):
                is_sunk = is_sunk and ((x, y) in attacked_cells)

        if is_sunk:
            sunk_count += 1

        # check hit
        # if a cell is hit, append 1 to the status list
        # if a cell is not hit, then append 0
        status = []
        for x in range(top_left[0], bottom_right[0]+1):
            for y in range(top_left[1], bottom_right[1]+1):
                if (x, y) in attacked_cells:
                    status.append(1)
                else:
                    status.append(0)

        if 0 in status and 1 in status:
            hit_count += 1

    return f'{sunk_count},{hit_count}'


def place_ships(S):
    ships = S.split(',')

    # a list of ship zones
    # each ship zone is defined by the top-left and bottom-right cells
    ship_zones = []
    for ship in ships:
        coor = ship.split(' ')
        top_left = [int(coor[0][0]) - 1, ord(coor[0][1]) - ord('A')]
        bottom_right = [int(coor[1][0]) - 1, ord(coor[1][1]) - ord('A')]

        ship_zones.append((top_left, bottom_right))

    return ship_zones


def attack(T):
    if not T:
        return []

    marks = T.split(' ')

    attacked_cells = []
    for coor in marks:
        x = int(coor[0]) - 1
        y = int(ord(coor[1]) - ord('A'))
        attacked_cells.append((x, y))

    return attacked_cells


# ----------------------------------- Test ---------------------------------
N = 4
S = "1B 2C,2D 4D"
T = "2B 2D 3D 4D 4A"
expected = "1,1"
assert solution(N, S, T) == expected

N = 4
S = "1B 2C,2D 4D"
T = "1B 1C 2B 2C 2D 3D 4D 4A"
expected = "2,0"
assert solution(N, S, T) == expected

N = 3
S = "1A 1B,2C 2C"
T = "1B"
expected = "0,1"
assert solution(N, S, T) == expected


N = 12
S = "1A 2A,12A 12A"
T = "12A"
expected = "1,0"
assert solution(N, S, T) == expected

print('All tests have passed.')
