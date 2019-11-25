#!/usr/bin/env bash
cat file.txt | awk 'NR==10'
tail -n+10 file.txt | head -1
sed -n 10p file.txt