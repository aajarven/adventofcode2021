CC=gcc
CFLAGS=-pedantic -Wall -Wextra -std=gnu99 -Wno-format-security
LIBS=-lm

run: main
	bin/main data/input.txt 12

example: main
	bin/main data/example.txt 5

valgrind: main
	valgrind bin/main data/input.txt 12

all: main

main: main.o power.o ../utils/filereader.o ../utils/arrayutils.o bin
	$(CC) $(CFLAGS) -o bin/main main.o power.o ../utils/filereader.o ../utils/arrayutils.o $(LIBS)

main.o: main.c main.h ../utils/filereader.o ../utils/arrayutils.o
	$(CC) $(CFLAGS) -c main.c

power.o: power.h power.c
	$(CC) $(CFLAGS) -c power.c $(LIBS)

../utils/filereader.o:  ../utils/filereader.c ../utils/filereader.h
	$(CC) $(CFLAGS) -c ../utils/filereader.c -o ../utils/filereader.o

../utils/arrayutils.o: ../utils/arrayutils.c ../utils/arrayutils.h
	$(CC) $(CFLAGS) -c ../utils/arrayutils.c -o ../utils/arrayutils.o

bin:
	mkdir -p bin

clean:
	rm -f bin/*
	rm *.o
