"""
Proposed solution for advent of code 2024 day 2: Part 1
"""
import pathlib
from typing import List


def obtain_reports_levels(file_name: str, sep: str) -> List[List[int]]:
    """
    Reads a list of integers from a file

    Args:
        file_path: Path to the file

    Returns:
        list: Matrix-like list that contains levels for each report
    """
    matrix: list = []
    absolute_path: str = pathlib.Path(__file__).parent.resolve()
    full_file_path: str = absolute_path.joinpath(file_name)
    with open(full_file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(sep)
            elements = [int(element.strip().replace("\n", "")) for element in elements]
            matrix.append(elements)

    return matrix

def obtain_number_of_safe_reports(matrix: List[List[int]]) -> int:
    """
    Obtain the number of safe reports

    Args:
        matrix (List[List[int]]): Matrix that contains reports and levels

    Returns:
        int: Number of safe reports
    """
    # Initialize variables
    safe_reports: list = []

    # Check elements
    for element in matrix:
        check_sort = _is_correctly_sorted(element)
        check_diff = _is_valid_diff(element)
        verdict = check_sort and check_diff
        safe_reports.append(verdict)
    
    return sum(safe_reports)


def _is_correctly_sorted(report: List[int]) -> bool:
    # Initializing variables
    iterations = len(report) - 1
    
    # Ascending
    c_asc = 0
    for i in range(iterations):
        if report[i] < report[i+1]:
            c_asc += 1
    ascending: bool = iterations == c_asc
    
    # Descending
    c_desc = 0
    for i in range(iterations):
        if report[i] > report[i+1]:
            c_desc += 1
    descending: bool = iterations == c_desc

    # Obtaing verdict
    return descending or ascending

def _is_valid_diff(report: List[int]) -> bool:
    # Initialize variables
    iterations: int = len(report) - 1

    # Check diff
    for i in range(iterations):
        diff = abs(report[i] - report[i+1])
        if 1 < diff > 3:
            return False
    
    return True
    

if __name__ == "__main__":
    matrix = obtain_reports_levels("input.txt", " ")
    result = obtain_number_of_safe_reports(matrix)
    print(result)