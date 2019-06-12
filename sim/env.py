import networkx as nx
import numpy as np



class Env:
    def __init__(self, config):
        self.config = config
        self.vertex_max = config.general.vertex_max
        self.vertex_min = config.general.vertex_min
        self.seed = config.general.seed
        self.directed = config.general.directed
        self.Z = config.general.number_color_init
        np.random.seed(self.seed)

    def _get_graph(self):
        self.vertex = np.random.randint(self.vertex_min, self.vertex_max)
        self.edges_proba = np.random.rand()
        self.G = nx.gnp_random_graph(self.vertex, self.edges_proba, seed=self.seed, directed=self.directed)
        self.C = np.zeros(self.vertex, self.Z)

    def step(self, action):
        """

        :param action: dimension 2 dim1 : le noeud a change dim2: la couleur
        :return: C
        """
        self.C[action[0]][action[1]] = 1

    def reset(self):
        """
        Reinitialize the environment to a random state and returns
        the original state

        :return: state
        """
        pass
