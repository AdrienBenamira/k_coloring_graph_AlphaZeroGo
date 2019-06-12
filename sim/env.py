import networkx as nx
import numpy as np



class Env:
    def __init__(self, config):
        self.config = config
        self.vertex_max = config.general.vertex_max
        self.vertex_min = config.general.vertex_min
        self.edges_proba = np.random.rand()
        self.vertex = np.random.randint(self.vertex_min, self.vertex_max)+1
        self.seed = config.general.seed
        self.directed = config.general.seed
        self.G = nx.gnp_random_graph(self.vertex, self.edges_proba, seed = self.seed, directed=self.directed)

    def step(self, action):
        pass

    def reset(self):
        """
        Reinitialize the environment to a random state and returns
        the original state

        :return: state
        """
        pass
