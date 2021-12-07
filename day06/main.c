#include<stdio.h>
#include<stdlib.h>
#include"lanternfish.h"
#include"../c-utils/filereader.h"
#include"../c-utils/arrayutils.h"

int main(int argc, char **argv){
	if (argc < 2) {
		fprintf(stderr,
				"Input file missing. Give the input file as a command "
				"line argument.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];

	int* data = read_row_of_ints(input_file, ',', 500);
    long* countdowns = parse_countdown(data, 500);
    printf("Number of fish after 80 days: %ld\n",
            count_after_n_days(countdowns, 80));
    printf("Number of fish after 256 days: %ld\n",
            count_after_n_days(countdowns, 256-80));

    free(countdowns);
	free(data);
	exit(EXIT_SUCCESS);
}
