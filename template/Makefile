CC=gcc
CFLAGS=-pedantic -Wall -Wextra -std=gnu99 -Wno-format-security

run: main
	bin/main data/input.txt

valgrind: main
	valgrind bin/main data/input.txt

all: main

main: main.o ../utils/filereader.o bin
	$(CC) $(CFLAGS) -o bin/main main.o ../utils/filereader.o

main.o: main.c main.h ../utils/filereader.o
	$(CC) $(CFLAGS) -c main.c

../utils/filereader.o:  ../utils/filereader.c ../utils/filereader.h
	$(CC) $(CFLAGS) -c ../utils/filereader.c -o ../utils/filereader.o

bin:
	mkdir -p bin

clean:
	rm bin/*
	rm *.o
