#!/usr/bin/env python

import os

# location of llvm and clang's binaries
clang = '/home/nazim/Desktop/llvm-forked/build/bin'

#name of the plugin
pluginName = 'omr-checker'

# location of plugin's shared library
pluginLib='/home/nazim/Desktop/llvm-forked/build/lib/OMRChecker.so'

#file that contains the list of all files to execute BruteClang on
all_files = 'all_files.config'

files = []
with open(all_files) as fileList:
    for currentFile in fileList:
        currentFile = currentFile.strip()
        os.system(clang + "/clang++ -std=c++0x -w -fsyntax-only '-D__sync()=' '-D__lwsync()=' '-D__isync()='  -Xclang -load -Xclang " + pluginLib + " -Xclang -add-plugin -Xclang "+ pluginName + " " + currentFile)