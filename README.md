# quick_merge
A utility to `merge(full outer join or inner join)` large number of files in an optimized manner.The algorithm capitalizes on the fact that `full outer join` is `associative` as well as `commutative`, so the order of merging would not change the final result.

Let's say we have 100 files `(f1, f2, f3, .... f100)` all of them indexed by `id`, all of which needs to be merged together to form one consolidate file. Insetead of merging them one after the other in a loop, the quick_merge follows these steps.


1. Add all the files `f1, f2, f3, ... f100` to a heap(the datastructure).
2. Balance the heap, such that the top contains the one with `minimum rowsize`. 
3. Pop the top 2 elements from the heap, merge(full outer join) them and push back again to the heap.
4. Repeat the process until we have just one file in the heap, which will be the final merged file.
5. Return the final merged file from heap.

Theoretically a full outer merge costs `O(n*m)`, where `n` and `m` are number of rows in the files (without indexing).
If we index, the same complexity reduces to `O(n+m)`. So, if we have two small files in each step to merge, we save time.

| ⚠️ : The passed `id` should be unique for each row in a dataframe, else the result would depend on the order of merge. |
| --- |


### Installation
Build from source.
<pre>
git clone https://github.com/farziengineer/quick_merge.git
cd quick_merge
python setup.py install
</pre>
### Usage
```python
import pandas as pd

from quick_merge import quick_merge_

df_1 = pd.DataFrame(data={"A" : [1, 2, 3, 4], "B" : [43, 54, 67, 23], "C" : [43, 56, 89, 12]})
df_2 = pd.DataFrame(data={"A" : [4, 5, 1, 6], "D" : [334, 34, 56, 12]})
df_3 = pd.DataFrame(data={"A" : [12, 1, 3, 4], "E" : [12, 54, 56, 67], "F" : [34, 56, 34, 12]})
df_1
   A   B   C
0  1  43  43
1  2  54  56
2  3  67  89
3  4  23  12

df_2

   A    D
0  4  334
1  5   34
2  1   56
3  6   12


df_3
    A   E   F
0  12  12  34
1   1  54  56
2   3  56  34
3   4  67  12


dfs = [df_1, df_2, df_3]

merged_df = quick_merge_(dataframes=dfs, merge_key="A")

merged_df

       B     C      D     E     F
A                                
1   43.0  43.0   56.0  54.0  56.0
2   54.0  56.0    NaN   NaN   NaN
3   67.0  89.0    NaN  56.0  34.0
4   23.0  12.0  334.0  67.0  12.0
5    NaN   NaN   34.0   NaN   NaN
6    NaN   NaN   12.0   NaN   NaN
12   NaN   NaN    NaN  12.0  34.0


  ```
