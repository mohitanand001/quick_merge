# quick_merge
A utility to `merge(full outer join)` large number of files in an optimized manner.The algorithm capitalizes on the fact that `full outer join` is `associative` as well as `commutative`, so the order of merging would not change the final result.

Let's say we have 100 files `(f1, f2, f3, .... f100)` all of them indexed by `id`, all of which needs to be merged together to form one consolidate file. Insetead of merging them one after the other in a loop, the quick_merge follows these steps.

1. Add all the files `f1, f2, f3, ... f100` to a heap(the datastructure).
2. Balance the heap, such that the top contains the one with `minimum rowsize`. 
3. Pop the top 2 elements from the heap, merge(full outer join) them and push back again to the heap.
4. Repeat the process until we have just one file in the heap, which will be the final merged file.
5. Return the final merged file from heap.

Theoretically a full outer merge costs `O(n*m)`, where `n` and `m` are number of rows in the files (without indexing).
If we index, the same complexity reduces to `O(n+m)`. So, if we have two small files in each step to merge, we save time.


### Installation
Build from source.
<pre>
git clone https://github.com/farziengineer/quick_merge.git
cd quick_merge
python setup.py install
</pre>
### Usage
```python
from quick_merge import quick_merge as qm

df_1 = pd.DataFrame(
    np.random.randint(0, 100, size=(100, 6)), columns=list("ABCDEF")
)
df_2 = pd.DataFrame(
    np.random.randint(0, 100, size=(100, 9)), columns=list("ABCDEFGHI")
)
df_3 = pd.DataFrame(np.random.randint(0, 100, size=(100, 3)), columns=list("ABC"))

dfs = [df_1, df_2, df_3]

res = qm(dataframes=dfs, merge_key='A')
  ```
