from git import Repo
import sys
import argparse
from os import listdir
import os


def git_to_wordlist(repo_dir):
    for folderName, subfolders, filenames in os.walk(repo_dir):
        for filename in filenames:
            with open("{}_wordlist.txt".format(repo_dir), "a") as write_wordlist:
                ww = "/".join("{}/{}".format(folderName,filename).split("/")[1:])
                write_wordlist.write(ww + "\n")


def git_clone(git_url):
    """
    Just git clone the repo
    """
    repo_dir = git_url.split("/")[-1].replace(".git", "")
    try:
        Repo.clone_from(git_url, repo_dir)
        git_to_wordlist(repo_dir)
    except:
        print("A problem has detected during the github repository download ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="URL git [required]. Ex: '-u https://github.com/c0dejump/HawkScan.git'", dest='git_url')
    results = parser.parse_args()
                                     
    git_url = results.git_url
    git_clone(git_url)