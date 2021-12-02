#include<stdio.h>
#include<stdlib.h>
#include"route.h"
#include"../utils/filereader.h"

int main(int argc, char **argv){
	if (argc < 2) {
		fprintf(stderr,
				"Input file missing. Give the input file as a command "
				"line argument.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];

	int len_data = count_lines(input_file);
	char* data = read_lines(input_file, 20);

	printf("Position product: %d\n",
		   position_product(data, 20, len_data));
	printf("Aimed position product: %d\n",
		   aimed_position_product(data, 20, len_data));

	free(data);
	exit(EXIT_SUCCESS);
}
