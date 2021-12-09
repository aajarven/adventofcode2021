#include<stdbool.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include"../c-utils/arrayutils.h"

#define UNVISITED -1
#define BORDER 9


int risk_level(int* data, int column, int row, int width, int height);
void expand_low_point(int* data, int* in_basin, int basin_index,
					  int column, int row,
					  int width, int height);
void visit_neighbors(int* data, int* in_basin, int basin_index,
					 int previous_column, int previous_row,
				     int column, int row,
					 int width, int height);
bool valid_index(int column, int row, int width, int height);


int risk_level_sum(int* data, int width, int height) {
	int sum = 0;
	for (int i=0; i<height; i++) {
		for (int j=0; j<width; j++) {
			int risk = risk_level(data, j, i, width, height);
			sum += risk;
		}
	}
	return sum;
}


int basins(int* data, int width, int height) {

	int* in_basin = malloc(width * height * sizeof(int));
	memset(in_basin, -1, width * height * sizeof(int));

	int basin_index = 0;

	// find the basins
	for (int i=0; i<height; i++) {
		for (int j=0; j<width; j++) {
			if (risk_level(data, j, i, width, height) > 0) {
				expand_low_point(data, in_basin, ++basin_index,
								 j, i,
								 width, height);
			}
		}
	}

	// count sizes of the basins
	int sizes[basin_index + 1];
	memset(sizes, 0, sizeof(sizes));
	for (int i=1; i<=basin_index; i++) {
		sizes[i] = count_number_frequency(in_basin, i, height*width);
	}
	free(in_basin);

	// calculate the product of the three biggest
	quicksort(sizes, basin_index + 1);
	return sizes[basin_index] * sizes[basin_index -1] * sizes[basin_index -2];
}

void expand_low_point(int* data, int* in_basin, int basin_index,
					  int column, int row,
					  int width, int height) {
	in_basin[row*width + column] = basin_index;

	visit_neighbors(data, in_basin, basin_index, column, row, column + 1, row, width, height);
	visit_neighbors(data, in_basin, basin_index, column, row, column - 1, row, width, height);
	visit_neighbors(data, in_basin, basin_index, column, row, column, row + 1 , width, height);
	visit_neighbors(data, in_basin, basin_index, column, row, column, row - 1, width, height);
}

void visit_neighbors(int* data, int* in_basin, int basin_index,
					 int previous_column, int previous_row,
				     int column, int row,
					 int width, int height) {
	if ( !valid_index(column, row, width, height) ) {
		return;
	}

	int current_index = row*width + column;
	if (in_basin[current_index] == basin_index) {
		return;
	}
	if (data[current_index] == BORDER) {
		return;
	}

	int previous_index = previous_row * width + previous_column;

	if (data[current_index] > data[previous_index]) {
		in_basin[current_index] = basin_index;

		visit_neighbors(data, in_basin, basin_index, column, row, column + 1, row, width, height);
		visit_neighbors(data, in_basin, basin_index, column, row, column - 1, row, width, height);
		visit_neighbors(data, in_basin, basin_index, column, row, column, row + 1 , width, height);
		visit_neighbors(data, in_basin, basin_index, column, row, column, row - 1, width, height);
	}
}

bool valid_index(int column, int row, int width, int height) {
	if (column >= width || column < 0 || row >= height || row < 0) {
	   return false;
	} else {
		return true;
	}
}

int risk_level(int* data, int column, int row, int width, int height) {
	int elevation = data[row*width + column];

	// check left side
	if (column > 0) {
		if (elevation >= data[row*width + column - 1]) {
			return 0;
		}
	}

	// check right size
	if (column < width - 1) {
		if (elevation >= data[row*width + column + 1]) {
			return 0;
		}
	}

	// check top
	if (row > 0) {
		if (elevation >= data[(row - 1)*width + column]) {
			return 0;
		}
	}

	// check bottom
	if (row < height - 1) {
		if (elevation >= data[(row + 1)*width + column]) {
			return 0;
		}
	}

	return elevation + 1;
}
