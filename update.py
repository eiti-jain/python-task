from git import Repo
import argparse, os
parser = argparse.ArgumentParser()
# You added argparse to get path, which is a good thing. But it is not mandatory, hence the user may or may not pass a directory
# TODO: Create a separte function to parse_args
parser.add_argument('--path', help= 'enter path')
args = parser.parse_args()
repo = Repo(args.path)
assert repo.bare == False
repo.remotes.origin.pull()
# TODO: No useful information is printed. This statement prints [<git.remote.FetchInfo object at 0x7fe99ab1d1d0>] which is not helpful at all
print(repo.remotes.origin.pull())
