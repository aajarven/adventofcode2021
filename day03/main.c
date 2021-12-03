#include<stdio.h>
#include<stdlib.h>
#include"power.h"
#include"../utils/arrayutils.h"
#include"../utils/filereader.h"

int main(int argc, char **argv){
	if (argc < 3) {
		fprintf(stderr,
				"Input file or measurement length missing. Give them as "
				"command line arguments.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];
	int measurement_length = atoi(argv[2]);

	int len_data = count_lines(input_file);
	char* raw_data = read_lines(input_file, measurement_length + 2);
	int* numeric_data = char_array_to_digits(
			raw_data,
			len_data,
			measurement_length,
			2);

	printf("power consumption: %d\n", power(raw_data, len_data, measurement_length));
	printf("life support: %d\n", lifesupport(numeric_data, len_data, measurement_length));

	free(raw_data);
	free(numeric_data);
	exit(EXIT_SUCCESS);
}
