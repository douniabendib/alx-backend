#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function named index_range that
    takes two integer arguments page
    and page_size
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
