#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"filereader.h"

/*
 * Reads all numbers from a file and returns them in an array.
 * One number per line.
 */
int* read_int_array(char* filename){
	FILE *fp = fopen(filename, "r");

	int len = count_lines(filename);
	int *data = malloc(len * sizeof(int));

	int i=0;
	while(i < len){
		fscanf(fp, "%d", &data[i++]);
	}
	fclose(fp);

	return data;
}

/*
 * Return the number of lines in a file
 */
int count_lines(char* filename){
	FILE *fp = fopen(filename, "r");
	int len = 0;
	while(!feof(fp)){
		if (fgetc(fp) == '\n') {
			len++;
		}
	}
	fclose(fp);
	return len;
}

/*
 * Read a the lines from a text file into a 2D char array.
 */
char* read_lines(char* filename, int max_line_length){

	int len = count_lines(filename);
	char* arr = malloc(len * max_line_length * sizeof(char));

	FILE *fp = fopen(filename, "r");

	int line=0;
	while(fgets(&arr[line * max_line_length], max_line_length, fp) != NULL && ++line < len){
	}
	fclose(fp);
	return arr;
}

/*
 * Read a file containing a single row of integers into an array.
 */
int* read_row_of_ints(char* filename, char separator, int max_ints) {
	FILE *fp = fopen(filename, "r");

    char format[] = "%d";
    strncat(format, &separator, 1);

    int* arr = malloc(max_ints * sizeof(int));
    int current_index = -1;

    // read the integers
    while(!feof(fp)) {
        fscanf(fp, format, &arr[++current_index]);
    }

    // fill the rest of the array with -1 to signify the end of input
    while (current_index < max_ints) {
        arr[current_index++] = -1;
    }

	fclose(fp);
    return arr;
}


/*
 * Read an array of digits into an int array
 */
int* read_digit_array(char* filename, int width, int height) {
	int* arr = malloc(width * height * sizeof(int));
	FILE *fp = fopen(filename, "r");

	char next_digit;
	int row = 0;
	int column = 0;

	while ( (next_digit = getc(fp)) != EOF) {
		if (next_digit != '\n') {
			arr[row*width + column] = (int) next_digit - '0';

			column++;
			if (column >= width) {
				row++;
				column = 0;
			}
		}
	}

	fclose(fp);
	return arr;
}
