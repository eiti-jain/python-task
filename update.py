from git import Repo
import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument('--path', help= 'enter path')
args = parser.parse_args()
repo = Repo(args.path)
assert repo.bare == False
repo.remotes.origin.pull()
print(repo.remotes.origin.pull())
