#!/usr/bin/env bash

# Create sfz directory list for package removal
find sfz/*/* -type d --maxdepth 1 > dir_list.txt
