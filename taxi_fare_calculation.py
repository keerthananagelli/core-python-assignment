def calculate_fare(distance):
    """Calculate the total fare for a trip."""
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare


def calculate_total_fare(trips):
    """Calculate the total fare for all trips."""
    total_fare = 0
    for i, trip in enumerate(trips, start=1):
        fare = calculate_fare(trip)
        total_fare += fare
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total_fare}")


# Example usage
trips = [5, 10, 3]
calculate_total_fare(trips)
