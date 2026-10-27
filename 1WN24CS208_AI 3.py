CUTOFF = "cutoff"
FAILURE = "failure"


def depth_limited_search(node, goal, graph, limit, path):
    """Recursive DLS. Returns a path (list), CUTOFF, or FAILURE."""
    if node == goal:
        return path + [node]
    if limit == 0:
        return CUTOFF

    cutoff_occurred = False
    for child in graph.get(node, []):
        if child not in path:  # avoid revisiting states on the current path
            result = depth_limited_search(child, goal, graph, limit - 1, path + [node])
            if isinstance(result, list):  # solution found
                return result
            if result == CUTOFF:
                cutoff_occurred = True

    return CUTOFF if cutoff_occurred else FAILURE


def iterative_deepening_search(initial, goal, graph, maximum_depth, initial_depth=0):
    """Returns (path, depth) if found, otherwise (None, None)."""
    for depth in range(initial_depth, maximum_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, [])
        if isinstance(result, list):
            return result, depth
    return None, None


def read_graph():
    """Read lines like 'A: B, C' (use '-' or nothing for no children).
    A blank line ends the input."""
    graph = {}
    print("Enter the search tree, one node per line (e.g.  A: B, C  or  B: -).")
    print("Press Enter on an empty line when done.")
    while True:
        line = input("  ").strip()
        if not line:
            break
        if ":" not in line:
            print("  Invalid line, use the format  NODE: CHILD1, CHILD2")
            continue
        node, children = line.split(":", 1)
        node = node.strip()
        children = [c.strip() for c in children.split(",")]
        graph[node] = [c for c in children if c and c != "-"]
    return graph


def run_test():
    initial = input("Initial State : ").strip()
    goal = input("Goal State    : ").strip()
    while True:
        try:
            raw = input("Initial Depth Limit (press Enter for 0): ").strip()
            initial_depth = int(raw) if raw else 0
            max_depth = int(input("Maximum Depth : ").strip())
            if initial_depth < 0 or initial_depth > max_depth:
                print("  Initial depth must be between 0 and the maximum depth.")
                continue
            break
        except ValueError:
            print("  Please enter whole numbers.")
    graph = read_graph()

    path, depth = iterative_deepening_search(initial, goal, graph, max_depth, initial_depth)
    print("\n--- Result ---")
    if path:
        print(f"Goal found at depth {depth}")
        print(f"Solution Path : {' -> '.join(path)}")
    else:
        print(f"Goal not found for depth limits {initial_depth} to {max_depth}")


def main():
    test_no = 1
    while True:
        print(f"\n===== Test Case {test_no} =====")
        run_test()
        again = input("\nRun another test case? (y/n): ").strip().lower()
        if again != "y":
            break
        test_no += 1


if __name__ == "__main__":
    main()

