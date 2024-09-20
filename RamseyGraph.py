# Copyright 2024 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Ramsey Graph Dataset."""

import os
import datasets
import gzip
import networkx as nx

from huggingface_hub import hf_hub_url

_CITATION = """\
@article{xueyuan2024ramseygraph,
  title={Ramsey Graph Dataset},
  author={Xueyuan Lin},
  journal={HuggingFace Datasets},
  year={2024}
}
"""

# Dataset description
_DESCRIPTION = """\
The Ramsey Graph dataset contains graphs related to Ramsey Numbers. These graphs are used in combinatorics to find the smallest vertex number for specific configurations of cliques and independent sets.
"""

# Homepage of the dataset
_HOMEPAGE = "https://huggingface.co/datasets/linxy/RamseyGraph"

# License information
_LICENSE = "MIT"

# URL for dataset files

_AUTHOR = "linxy"
_DATASET = "RamseyGraph"
_FILENAMES = [
    "r34_8.g6",
    "r35_12.g6",
    "r44_3.g6",
    "r37_22.g6",
    "r35_9.g6",
    "r44_7.g6",
    "r39_35.g6",
    "r45_24.g6",
    "r44_6.g6",
    "r44_11.g6.gz",
    "r35_13.g6",
    "r44_2.g6",
    "r44_13.g6.gz",
    "r35_8.g6",
    "r44_9.g6",
    "r34_2.g6",
    "r35_3.g6",
    "r36_4.g6",
    "r44_14.g6.gz",
    "r34_6.g6",
    "r37_21.g6.gz",
    "r35_7.g6",
    "r44_15.g6",
    "r34_7.g6",
    "r36_1.g6",
    "r35_6.g6",
    "r44_12.g6.gz",
    "r36_17.g6",
    "r44_10.g6.gz",
    "r44_8.g6",
    "r34_3.g6",
    "r35_2.g6",
    "r36_5.g6",
    "r44_16.g6",
    "r34_4.g6",
    "r36_16.g6.gz",
    "r36_2.g6",
    "r35_5.g6",
    "r36_14.g6.gz",
    "r35_1.g6",
    "r36_6.g6",
    "r36_10.g6",
    "r34_1.g6",
    "r36_7.g6",
    "r44_17.g6",
    "r36_12.g6.gz",
    "r34_5.g6",
    "r38_27.g6.gz",
    "r36_3.g6",
    "r35_4.g6",
    "r36_15.g6.gz",
    "r44_5.g6",
    "r36_8.g6",
    "r55_42some.g6",
    "r35_10.g6",
    "r44_1.g6",
    "r35_11.g6",
    "r36_13.g6.gz",
    "r46_35some.g6",
    "r44_4.g6",
    "r36_11.g6.gz",
    "r36_9.g6",
]
_URLS = {
    filename.split(".")[0]: hf_hub_url(f"{_AUTHOR}/{_DATASET}", filename=f"data/{filename}", repo_type="dataset")
    for filename in _FILENAMES
}


class RamseyGraph(datasets.GeneratorBasedBuilder):
    """Ramsey Graph Dataset: Contains various Ramsey graphs for combinatorics research."""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(name=filename.split(".")[0], version=datasets.Version("1.0.0"), description=f"Ramsey graphs dataset: R({filename[1]},{filename[2]}), n={filename.split('_')[1].split('.')[0]} (from {filename})")
        for filename in _FILENAMES
    ]

    DEFAULT_CONFIG_NAME = "r34_8"

    def _info(self):
        # Define dataset features
        features = datasets.Features(
            {
                "edges": datasets.Sequence(datasets.Sequence(datasets.Value("int32"))),  # Nested sequence for edge indices
                "num_nodes": datasets.Value("int32"),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        # Download and extract dataset
        name = self.config.name
        url = _URLS[name]
        filepath = dl_manager.download_and_extract(url)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepath": filepath,
                    "name": name,
                    "url": url,
                },
            )
        ]

    def _generate_examples(self, filepath: str, name: str, url: str):
        """Yields examples from the dataset."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Dataset file {filepath} not found.")
        # Determine if the file is gzipped or not
        open_func = gzip.open if url.endswith('.gz') else open

        with open_func(filepath, 'rt') as f:
            for key, line in enumerate(f):
                # Read the graph in g6 format
                graph = nx.from_graph6_bytes(line.strip().encode('utf-8'))

                edges = list(graph.edges) # [(0, 1), (1, 2), ...]
                num_nodes = graph.number_of_nodes()

                # Convert to a JSON-friendly format
                data_json = {
                    "edges": edges,  # Convert to list of lists
                    "num_nodes": num_nodes,
                }

                yield key, data_json
