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
		fscanf(fp, "%*s\n");
		len++;
	}
	fclose(fp);
	return len;
}
