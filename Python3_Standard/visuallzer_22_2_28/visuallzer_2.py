import argparse
from episode_builder import EpisodeBuilder
from visualizer import Visualizer

DEFAULT_FILE_PATH = "data/template.json"

parser = argparse.ArgumentParser(description="Visualize Conway's Game of Life")
parser.add_argument("-file_path", default=DEFAULT_FILE_PATH)
args = parser.parse_args()

file_path = args.file_path

episode_builder = EpisodeBuilder(file_path)
episode = episode_builder.get_episode()

visualizer = Visualizer(episode)
visualizer.visualize()