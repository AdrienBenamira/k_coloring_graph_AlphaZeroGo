from sim.EnvTest import EnvTest
from utils.config import Config
from model.Coach import Coach
from model.NNet import NNetWrapper as nn
from utils import *





if __name__=="__main__":
    config = Config('config/')
    envtest = EnvTest(config)
    nnet = nn(envtest, config)
    if config.general.load_model:
        nnet.load_checkpoint(config.path.load_folder_file)
    c = Coach(envtest, nnet, config)
    if config.general.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()