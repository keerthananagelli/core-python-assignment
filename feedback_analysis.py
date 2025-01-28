def calculate_positive_feedback_percentage(ratings):
    """Calculate the percentage of positive feedback (ratings 4 or 5)."""
    if not ratings:
        return "No ratings available."
    positive_count = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.2f}%"


# Example usage
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(calculate_positive_feedback_percentage(ratings))
