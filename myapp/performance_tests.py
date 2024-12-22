import time
from .qyery_tests import  get_books_without_optimization, get_books_with_optimization

def measure_performance():
    """Вимірювання часу для запиту без оптимізації"""
    start_time = time.time()
    get_books_without_optimization()
    print(f"Time without optimization: {time.time() - start_time:.2f} seconds")

    """Вимірювання часу для запиту з оптимізацією"""
    start_time = time.time()
    get_books_with_optimization()
    print(f"Time with optimization: {time.time() - start_time:.2f} seconds")
