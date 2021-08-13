#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from git import Repo
import sys
import argparse
from os import listdir
import os
import shutil
import traceback


def git_to_wordlist(repo_dir, output):
    if output == ".":
        output_file = "{}_wordlist.txt".format(repo_dir)
    else:
        output_file = "{}/{}__wordlist.txt".format(output, repo_dir) if output[-1] != "/" else "{}{}__wordlist.txt".format(output, repo_dir)
    for folderName, subfolders, filenames in os.walk(repo_dir):
        for filename in filenames:
            with open(output_file, "a") as write_wordlist:
                ww = "/".join("{}/{}".format(folderName,filename).split("/")[1:])
                write_wordlist.write(ww + "\n")
    shutil.rmtree(repo_dir)
    print("[+] Github repository have been copy to {}".format(output_file))


def git_clone(git_url, output):
    """
    Just git clone the repo
    """
    repo_dir = git_url.split("/")[-1].replace(".git", "")
    try:
        Repo.clone_from(git_url, repo_dir)
        git_to_wordlist(repo_dir, output)
    except:
        #traceback.print_exc() #Debug
        print("A problem has detected during the github repository download ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="URL git [required]. Ex: '-u https://github.com/c0dejump/HawkScan.git'", dest='git_url')
    parser.add_argument("-o", help="Output (default in directory)", required=False, dest="output", default=".")

    results = parser.parse_args()

                                     
    git_url = results.git_url
    output = results.output

    git_clone(git_url, output)
