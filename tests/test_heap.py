import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from src.heap import Heap

@pytest.mark.parametrize("test_input,expected", [ ([8, 1, 2, 4], 8),
                                                  ([1, 2, 5, 3], 5),
                                                  ([5], 5)] ) 
def test_get_top_element(test_input, expected):
    heap_obj = Heap()
    heap_obj.build_heap(test_input)
    assert heap_obj.get_top_element() == 1

