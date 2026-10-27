CLEAN = "Clean"
DIRTY = "Dirty"


def vacuum_agent(location, status_a, status_b):
    """Simple reflex agent: returns SUCK, LEFT, RIGHT or NO-OP."""
    if location == "A" and status_a == DIRTY:
        return "SUCK"
    elif location == "B" and status_b == DIRTY:
        return "SUCK"
    elif status_a == DIRTY:
        return "LEFT"
    elif status_b == DIRTY:
        return "RIGHT"
    else:
        return "NO-OP"


def vacuum_simulation(location, status_a, status_b):
    step = 0
    print(f"\nInitial state -> Location: {location}, Room A: {status_a}, Room B: {status_b}\n")

    while True:
        action = vacuum_agent(location, status_a, status_b)
        if action == "NO-OP":
            print(f"Action: NO-OP (both rooms are clean, stopping)")
            break

        if action == "SUCK" and location == "A":
            status_a = CLEAN
        elif action == "SUCK" and location == "B":
            status_b = CLEAN
        elif action == "LEFT":
            location = "A"
        elif action == "RIGHT":
            location = "B"

        step += 1
        print(f"Step {step}: Action: {action:<5} -> Location: {location}, "
              f"Room A: {status_a}, Room B: {status_b}")

    print(f"\nFinal state -> Location: {location}, Room A: {status_a}, Room B: {status_b}")
    print(f"Total actions performed (excluding NO-OP): {step}")


def read_location(prompt):
    while True:
        value = input(prompt).strip().upper()
        if value in ("A", "B"):
            return value
        print("  Please enter A or B.")


def read_status(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("clean", "c"):
            return CLEAN
        if value in ("dirty", "d"):
            return DIRTY
        print("  Please enter Clean or Dirty (or C / D).")


def main():
    test_no = 1
    while True:
        print(f"\n===== Test Case {test_no} =====")
        location = read_location("Initial Location (A/B)       : ")
        status_a = read_status("Room A (Clean/Dirty)         : ")
        status_b = read_status("Room B (Clean/Dirty)         : ")

        vacuum_simulation(location, status_a, status_b)

        again = input("\nRun another test case? (y/n): ").strip().lower()
        if again != "y":
            break
        test_no += 1


if __name__ == "__main__":
    main()
