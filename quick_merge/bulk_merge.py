from functools import reduce
import os

import numpy as np
import pandas as pd

from quick_merge.heap import Heap


class QuickMerge:
    """Performs full outer join(merge) of large number of
    dataframes in an optimized manner. The algorithm capitalizes
    on the fact that full outer joins(merge) is both commutative
    and associative.
    :param container: Container of dataframes
    :type container: List[pandas.core.frame.DataFrame]
    :param merge_key: The key to be indexed by which we have to merge the dataframes.
    :type merge_key: str, optional
    """
    def __init__(self, container, key=None):
        self.container = container.copy()
        self.merge_key = key

    def index_dataframes_util(self):
        """Utility function for indexing the dataframe by
        `key`.
        :raises KeyError: Raises a KeyError when trying to set_index on a column that does
        not exist. 
        """
        if self.merge_key is not None:
            self.container = [df.set_index(self.merge_key, inplace=True) for df in self.container]


    def quick_merge_util(self, hp_obj):
        """Maintains a heap of dataframes, constantly
        merges(outer) two smallest dataframes and keeps
        on adding it to the heap.
        :param hp_obj: object of :class:`Heap`
        :return: A pandas Dataframe having the merged(outer) data.
        :rtype: pandas.core.frame.DataFrame
         """

        while hp_obj.get_size() > 1:
            curr_df_1 = hp_obj.pop_top_element()
            curr_df_2 = hp_obj.pop_top_element()
            merged_df = pd.merge(curr_df_1,
                                 curr_df_2,
                                 how="outer",
                                 left_index=True,
                                 right_index=True)
            hp_obj.insert_node(merged_df)

        return hp_obj.pop_top_element()

    def quick_merge_driver(self):
        """Driver function for creating `:class:Heap` object and 
        setting index on the list of dataframes. The `:class:Heap` is
        balanced in such a way that dataframe with minimum size is 
        at the top. Also calls `quick_merge_util` which does the merging(outer) 
        and returns the final merged dataframe.
        :return: A pandas Dataframe having the merged(outer) data.
        :rtype: pandas.core.frame.DataFrame
        """
        heap_obj = Heap(self.container, lambda x, y: x.size < y.size)
        heap_obj.build_heap()
        self.index_dataframes_util()
        return self.quick_merge_util(heap_obj)


def quick_merge_(dataframes=None, merge_key=None):
    q_merge_obj = QuickMerge(dataframes, merge_key, )
    res = q_merge_obj.quick_merge_driver()
    return res

if __name__ == "__main__":
    pass