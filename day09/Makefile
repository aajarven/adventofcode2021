CC=gcc
CFLAGS=-pedantic -Wall -Wextra -std=gnu99 -Wno-format-security
LIBS=-lm

FUNCTION_FILE=smoke

run: main
	bin/main data/input.txt 100

example: main
	bin/main data/example.txt 10

valgrind: main
	valgrind bin/main data/example.txt 10

all: main

main: main.o $(FUNCTION_FILE).o ../c-utils/filereader.o ../c-utils/arrayutils.o bin
	$(CC) $(CFLAGS) -o bin/main main.o $(FUNCTION_FILE).o ../c-utils/filereader.o ../c-utils/arrayutils.o $(LIBS)

main.o: main.c main.h ../c-utils/filereader.o ../c-utils/arrayutils.o
	$(CC) $(CFLAGS) -c main.c

$(FUNCTION_FILE).o: $(FUNCTION_FILE).h $(FUNCTION_FILE).c
	$(CC) $(CFLAGS) -c $(FUNCTION_FILE).c $(LIBS)

../c-utils/filereader.o:  ../c-utils/filereader.c ../c-utils/filereader.h
	$(CC) $(CFLAGS) -c ../c-utils/filereader.c -o ../c-utils/filereader.o

../c-utils/arrayutils.o: ../c-utils/arrayutils.c ../c-utils/arrayutils.h
	$(CC) $(CFLAGS) -c ../c-utils/arrayutils.c -o ../c-utils/arrayutils.o

bin:
	mkdir -p bin

clean:
	rm -f bin/*
	rm *.o
