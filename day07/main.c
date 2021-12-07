#include<stdio.h>
#include<stdlib.h>
#include"../c-utils/arrayutils.h"
#include"../c-utils/filereader.h"
#include"crabs.h"

int main(int argc, char **argv){
	if (argc < 4) {
		fprintf(stderr,
				"Not enough arguments. Give the input file, number of crabs in the input "
				"and the maximum coordinate as command line arguments.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];
	int n_crabs = atoi(argv[2]);
	int max_coordinate = atoi(argv[3]);

	int* data = read_row_of_ints(input_file, ',', n_crabs);
	printf("Least naive fuel to alignment: %d\n",
		   least_fuel_to_alignment(data, n_crabs, max_coordinate));
	printf("Least crab engineering fuel to alignment: %d\n",
		   least_crab_engineering_fuel_to_alignment(data, n_crabs, max_coordinate));

	free(data);
	exit(EXIT_SUCCESS);
}
