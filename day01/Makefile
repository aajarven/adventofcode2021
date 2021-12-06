CC=gcc
CFLAGS=-pedantic -Wall -Wextra -std=gnu99 -Wno-format-security

run: main
	bin/main data/input.txt

example: main
	bin/main data/example.txt

valgrind: main
	valgrind bin/main data/input.txt

all: main

main: main.o depth.o ../c-utils/filereader.o bin
	$(CC) $(CFLAGS) -o bin/main main.o depth.o ../c-utils/filereader.o

main.o: main.c main.h ../c-utils/filereader.o
	$(CC) $(CFLAGS) -c main.c

depth.o: depth.c depth.h
	$(CC) $(CFLAGS) -c depth.c

../c-utils/filereader.o:  ../c-utils/filereader.c ../c-utils/filereader.h
	$(CC) $(CFLAGS) -c ../c-utils/filereader.c -o ../c-utils/filereader.o

bin:
	mkdir -p bin

clean:
	rm bin/*
	rm *.o
