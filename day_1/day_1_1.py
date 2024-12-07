"""
Proposed solution for advent of code 2024 day 1
"""
from typing import List

# Read data
def obtain_id_lists(file_path: str, sep: str) -> tuple[list[int], list[int]]:
    """
    Reads a list of integers from a file

    Args:
        file_path: Path to the file

    Returns:
        list: List of integers
    """
    int_input = []
    with open(file_path, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(sep)
            elements = [int(element.strip().replace("\n", "")) for element in elements]
            int_input.append(elements)

    list_1 = [element[0] for element in int_input]
    list_2 = [element[1] for element in int_input]

    return list_1, list_2

def obtain_total_distance(list_1: List[int], list_2: List[int]) -> List[int]:
    """
    Obtains the total distance between the two lists

    Args:
        list_1: List of integers
        list_2: List of integers

    Returns:
        list: List of integers
    """
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    total_distance = [abs(sorted_list_1[i] - sorted_list_2[i]) for i in range(len(list_1))]

    return sum(total_distance)

# Sort data
l1, l2 = obtain_id_lists(r"C:\Users\uif72896\Desktop\AoC_2024\day_1\input.txt", "   ")
result = obtain_total_distance(l1, l2)
print(result)