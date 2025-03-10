---
license: mit
task_categories:
  - graph-ml
language:
  - en
size_categories:
  - 100M<n<1B
---
# Ramsey Graph

[Live Demo](https://huggingface.co/spaces/linxy/RamseyGraph)

本仓库托管了一些与经典 **拉姆齐数（Ramsey Number）** 相关的图。同时发布到 [Huggingface datasets (linxy/RamseyGraph)](https://huggingface.co/datasets/linxy/RamseyGraph)。你可以使用以下代码获取：

```bash
pip install datasets
```

```python
>>> from datasets import load_dataset
>>> dataset = load_dataset("linxy/RamseyGraph", "r44_3", trust_remote_code=True)
>>> for i in dataset["train"]:
>>>     print(i)
{'edges': [], 'num_nodes': 3}
{'edges': [[1, 2]], 'num_nodes': 3}
{'edges': [[0, 2], [1, 2]], 'num_nodes': 3}
{'edges': [[0, 1], [0, 2], [1, 2]], 'num_nodes': 3}
```

`r44_3` 指 Ramsey(4,4) 图中 3 个顶点的图。以下是所有数据集的名称：
```python
['r34_1', 'r34_2', 'r34_3', 'r34_4', 'r34_5', 'r34_6', 'r34_7', 'r34_8',
 'r35_1', 'r35_2', 'r35_3', 'r35_4', 'r35_5', 'r35_6', 'r35_7', 'r35_8', 'r35_9', 'r35_10', 'r35_11', 'r35_12', 'r35_13',
 'r36_1', 'r36_2', 'r36_3', 'r36_4', 'r36_5', 'r36_6', 'r36_7', 'r36_8', 'r36_9', 'r36_10', 'r36_11', 'r36_12', 'r36_13', 'r36_14', 'r36_15', 'r36_16', 'r36_17',
 'r37_21', 'r37_22',
 'r38_27',
 'r39_35',
 'r44_1', 'r44_2', 'r44_3', 'r44_4', 'r44_5', 'r44_6', 'r44_7', 'r44_8', 'r44_9', 'r44_10', 'r44_11', 'r44_12', 'r44_13', 'r44_14', 'r44_15', 'r44_16', 'r44_17',
 'r45_24',
 'r46_35some',
 'r55_42some']
```

# 介绍

| 一个 6 结点的 Ramsey(4, 4) 图及其补图 |
| --------------- |
| ![Ramsey(4, 4) 图](ramsey_graph.png) |
| 它不包含 4 个顶点的完全子图，也不包含 4 个顶点的完全独立集。 |

**Ramsey(s,t,n) 图** 是具有 $n$ 个顶点的图，它不包含大小为 $s$ 的团，也不包含大小为 $t$ 的独立集。通常将 `n` 省略，用 **Ramsey(s,t) 图** 代指某些 $n$ 的 Ramsey(s,t,n) 图。 **Ramsey 定理**表示，对于给定的 $s$ 和 $t$，Ramsey(s,t) 图的数量是有限的。我们称满足 Ramsey 图的最小顶点数为**拉姆齐数（Ramsey Number）**。然而，找到所有这样的图，甚至确定它们存在的最大 $n$，都是一个著名的组合数学难题。

人类已知的拉姆齐数非常有限，大部分只能知道该数的上界和下界。一个方法是寻找最大 Ramsey 图，它的顶点数就是 Ramsey 数的下界。

如果你对这个主题感兴趣，可以尝试找一下 **最大的 Ramsey(5,5) 图**。人们已经将 42 顶点的 Ramsey(5,5) 图全部找到了，但是不确定有没有 43 顶点的 Ramsey(5,5) 图。拉姆齐数 Ramsey(5,5) 的下界最后一次被改进是在 1989 年。只要你找到一个，那就是这个领域 35 年来的重要进展！

> 有关 Ramsey 图的最新研究，请参见 **Radziszowski** 的动态综述，持续更新刊登于 [**电子组合学期刊**](https://www.combinatorics.org)。


## Ramsey 数

**Ramsey 数** 是指满足 Ramsey 图的最小顶点数。以下是一些已知的 Ramsey 数：

| s\t | 1   | 2   | 3   | 4   | 5       | 6         | 7         | 8          | 9          | 10          |
| --- | --- | --- | --- | --- | ------- | --------- | --------- | ---------- | ---------- | ----------- |
| 1   | 1   | 1   | 1   | 1   | 1       | 1         | 1         | 1          | 1          | 1           |
| 2   | -   | 2   | 3   | 4   | 5       | 6         | 7         | 8          | 9          | 10          |
| 3   | -   | -   | 6   | 9   | 14      | 18        | 23        | 28         | 36         | 40 - 41     |
| 4   | -   | -   | -   | 18  | 25      | 36 - 40   | 49 - 58   | 59 - 79    | 73 - 106   | 92 - 136    |
| 5   | -   | -   | -   | -   | 43 - 48 | 59 - 85   | 80 - 133  | 101 - 194  | 133 - 282  | 149 - 381   |
| 6   | -   | -   | -   | -   | -       | 102 - 161 | 115 - 273 | 134 - 427  | 183 - 656  | 204 - 949   |
| 7   | -   | -   | -   | -   | -       | -         | 205 - 497 | 219 - 840  | 252 - 1379 | 292 - 2134  |
| 8   | -   | -   | -   | -   | -       | -         | -         | 282 - 1532 | 329 - 2683 | 343 - 4432  |
| 9   | -   | -   | -   | -   | -       | -         | -         | -          | 565 - 5366 | 581 - 9797  |
| 10  | -   | -   | -   | -   | -       | -         | -         | -          | -          | 798 - 17730 |

## 进展

目前人们已经找到了许多 Ramsey 图，但仍有许多图尚未找到。以下是一些已知的 Ramsey 图：

| 顶点数 | Ramsey(3,4)              | Ramsey(3,5)                | Ramsey(3,6)                                 | Ramsey(4,4) 图                               |
| ------ | ------------------------ | -------------------------- | ------------------------------------------- | -------------------------------------------- |
| 1      | [1 个图](data/r34_1.g6)  | [1 个图](data/r35_1.g6)    | [1 个图](data/r36_1.g6)                     | [1 个图](data/r44_1.g6)                      |
| 2      | [2 个图](data/r34_2.g6)  | [2 个图](data/r35_2.g6)    | [2 个图](data/r36_2.g6)                     | [2 个图](data/r44_2.g6)                      |
| 3      | [3 个图](data/r34_3.g6)  | [3 个图](data/r35_3.g6)    | [3 个图](data/r36_3.g6)                     | [4 个图](data/r44_3.g6)                      |
| 4      | [6 个图](data/r34_4.g6)  | [7 个图](data/r35_4.g6)    | [7 个图](data/r36_4.g6)                     | [9 个图](data/r44_4.g6)                      |
| 5      | [9 个图](data/r34_5.g6)  | [13 个图](data/r35_5.g6)   | [14 个图](data/r36_5.g6)                    | [24 个图](data/r44_5.g6)                     |
| 6      | [15 个图](data/r34_6.g6) | [32 个图](data/r35_6.g6)   | [37 个图](data/r36_6.g6)                    | [84 个图](data/r44_6.g6)                     |
| 7      | [9 个图](data/r34_7.g6)  | [71 个图](data/r35_7.g6)   | [100 个图](data/r36_7.g6)                   | [362 个图](data/r44_7.g6)                    |
| 8      | [3 个图](data/r34_8.g6)  | [179 个图](data/r35_8.g6)  | [356 个图](data/r36_8.g6)                   | [2079 个图](data/r44_8.g6)                   |
| 9      |                          | [290 个图](data/r35_9.g6)  | [1407 个图](data/r36_9.g6)                  | [14701 个图](data/r44_9.g6)                  |
| 10     |                          | [313 个图](data/r35_10.g6) | [6657 个图](data/r36_10.g6)                 | [103706 个图 (压缩文件)](data/r44_10.g6.gz)  |
| 11     |                          | [105 个图](data/r35_11.g6) | [30395 个图 (压缩文件)](data/r36_11.g6.gz)  | [546356 个图 (压缩文件)](data/r44_11.g6.gz)  |
| 12     |                          | [12 个图](data/r35_12.g6)  | [116792 个图 (压缩文件)](data/r36_12.g6.gz) | [1449166 个图 (压缩文件)](data/r44_12.g6.gz) |
| 13     |                          | [1 个图](data/r35_13.g6)   | [275086 个图 (压缩文件)](data/r36_13.g6.gz) | [1184231 个图 (压缩文件)](data/r44_13.g6.gz) |
| 14     |                          |                            | [263520 个图 (压缩文件)](data/r36_14.g6.gz) | [130816 个图 (压缩文件)](data/r44_14.g6.gz)  |
| 15     |                          |                            | [64732 个图 (压缩文件)](data/r36_15.g6.gz)  | [640 个图](data/r44_15.g6)                   |
| 16     |                          |                            | [2576 个图 (压缩文件)](data/r36_16.g6.gz)   | [2 个图](data/r44_16.g6)                     |
| 17     |                          |                            | [7 个图](data/r36_17.g6)                    | [1 个图](data/r44_17.g6)                     |

- 所有最大 Ramsey(3,7) 图
  - [21 个顶点 (压缩文件)](data/r37_21.g6.gz) (1118436 个图，由 **Gunnar Brinkmann** 和 **Jan Goedgebeur** 发现)
  - [22 个顶点](data/r37_22.g6) (191 个图)
- 所有最大 Ramsey(3,8) 图
  - 1992 年 **McKay** 和 **Zhang** 证明最大 Ramsey(3,8) 图有 27 个顶点，但完整的 Ramsey(3,8,27) 图集直到 2012 年才由 **Gunnar Brinkmann** 和 **Jan Goedgebeur** 确定。
  - [27 个顶点 (压缩文件)](data/r38_27.g6.gz) (477142 个图)
- 所有最大 Ramsey(3,9) 图
  - 最大 Ramsey(3,9) 图有 35 个顶点，由 **Kalbfleisch** 很久以前发现，但直到 2013 年才证明其唯一性。参见 **Goedgebeur** 和 **Radziszowski** 的[论文](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i1p30)。
  - [35 个顶点](data/r39_35.g6) (1 个图)
- 所有最大 Ramsey(4,5) 图
  - 1995 年，**McKay** 和 **Radziszowski** 证明不存在超过 24 个顶点的 Ramsey(4,5) 图，并找到了 350904 个 24 顶点的图。剩下的图在 2016 年由 **McKay** 和 **Angeltveit** 发现。总共有 352366 个图，参见 [r45_24.g6](data/r45_24.g6)。
- 已知最大的 Ramsey(4,6) 图
  - 2012 年初，**Geoffrey Exoo** 发现了 37 个 Ramsey(4,6,35) 图。这可能还有更多，甚至可能存在 36 到 40 个顶点的图。参见 [r46_35some.g6](data/r46_35some.g6)。
- 已知最大的 Ramsey(5,5) 图
  - 1989 年，**Geoffrey Exoo** 发现了几个 Ramsey(5,5,42) 图。**McKay** 和 **Radziszowski** 将其扩展至 656 个图，并推测不可能有更大的图。然而，可能还有更多 42 顶点的图，甚至可能存在 43 到 47 个顶点的图。[r55_42some.g6](data/r55_42some.g6) 包含其中 328 个图，其他 328 个是它们的补图。
- Ramsey(4,4;3)-超图
  - **Ramsey(4,4;3) 超图** 是一个 3-均匀超图，不能包含 4-顶点的完全子图，也不能包含 4-顶点的完全独立集。**Steve Butler** 和 **Aaron Wootton** 在 2010 年发现了 42 个这样的超图，每个都有 13 个顶点。


## Thanks

**Gunnar Brinkmann** 和 **Jan Goedgebeur** 的 [**ramsey**](https://users.cecs.anu.edu.au/~bdm/data/ramsey.html) 数据库
