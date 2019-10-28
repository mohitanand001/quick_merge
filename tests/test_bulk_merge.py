import os
import sys

# sys.path.append((os.path.dirname(os.path.abspath(__file__))))

import pytest

from quick_merge.heap import Heap


@pytest.mark.parametrize("test_input", [[]])
def test_get_top_element_raises(test_input):
    with pytest.raises(IndexError):
        heap_obj = Heap(test_input)
        heap_obj.build_heap()
        heap_obj.get_top_element()
