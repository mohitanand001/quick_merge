import os

import numpy as np
import pandas as pd

from quick_merge.quick_merge.heap import Heap


class QuickMerge:
    def __init__(self, container, key, custom_comp=None):
        self.container = container
        self.custom_comp = custom_comp
        self.merge_key = key

    def quick_merge_util(self, hp_obj):
        while hp_obj.get_size() > 1:
            print(list(map(lambda x: x.size, self.container)))
            curr_df_1 = hp_obj.pop_top_element()
            curr_df_2 = hp_obj.pop_top_element()

            merged_df = pd.merge(curr_df_1, curr_df_2, on=self.merge_key, how="outer")
            hp_obj.insert_node(merged_df)

            return hp_obj.pop_top_element()

    def quick_merge_driver(self):
        heap_obj = Heap(self.container, self.custom_comp)
        heap_obj.build_heap()

        return self.quick_merge_util(heap_obj)


def quick_merge(dataframes=None, merge_key=None, comparator=None):
    q_merge_obj = QuickMerge(dataframes, merge_key, comparator)
    res = q_merge_obj.quick_merge_driver()
    return res


if __name__ == "__main__":

    df_1 = pd.DataFrame(
        np.random.randint(0, 100, size=(100, 6)), columns=list("ABCDEF")
    )
    df_2 = pd.DataFrame(
        np.random.randint(0, 100, size=(100, 9)), columns=list("ABCDEFGHI")
    )
    df_3 = pd.DataFrame(np.random.randint(0, 100, size=(100, 3)), columns=list("ABC"))

    A = [df_1, df_2, df_3]
    q_merge_obj = QuickMerge(A, "A", lambda x, y: x.size < y.size)
    print(q_merge_obj.quick_merge_driver().head())
