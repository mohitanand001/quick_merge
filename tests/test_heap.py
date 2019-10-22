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
    assert heap_obj.get_top_element() == expected

@pytest.mark.parametrize("test_input", [[]])
def test_get_top_element_raises(test_input):
    with pytest.raises(IndexError, ):
        heap_obj = Heap()
        heap_obj.build_heap(test_input)
        heap_obj.get_top_element()


@pytest.mark.parametrize("test_input", [[1, 2, 3, 5],
                                        [4, 6, 0, 1],
                                         [-1, 2, 0, 12], 
                                         [0, 1, 3, 54, -12, -43, 21, ],
                                         [],]
                                         )
def test_heap_sort(test_input):
    heap_obj = Heap()
    heap_obj.build_heap(test_input)
    assert heap_obj.heap_sort() == sorted(test_input, reverse=True)

