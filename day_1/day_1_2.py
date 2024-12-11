"""
Proposed solution for advent of code 2024 day 1: Part 2
"""

import pathlib
from typing import List


def obtain_id_lists(file_name: str, sep: str) -> tuple[List[int], List[int]]:
    """
    Reads a list of integers from a file

    Args:
        file_path: Path to the file

    Returns:
        tuple: List of integers
    """
    int_input: list = []
    absolute_path: str = pathlib.Path(__file__).parent.resolve()
    full_file_path: str = absolute_path.joinpath(file_name)
    with open(full_file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(sep)
            elements = [int(element.strip().replace("\n", "")) for element in elements]
            int_input.append(elements)

    left_list = [element[0] for element in int_input]
    right_list = [element[1] for element in int_input]

    return left_list, right_list


def obtain_similarity_score(left_list: List[int], right_list: List[int]) -> int:
    """
    Obtains the total distance between the two lists

    Args:
        left_list: List of ids
        right_list: List of appeareances of the ids

    Returns:
        int: calculated similarity score
    """
    result: int = 0
    
    for element in left_list:
        result += element * right_list.count(element)
    
    return result


if __name__ == "__main__":
    ll, rl = obtain_id_lists(r"input.txt", "   ")
    result = obtain_similarity_score(ll, rl)
    print(result)
