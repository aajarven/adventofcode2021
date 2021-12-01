#include<stdio.h>
#include<stdlib.h>
#include"depth.h"
#include"../utils/filereader.h"

int main(int argc, char **argv){
	if (argc < 2) {
		fprintf(stderr,
				"Input file missing. Give the input file as a command "
				"line argument.\n");
		exit(EXIT_FAILURE);
	}

	int len_data = count_lines(argv[1]);
	int* data = read_int_array(argv[1]);

	printf("There are %d measurements larger than the previous one\n",
		   increases(data, len_data));

	printf("There are %d three-measurement windows deeper than the previous one\n",
		   windowed_increases(data, len_data));

	free(data);
	exit(EXIT_SUCCESS);
}
