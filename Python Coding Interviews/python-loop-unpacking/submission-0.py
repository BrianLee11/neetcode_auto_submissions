from typing import List, Tuple

def best_student(scores: List[Tuple[str, int]]) -> str:
    current_high_score = 0
    current_champion_name = ""

    for name, score in scores:
        if score > current_high_score:
            current_high_score = score
            current_champion_name = name

    return current_champion_name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
