import copy
import os
import sys

import pandas as pd
import pytest

from quick_merge import quick_merge_
from quick_merge.heap import Heap

df_1 = pd.DataFrame(
    data={"A": [1, 2, 3, 4], "B": [43, 54, 67, 23], "C": [43, 56, 89, 12]}
)
df_2 = pd.DataFrame(data={"A": [4, 5, 1, 6], "D": [334, 34, 56, 12]})
df_3 = pd.DataFrame(
    data={"A": [12, 1, 3, 4], "E": [12, 54, 56, 67], "F": [34, 56, 34, 12]}
)
dfs_qm = [df_1, df_2, df_3]

dfs_brute = copy.deepcopy(dfs_qm)


@pytest.mark.parametrize("quick_merge_input, brute_input", [(dfs_qm, dfs_brute)])
def test_bulk_merge_on_frames(quick_merge_input, brute_input):
    merged_qm = quick_merge_(dataframes=quick_merge_input, merge_key="A")

    for df_c in brute_input:
        df_c.set_index("A", inplace=True)

    merged_brute = dfs_brute[0]
    for df in dfs_brute[1:]:
        merged_brute = pd.merge(
            merged_brute, df, how="outer", left_index=True, right_index=True
        )

    merged_brute.fillna(0, inplace=True)
    merged_qm.fillna(0, inplace=True)

    # print(merged_brute.equals(merged_qm))
    pd.testing.assert_frame_equal(merged_brute, merged_qm)
