class Heap:
    """Custom Heap class which is used to find the max or min
       among a group of objects according to the comparator 
       function specified. If no comparator function is specified
       the class behaves as max_heap.
    """

    def __init__(self, ):
        self.heap_arr = []
        self.size = 0
        self.comprt = None


    def get_left_child_indx(self, node):
        """Returns the index of left child of node.
        """
        if 2 * node + 1 < self.size:
            return 2 * node + 1
        return None

    def get_right_child_indx(self, node):
        """Returns the index of the left child of node.
        """
        if 2 * node + 2 < self.size:
            return 2 * node + 2
        return None
    
    def get_top_element(self):
        """Returns the top element in the heap.
        """
        if self.size > 0:
            return self.heap_arr[0]
        raise IndexError('Cannot get top element from an empty heap.')

    def get_last_element(self):
        """Returns the last element in the heap.
        """
        if self.size > 0:
            return self.heap_arr[-1]
        raise IndexError('Cannot get last element from an empty heap.')

    def pop_top_element(self):
        """Returns top element, removes it from balances the heap."""

        if self.size <= 0:
            raise IndexError('Cannot pop from an empty heap.')

        last_element_indx = self.size - 1
        top_element_indx = 0
        top_element = self.heap_arr[0]

        self.swap_nodes(self.heap_arr, top_element_indx, last_element_indx)

        self.size = self.size - 1
        self.max_heapify(top_element_indx)

        return top_element

    def swap_nodes(self, arr, indx_1, indx_2):
        """Swap the value in the arr, with the given index inde_1, and indx_2.
        """
        arr[indx_1], arr[indx_2] = arr[indx_2], arr[indx_1]

    def max_heapify(self, node):
        """Max heapifies a tree, starting from a given node index.
        """
        
        left_child_indx = self.get_left_child_indx(node)
        right_child_indx = self.get_right_child_indx(node)
        largest_node_indx = node

        if left_child_indx is not None and self.heap_arr[left_child_indx] > self.heap_arr[largest_node_indx]:
            largest_node_indx = left_child_indx
        
        if right_child_indx is not None and self.heap_arr[right_child_indx] > self.heap_arr[largest_node_indx]:
            largest_node_indx = right_child_indx
        
        if largest_node_indx != node:
            self.swap_nodes(self.heap_arr, largest_node_indx, node)
            self.max_heapify(largest_node_indx)

    def build_heap(self, A):
        """Builds the heap from the collection.
        """

        begin_node, end_node = len(A) // 2, 0
        self.heap_arr = A.copy()
        self.size = len(A)

        for node in range(begin_node, end_node - 1, -1):
            self.max_heapify(node)

    def heap_sort(self):
        """Returns a sorted list. The heap exhausts (size becomes 0) after
        the heap_sort operation is performed.
        """
        sorted_list = []
        while(self.size > 0):
            sorted_list.append(self.pop_top_element())
        
        return sorted_list


if __name__ == "__main__":
    head_obj = Heap()
    head_obj.build_heap([3, -4, 1, 21, 2])
 
    print(head_obj.heap_sort())