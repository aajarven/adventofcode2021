#include<stdio.h>
#include<stdlib.h>
#include"../c-utils/filereader.h"
#include"syntax.h"

int main(int argc, char **argv){
	if (argc < 3) {
		fprintf(stderr,
				"Input file or max line length missing. Give both as command "
				"line arguments.\n");
		exit(EXIT_FAILURE);
	}

	char* input_file = argv[1];
	int max_line_length = atoi(argv[2]);

	int len_data = count_lines(input_file);
	char* data = read_lines(input_file, max_line_length);

	printf("Syntax score: %d\n", syntax_score(data, max_line_length, len_data));
	printf("Autocomplete score: %ld\n", autocomplete_score(data, max_line_length, len_data));

	free(data);
	exit(EXIT_SUCCESS);
}
