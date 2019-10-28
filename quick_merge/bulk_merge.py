from functools import reduce
import os

import numpy as np
import pandas as pd

from quick_merge.heap import Heap


class QuickMerge:
    def __init__(self, container, key, custom_comp=None):
        self.container = container
        self.custom_comp = custom_comp
        self.merge_key = key

    def quick_merge_util(self, hp_obj):
        # for _ in range(4):
        #     print(hp_obj.pop_top_element(),)
        # print(hp_obj.heap_sort())
        # cnt = 0
        while hp_obj.get_size() > 1:
            curr_df_1 = hp_obj.pop_top_element()
            curr_df_2 = hp_obj.pop_top_element()

            print(curr_df_1.size, curr_df_2.size, hp_obj.get_size())

            merged_df = pd.merge(curr_df_1, curr_df_2, on=self.merge_key, how="outer")
            hp_obj.insert_node(merged_df)

        return hp_obj.pop_top_element()

    def quick_merge_driver(self):
        heap_obj = Heap(self.container, self.custom_comp)
        heap_obj.build_heap()
        # print(self.container)

        return self.quick_merge_util(heap_obj)


def quick_merge(dataframes=None, merge_key=None, comparator=None):
    q_merge_obj = QuickMerge(dataframes, merge_key, comparator)
    res = q_merge_obj.quick_merge_driver()
    return res

if __name__ == "__main__":
    base_dir = '/Users/mohitanand/quick_merge/files'
    files = os.listdir(base_dir)
    files.sort()
    print('sorted')
    dfs = [pd.read_csv(os.path.join(base_dir, file_), index_col='A') for file_ in files]
    print('read')
    # df_ = quick_merge(dfs, 'A', lambda x, y: x.size < y.size)
    # print(df_.shape)
    df_final = reduce(lambda left,right: pd.merge(left,right, on='A', left_index=True, right_index=True, how='outer'), dfs)


    # df_1 = pd.DataFrame(
    #     np.random.randint(0, 100, size=(100, 6)), columns=list("ABCDEF")
    # )
    # df_2 = pd.DataFrame(
    #     np.random.randint(0, 100, size=(100, 9)), columns=list("ABCDEFGHI")
    # )
    # df_3 = pd.DataFrame(np.random.randint(0, 100, size=(100, 3)), columns=list("ABC"))

    # A = [df_1, df_2, df_3]
    # q_merge_obj = QuickMerge(A, "A", lambda x, y: x.size < y.size)
    # print(q_merge_obj.quick_merge_driver().head())

    # q_o = QuickMerge([3, 2, 1, 5], lambda x,y: x < y)
    # q_o.quick_merge_driver()
