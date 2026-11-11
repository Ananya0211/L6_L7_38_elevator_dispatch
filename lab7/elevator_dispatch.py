def parse_request(text):
    if not isinstance(text, str):
        return None
    parts = text.split('->')
    if len(parts) != 2:
        return None
    try:
        start = int(parts[0].strip())
        end = int(parts[1].strip())
        return start, end
    except (ValueError, OverflowError):
        return None


def total_travel(floors_csv):
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        return 0
    try:
        floors = [int(f.strip()) for f in floors_csv.split(',') if f.strip()]
        if len(floors) < 2:
            return 0
        return sum(abs(floors[i + 1] - floors[i]) for i in range(len(floors) - 1))
    except (ValueError, OverflowError):
        return 0


def load_percent(text):
    if not isinstance(text, str):
        return None
    parts = text.split(' of ')
    if len(parts) != 2:
        return None
    try:
        load = int(parts[0].strip())
        capacity = int(parts[1].strip())
        if capacity <= 0:
            return None
        return (load * 100) // capacity
    except (ValueError, OverflowError, ZeroDivisionError):
        return None


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result)


if __name__ == "__main__":
    main()