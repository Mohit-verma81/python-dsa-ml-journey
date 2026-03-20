def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return {
        "Total": total,
        "Average": average,
        "Highest": highest,
        "Lowest": lowest
    }


marks = [85, 90, 78, 92, 88]

result = analyze_marks(marks)

for key, value in result.items():
    print(f"{key}: {value}")