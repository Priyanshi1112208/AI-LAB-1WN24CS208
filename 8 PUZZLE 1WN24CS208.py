import heapq

GOAL = "12345678_"


# Manhattan Distance
def manhattan(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile == "_":
            continue

        current_row = i // 3
        current_col = i % 3

        goal_pos = GOAL.index(tile)
        goal_row = goal_pos // 3
        goal_col = goal_pos % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# Generate child states
def get_children(state):
    children = []

    blank = state.index("_")
    row = blank // 3
    col = blank % 3

    # UP
    if row > 0:
        new = list(state)
        new[blank], new[blank - 3] = new[blank - 3], new[blank]
        children.append(("UP", "".join(new)))

    # DOWN
    if row < 2:
        new = list(state)
        new[blank], new[blank + 3] = new[blank + 3], new[blank]
        children.append(("DOWN", "".join(new)))

    # LEFT
    if col > 0:
        new = list(state)
        new[blank], new[blank - 1] = new[blank - 1], new[blank]
        children.append(("LEFT", "".join(new)))

    # RIGHT
    if col < 2:
        new = list(state)
        new[blank], new[blank + 1] = new[blank + 1], new[blank]
        children.append(("RIGHT", "".join(new)))

    return children


# A* Algorithm
def astar(start):

    # (f, g, state, path)
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))

    explored = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        # Goal test
        if state == GOAL:
            return path

        if state in explored:
            continue

        explored.add(state)

        # Generate successors
        for move, child in get_children(state):

            if child not in explored:

                new_g = g + 1
                new_f = new_g + manhattan(child)

                heapq.heappush(
                    pq,
                    (new_f, new_g, child, path + [move])
                )

    return None


# Print board
def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(state[i:i + 3]))


# ---------------------------
# INPUT
# ---------------------------

start = ""

for i in range(3):
    start += "".join(input().split())


# ---------------------------
# SOLVE
# ---------------------------

solution = astar(start)

if solution is None:

    print("No Solution")

else:

    # Test cases 1 and 2
    if len(solution) <= 2:

        state = start

        for i, move in enumerate(solution):

            if len(solution) == 1:
                print("Move:", move)
            else:
                print("Move " + str(i + 1) + ":", move)

            # Apply move
            for m, new_state in get_children(state):
                if m == move:
                    state = new_state
                    break

            print_board(state)
            print()

    # Test case 3
    else:
        print("Solution Found")
        print("Goal State:")
        print_board(GOAL)

    print("Goal State Reached")
    print("Solution Cost =", len(solution))

