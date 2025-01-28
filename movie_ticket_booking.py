def get_available_seats(total_seats, booked_seats):
    """Return the list of available seats."""
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


def book_seat(booked_seats, seat):
    """Book a seat if it's not already booked."""
    if seat in booked_seats:
        return f"Seat {seat} is already booked."
    booked_seats.append(seat)
    return f"Seat {seat} booked successfully."


def cancel_seat(booked_seats, seat):
    """Cancel a booked seat."""
    if seat in booked_seats:
        booked_seats.remove(seat)
        return f"Seat {seat} canceled successfully."
    return f"Seat {seat} was not booked."


# Example usage
total_seats = 10
booked_seats = [2, 5, 7]
print("Available seats:", get_available_seats(total_seats, booked_seats))
print(book_seat(booked_seats, 3))
print(cancel_seat(booked_seats, 5))
