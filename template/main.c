#include<stdio.h>
#include<stdlib.h>
#include"../utils/filereader.h"

int main(int argc, char **argv){
	if (argc < 2) {
		fprintf(stderr,
				"Input file missing. Give the input file as a command "
				"line argument.\n");
		exit(EXIT_FAILURE);
	}

	int* data = read_int_array(argv[1]);

	// do something

	free(data);
	exit(EXIT_SUCCESS);
}
