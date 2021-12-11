#include<stdio.h>
#include<stdlib.h>
#include"../c-utils/filereader.h"
#include"flashes.h"

int main(int argc, char **argv){
	if (argc < 3) {
		fprintf(stderr,
				"Input file or line length missing. Give them command "
				"line arguments.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];
    int line_length = atoi(argv[2]);

	int len_data = count_lines(input_file);
	int* data = read_digit_array(input_file, line_length, len_data);

    printf("Flashes: %d\n", flashes(data, line_length, len_data));
    printf("Synchronized after %d steps\n", 100 + synchronized_after_steps(data, line_length, len_data));

	free(data);
	exit(EXIT_SUCCESS);
}
