import os
import json

import networkx as nx
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.layouts import LAYOUTS
from datasets import load_dataset

LAYOUT_NAMES = list(LAYOUTS.keys())

st.set_page_config(layout="wide")

# Sample Data

elements = {
    "nodes": [
        {"data": {"id": 1, "label": "Node", "name": "Streamlit"}},
        {"data": {"id": 2, "label": "PERSON", "name": "Hello"}},
        {"data": {"id": 3, "label": "Node", "name": "World"}},
        {"data": {"id": 4, "label": "POST", "content": "x"}},
        {"data": {"id": 5, "label": "POST", "content": "y"}},
    ],
    "edges": [
        {"data": {"id": 6, "label": "FOLLOWS", "source": 1, "target": 2}},
        {"data": {"id": 7, "label": "FOLLOWS", "source": 2, "target": 3}},
        {"data": {"id": 8, "label": "POSTED", "source": 3, "target": 4}},
        {"data": {"id": 9, "label": "POSTED", "source": 1, "target": 5}},
        {"data": {"id": 10, "label": "QUOTES", "source": 5, "target": 4}},
    ],
}

# Style node & edge groups
node_styles = [
    NodeStyle("Node", "#FF7F3E", "name"),
]

edge_styles = [
    EdgeStyle("RED", "#FFB6C1", directed=False),
    EdgeStyle("BLUE", "#87CEEB", directed=False),
]

# Render the component
@st.cache_data
def load_graphs(graphset_name: str):
    graphs = nx.read_graph6(f"data/{graphset_name}")
    return graphs
@st.cache_data
def load_graphs_from_dataset(graphset_name: str):
    dataset = load_dataset("linxy/RamseyGraph", graphset_name, trust_remote_code=True)
    return list(dataset["train"])

_FILENAMES = [
    "r34_8",
    "r35_12",
    "r44_3",
    "r37_22",
    "r35_9",
    "r44_7",
    "r39_35",
    "r45_24",
    "r44_6",
    "r44_11",
    "r35_13",
    "r44_2",
    "r44_13",
    "r35_8",
    "r44_9",
    "r34_2",
    "r35_3",
    "r36_4",
    "r44_14",
    "r34_6",
    "r37_21",
    "r35_7",
    "r44_15",
    "r34_7",
    "r36_1",
    "r35_6",
    "r44_12",
    "r36_17",
    "r44_10",
    "r44_8",
    "r34_3",
    "r35_2",
    "r36_5",
    "r44_16",
    "r34_4",
    "r36_16",
    "r36_2",
    "r35_5",
    "r36_14",
    "r35_1",
    "r36_6",
    "r36_10",
    "r34_1",
    "r36_7",
    "r44_17",
    "r36_12",
    "r34_5",
    "r38_27",
    "r36_3",
    "r35_4",
    "r36_15",
    "r44_5",
    "r36_8",
    "r55_42some",
    "r35_10",
    "r44_1",
    "r35_11",
    "r36_13",
    "r46_35some",
    "r44_4",
    "r36_11",
    "r36_9",
]

def convert_graph_to_json(G, show_blue):
    # 创建元素列表，存储节点和边的数据
    elements = {"nodes": [], "edges": []}

    # 遍历图的所有节点并将其添加到elements["nodes"]
    for node in G.nodes(data=True):
        # 假设你想为节点提供一个简单的 "label" 和 "name"
        # 可以根据需求自定义数据结构
        elements["nodes"].append(
            {
                "data": {
                    "id": str(node[0]),
                    "label": node[1].get("label", f"Node"),  # 可根据实际属性设置
                    "name": node[1].get("name", f"Node{node[0]}"),
                }
            }
        )

    # 遍历图的所有边并将其添加到elements["edges"]
    edge_set = set()
    for i, edge in enumerate(G.edges(data=True)):
        elements["edges"].append(
            {
                "data": {
                    "id": str(i + len(G.nodes)),  # 确保edge的id与node的id不冲突
                    "label": edge[2].get("label", f"RED"),
                    "source": str(edge[0]),
                    "target": str(edge[1]),
                }
            }
        )
        edge_set.add((str(edge[0]), str(edge[1])))

    if show_blue:
        for i in range(len(G.nodes)):
            for j in range(i+1, len(G.nodes)):
                if (str(i), str(j)) in edge_set:
                    continue
                elements["edges"].append(
                    {
                        "data": {
                            "id": str(len(G.nodes) + len(G.edges) + i*(len(G.nodes)) + j),  # 确保edge的id与node的id不冲突
                            "label": "BLUE",
                            "source": str(i),
                            "target": str(j),
                        }
                    }
                )


    return elements


def convert_data_to_elements(G, show_blue):
    elements = {"nodes": [], "edges": []}

    for node in range(G['num_nodes']):
        elements["nodes"].append(
            {
                "data": {
                    "id": str(node),
                    "label": "Node",
                    "name": f"Node {node}",
                }
            }
        )

    edge_set = set()
    for i, (source, target) in enumerate(G["edges"]):
        elements["edges"].append(
            {
                "data": {
                    "id": str(G['num_nodes'] + i),
                    "label": "RED",
                    "source": str(source),
                    "target": str(target),
                }
            }
        )
        edge_set.add((str(source), str(target)))

    if show_blue:
        for i in range(G['num_nodes']):
            for j in range(i+1, G['num_nodes']):
                if (str(i), str(j)) in edge_set:
                    continue
                elements["edges"].append(
                    {
                        "data": {
                            "id": str(G['num_nodes'] + len(G["edges"]) + i*(G['num_nodes']) + j),  # 确保edge的id与node的id不冲突
                            "label": "BLUE",
                            "source": str(i),
                            "target": str(j),
                        }
                    }
                )
    return elements

with st.sidebar:
    st.title("Ramsey Graph")
    # graphset_name = st.selectbox("R(s,t)_n", os.listdir("data"), index=0)
    # dataset = load_dataset("linxy/RamseyGraph", graphset_name, trust_remote_code=True)
    # graphs = load_graphs(graphset_name)
    graphset_name = st.selectbox("R(s,t)_n", _FILENAMES, index=0)
    graphs = load_graphs_from_dataset(graphset_name)
    G = st.radio("G", graphs, index=0, format_func=lambda x: f"Graph with {x['num_nodes']} nodes and {len(x['edges'])} edges")

    st.markdown("## Visualization Settings")
    layout = st.selectbox("Layout Name", LAYOUT_NAMES, index=4)
    show_blue = st.checkbox("Show Blue Edges", True)

    st.markdown("## Graph Data")
    elements = convert_data_to_elements(G, show_blue)
    st.json(elements)
    # print(json.dumps(elements, ensure_ascii=False, indent=2))

st.markdown("# Ramsey Graph")
s, t = graphset_name[1], graphset_name[2]
st.markdown(f"the graph does not contain a clique of size {s} (RED) or an independent set of size {t} (BLUE)")
st_link_analysis(elements, layout, node_styles, edge_styles)
