---
license: mit
task_categories:
  - graph-ml
language:
  - en
size_categories:
  - 100M<n<1B
---
<div align="center">

<h1>Ramsey Graph</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-blue)](https://huggingface.co/datasets/linxy/RamseyGraph)
[![Live Demo](https://img.shields.io/badge/🌐%20Live-Demo-green)](https://linxueyuan.online/RamseyGraph)
[![Graph ML](https://img.shields.io/badge/Task-Graph%20ML-orange)](https://huggingface.co/datasets/linxy/RamseyGraph)

[🌐 Live Demo](https://linxueyuan.online/RamseyGraph) | [中文文档](README_CN.md)

</div>

| A 6-vertex Ramsey(4, 4) graph and its complement |
| --------------- |
| ![Ramsey(4, 4) graph](ramsey_graph.png) |
| It contains no complete subgraph of 4 vertices, nor does it contain an independent set of 4 vertices. |

A **Ramsey(s,t,n) graph** is a graph with $n$ vertices that contains no clique of size $s$ and no independent set of size $t$. The `n` is usually omitted, and **Ramsey(s,t) graph** is used to refer to Ramsey(s,t,n) graphs for some $n$. **Ramsey's theorem** states that for given $s$ and $t$, the number of Ramsey(s,t) graphs is finite. The minimum number of vertices satisfying a Ramsey graph is called a **Ramsey Number**. However, finding all such graphs, or even determining the maximum $n$ for which they exist, is a famous combinatorial mathematics problem.

The Ramsey numbers known to humans are very limited, with most only having known upper and lower bounds. One approach is to search for the largest Ramsey graphs, whose number of vertices provides a lower bound for the Ramsey number.

If you are interested in this topic, you can try to find the **largest Ramsey(5,5) graph**. All Ramsey(5,5) graphs with 42 vertices have been found, but it is uncertain whether there are any with 43 vertices. The lower bound for the Ramsey number Ramsey(5,5) was last improved in 1989. If you find even one such graph, it would be a significant advancement in this field after 35 years!

> For the latest research on Ramsey graphs, please refer to **Radziszowski**'s dynamic survey, continuously updated in the [**Electronic Journal of Combinatorics**](https://www.combinatorics.org).


## Ramsey Numbers

**Ramsey numbers** refer to the minimum number of vertices satisfying Ramsey graphs. Here are some known Ramsey numbers:

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


## How to Use

This repository hosts graphs related to the classical **Ramsey Numbers**. You can access them using the following code:

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

`r44_3` refers to Ramsey(4,4) graphs with 3 vertices. Here are all dataset names:
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

## Progress

Many Ramsey graphs have been found, but many remain undiscovered. Here are some known Ramsey graphs (also available in `data/` directory):

| Vertices | Ramsey(3,4)              | Ramsey(3,5)                | Ramsey(3,6)                                 | Ramsey(4,4) Graphs                           |
| ------ | ------------------------ | -------------------------- | ------------------------------------------- | -------------------------------------------- |
| 1      | [1 graph](data/r34_1.g6)  | [1 graph](data/r35_1.g6)    | [1 graph](data/r36_1.g6)                     | [1 graph](data/r44_1.g6)                      |
| 2      | [2 graphs](data/r34_2.g6)  | [2 graphs](data/r35_2.g6)    | [2 graphs](data/r36_2.g6)                     | [2 graphs](data/r44_2.g6)                      |
| 3      | [3 graphs](data/r34_3.g6)  | [3 graphs](data/r35_3.g6)    | [3 graphs](data/r36_3.g6)                     | [4 graphs](data/r44_3.g6)                      |
| 4      | [6 graphs](data/r34_4.g6)  | [7 graphs](data/r35_4.g6)    | [7 graphs](data/r36_4.g6)                     | [9 graphs](data/r44_4.g6)                      |
| 5      | [9 graphs](data/r34_5.g6)  | [13 graphs](data/r35_5.g6)   | [14 graphs](data/r36_5.g6)                    | [24 graphs](data/r44_5.g6)                     |
| 6      | [15 graphs](data/r34_6.g6) | [32 graphs](data/r35_6.g6)   | [37 graphs](data/r36_6.g6)                    | [84 graphs](data/r44_6.g6)                     |
| 7      | [9 graphs](data/r34_7.g6)  | [71 graphs](data/r35_7.g6)   | [100 graphs](data/r36_7.g6)                   | [362 graphs](data/r44_7.g6)                    |
| 8      | [3 graphs](data/r34_8.g6)  | [179 graphs](data/r35_8.g6)  | [356 graphs](data/r36_8.g6)                   | [2079 graphs](data/r44_8.g6)                   |
| 9      |                          | [290 graphs](data/r35_9.g6)  | [1407 graphs](data/r36_9.g6)                  | [14701 graphs](data/r44_9.g6)                  |
| 10     |                          | [313 graphs](data/r35_10.g6) | [6657 graphs](data/r36_10.g6)                 | [103706 graphs (compressed)](data/r44_10.g6.gz)  |
| 11     |                          | [105 graphs](data/r35_11.g6) | [30395 graphs (compressed)](data/r36_11.g6.gz)  | [546356 graphs (compressed)](data/r44_11.g6.gz)  |
| 12     |                          | [12 graphs](data/r35_12.g6)  | [116792 graphs (compressed)](data/r36_12.g6.gz) | [1449166 graphs (compressed)](data/r44_12.g6.gz) |
| 13     |                          | [1 graph](data/r35_13.g6)   | [275086 graphs (compressed)](data/r36_13.g6.gz) | [1184231 graphs (compressed)](data/r44_13.g6.gz) |
| 14     |                          |                            | [263520 graphs (compressed)](data/r36_14.g6.gz) | [130816 graphs (compressed)](data/r44_14.g6.gz)  |
| 15     |                          |                            | [64732 graphs (compressed)](data/r36_15.g6.gz)  | [640 graphs](data/r44_15.g6)                   |
| 16     |                          |                            | [2576 graphs (compressed)](data/r36_16.g6.gz)   | [2 graphs](data/r44_16.g6)                     |
| 17     |                          |                            | [7 graphs](data/r36_17.g6)                    | [1 graph](data/r44_17.g6)                     |

- All maximal Ramsey(3,7) graphs
  - [21 vertices (compressed)](data/r37_21.g6.gz) (1118436 graphs, discovered by **Gunnar Brinkmann** and **Jan Goedgebeur**)
  - [22 vertices](data/r37_22.g6) (191 graphs)
- All maximal Ramsey(3,8) graphs
  - In 1992, **McKay** and **Zhang** proved that the maximal Ramsey(3,8) graph has 27 vertices, but the complete set of Ramsey(3,8,27) graphs was not determined until 2012 by **Gunnar Brinkmann** and **Jan Goedgebeur**.
  - [27 vertices (compressed)](data/r38_27.g6.gz) (477142 graphs)
- All maximal Ramsey(3,9) graphs
  - The maximal Ramsey(3,9) graph has 35 vertices, discovered long ago by **Kalbfleisch**, but its uniqueness was not proven until 2013. See the [paper](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i1p30) by **Goedgebeur** and **Radziszowski**.
  - [35 vertices](data/r39_35.g6) (1 graph)
- All maximal Ramsey(4,5) graphs
  - In 1995, **McKay** and **Radziszowski** proved that there are no Ramsey(4,5) graphs with more than 24 vertices and found 350904 graphs with 24 vertices. The remaining graphs were discovered in 2016 by **McKay** and **Angeltveit**. There are 352366 graphs in total, see [r45_24.g6](data/r45_24.g6).
- Known largest Ramsey(4,6) graphs
  - In early 2012, **Geoffrey Exoo** discovered 37 Ramsey(4,6,35) graphs. There may be more, and graphs with 36 to 40 vertices may even exist. See [r46_35some.g6](data/r46_35some.g6).
- Known largest Ramsey(5,5) graphs
  - In 1989, **Geoffrey Exoo** discovered several Ramsey(5,5,42) graphs. **McKay** and **Radziszowski** extended this to 656 graphs and conjectured that larger graphs are impossible. However, there may be more 42-vertex graphs, and graphs with 43 to 47 vertices may even exist. [r55_42some.g6](data/r55_42some.g6) contains 328 of these graphs, with the other 328 being their complements.
- Ramsey(4,4;3)-hypergraphs
  - A **Ramsey(4,4;3) hypergraph** is a 3-uniform hypergraph that cannot contain a complete subgraph with 4 vertices, nor a complete independent set with 4 vertices. **Steve Butler** and **Aaron Wootton** discovered 42 such hypergraphs in 2010, each with 13 vertices.


## Acknowledgments

The [**ramsey**](https://users.cecs.anu.edu.au/~bdm/data/ramsey.html) database by **Gunnar Brinkmann** and **Jan Goedgebeur**
