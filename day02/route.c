#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include"route.h"


int position_product(char* route, int line_length, int moves) {
	int x = 0;
	int y = 0;
	char* direction = malloc(line_length * sizeof(char));
	int distance = 0;

	for (int line=0; line<moves; line++) {
		sscanf(&route[line*line_length], "%s %d", direction, &distance);

		if (direction[0] == 'f') {
			x += distance;
		} else if (direction[0] == 'b') {
			x -= distance;
		} else if (direction[0] == 'u') {
			y -= distance;
		} else if (direction[0] == 'd') {
			y += distance;
		}
	}

	free(direction);
	return x*y;
}


int aimed_position_product(char* route, int line_length, int moves) {
	int x = 0;
	int y = 0;
	int aim = 0;
	char* direction = malloc(line_length * sizeof(char));
	int distance = 0;

	for (int line=0; line<moves; line++) {
		sscanf(&route[line*line_length], "%s %d", direction, &distance);

		if (direction[0] == 'f') {
			x += distance;
			y += distance * aim;
		} else if (direction[0] == 'u') {
			aim -= distance;
		} else if (direction[0] == 'd') {
			aim += distance;
		}
	}

	free(direction);
	return x*y;
}
