import os

import pytest

from quick_merge.quick_merge.heap import Heap


@pytest.mark.parametrize("test_heap", [ [1, 2, 4, 5], [] ])
def test_get_size(test_heap,):
    heap_obj = Heap(test_heap)
    heap_obj.build_heap()
    assert heap_obj.get_size() == len(test_heap)



@pytest.mark.parametrize("test_heap,test_node", [
                                                 ([1, 2, 4, 6 ,10], 1),
                                                 ])
def test_get_left_child_indx(test_heap, test_node):
    heap_obj = Heap(test_heap)
    heap_obj.build_heap()
    assert heap_obj.get_left_child_indx(test_node) == 2 * test_node + 1


@pytest.mark.parametrize("test_heap,test_node", [
                                                 ([1, 2, 4, 6 ,10], 1),
                                                 ([1, 2, 3], 0)
                                                 ])
def test_get_right_child_indx(test_heap, test_node):
    heap_obj = Heap(test_heap)
    heap_obj.build_heap()
    assert heap_obj.get_right_child_indx(test_node) == 2 * test_node + 2




@pytest.mark.parametrize("test_input", [[8, 1, 2, 4],
                                        [1, 2, 5, 3],
                                        [5],] ) 
def test_get_top_element(test_input,):
    heap_obj_max = Heap(test_input, lambda x, y: x > y)
    heap_obj_max.build_heap()
    assert heap_obj_max.get_top_element() == max(test_input)

    heap_obj_min = Heap(test_input, lambda x, y: x < y)
    heap_obj_min.build_heap()
    assert heap_obj_min.get_top_element() == min(test_input)


@pytest.mark.parametrize("test_input", [[]])
def test_get_top_element_raises(test_input):
    with pytest.raises(IndexError, ):
        heap_obj = Heap(test_input)
        heap_obj.build_heap()
        heap_obj.get_top_element()


@pytest.mark.parametrize("test_input", [[1, 2, 54, 5, 2, -1, 21, 3], 
                                        [2], 
                                        [-1],
                                        [5,2,-1]
                                        ])
def test_heap_sort(test_input):
    heap_obj_max = Heap(test_input.copy(), lambda x, y: x > y)
    heap_obj_max.build_heap()
    assert heap_obj_max.heap_sort() == sorted(test_input, reverse=True)

    heap_obj_min = Heap(test_input.copy(), lambda x, y: x < y)
    heap_obj_min.build_heap()
    assert heap_obj_min.heap_sort() == sorted(test_input)
    

# @pytest.mark.parametrize("test_input", [[1, 2, 3, 5],
#                                         [4, 6, 0, 1],
#                                          [-1, 2, 0, 12], 
#                                          [0, 1, 3, 54, -12, -43, 21, ],
#                                          [],]
#                                          )
# def test_heap_sort(test_input):
#     heap_obj = Heap(test_input)
#     heap_obj.build_heap()
#     assert heap_obj.heap_sort() == sorted(test_input, reverse=True)

