import os
import subprocess

cc = 'g++ '
include = '-ITools '
cflags = '-lm -lrt'

# Default
os.system('mkdir -p bin obj')
os.system('g++ -ITools -lm -lrt -c src/CHeterodyning.c -o obj/CHeterodyning.o')
os.system('g++ -ITools -lm -lrt -c Tools/Timer.cpp -o obj/Timer.o')
os.system('g++ -o bin/CHeterodyning obj/CHeterodyning.o obj/Timer.o -lm -lrt')

