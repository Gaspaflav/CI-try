"""
Solution Module for Gold Collection Problem
Student ID: 339228

This module contains the main solution function that solves the gold collection problem
using an adaptive hybrid algorithm combining Genetic Algorithm and Hill Climbing.
"""

from src.solver import adaptive_solver, conversion_solution


def solution(p):
    """
    Solve the gold collection problem instance.
    
    Args:
        p: Problem instance with graph, parameters (alpha, beta, density), 
           and methods (cost, baseline, graph properties)
    
    Returns:
        List of (node, gold_amount) tuples representing the solution path
    """
    # Call the adaptive solver to find best path and trip counts
    best_path, optimized_trip_counts, final_cost = adaptive_solver(p)
    
    # Convert internal representation to output format
    converted_solution = conversion_solution(p, best_path, optimized_trip_counts)
    
    return converted_solution
