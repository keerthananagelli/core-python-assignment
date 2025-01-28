def calculate_average(marks):
    """Calculate the average marks for each student."""
    return sum(marks) / len(marks)


def find_top_performer(students):
    """Find the student with the highest average marks."""
    averages = {student: calculate_average(marks) for student, marks in students.items()}
    top_student = max(averages, key=averages.get)
    return averages, top_student


# Example usage
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages, top_student = find_top_performer(students)
print("Average Marks:", averages)
print("Top Performer:", top_student)
