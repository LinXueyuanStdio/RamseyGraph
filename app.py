import os
import json

import networkx as nx
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.layouts import LAYOUTS

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
    graphs = nx.read_graph6(graphset_name)
    return graphs


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


with st.sidebar:
    st.title("## Ramsey Graph")
    graphset_name = st.selectbox("R(s,t)_n.g6", os.listdir("data"), index=0)
    graphs = load_graphs(f"data/{graphset_name}")
    G = st.radio("G", graphs)

    st.markdown("## Visualization Settings")
    layout = st.selectbox("Layout Name", LAYOUT_NAMES, index=4)
    show_blue = st.checkbox("Show Blue Edges", True)

    st.markdown("## Graph Data")
    elements = convert_graph_to_json(G, show_blue)
    st.json(elements)
    print(json.dumps(elements, ensure_ascii=False, indent=2))

st.markdown("# Ramsey Graph")
s, t = graphset_name[1], graphset_name[2]
st.markdown(f"the graph does not contain a clique of size {s} (RED) or an independent set of size {t} (BLUE)")
st_link_analysis(elements, layout, node_styles, edge_styles)
