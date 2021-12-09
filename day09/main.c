#include<stdio.h>
#include<stdlib.h>
#include"../c-utils/arrayutils.h"
#include"../c-utils/filereader.h"
#include"smoke.h"

int main(int argc, char **argv){
	if (argc < 3) {
		fprintf(stderr,
				"Input file or array width missing. Give them as command "
				"line arguments.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];
	int row_length = atoi(argv[2]);

	int rows = count_lines(input_file);
	int* data = read_digit_array(input_file, row_length, rows);

	printf("Risk level sum: %d\n", risk_level_sum(data, row_length, rows));
	printf("Product of three biggest basins: %d\n", basins(data, row_length, rows));

	free(data);
	exit(EXIT_SUCCESS);
}
