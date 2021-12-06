CC=gcc
CFLAGS=-pedantic -Wall -Wextra -std=gnu99 -Wno-format-security

run: main
	bin/main data/input.txt

example: main
	bin/main data/example.txt

valgrind: main
	valgrind bin/main data/input.txt

all: main

main: main.o ../c-utils/filereader.o route.o bin
	$(CC) $(CFLAGS) -o bin/main main.o route.o ../c-utils/filereader.o

main.o: main.c main.h ../c-utils/filereader.o
	$(CC) $(CFLAGS) -c main.c

route.o: route.h
	$(CC) $(CFLAGS) -c route.c

../c-utils/filereader.o:  ../c-utils/filereader.c ../c-utils/filereader.h
	$(CC) $(CFLAGS) -c ../c-utils/filereader.c -o ../c-utils/filereader.o

bin:
	mkdir -p bin

clean:
	rm bin/*
	rm *.o
