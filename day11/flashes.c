#include<stdbool.h>
#include<stdlib.h>
#include<string.h>
#include"../c-utils/arrayutils.h"

#define NOT_FLASHED 0
#define FLASHED 1

int step(int* data, int width, int height);
void charge_octopus(int* data, int* flash_status, int x, int y, int width, int height);


int flashes(int* data, int width, int height) {
    int flash_count = 0;
    for (int i=0; i<100; i++) {
        flash_count += step(data, width, height);
    }
    return flash_count;
}

int synchronized_after_steps(int* data, int width, int height) {
    int steps = 1;
    while ( step(data, width, height) != width*height ) {
        steps++;
    }
    return steps;
}

bool valid_coordinates(int x, int y, int width, int height) {
    return ( x >= 0 && x < width && y >= 0 && y < height);
}

int step(int* data, int width, int height) {
    int n_octopuses = width * height;
    int* flash_status = malloc(n_octopuses * sizeof(int));
    memset(flash_status, NOT_FLASHED, n_octopuses * sizeof(int));

    for (int y=0; y<height; y++) {
        for (int x=0; x<width; x++) {
            charge_octopus(data, flash_status, x, y, width, height);
        }
    }

    int flashes = sum(flash_status, n_octopuses);
    free(flash_status);
    return flashes;
}


void charge_octopus(int* data, int* flash_status, int x, int y, int width, int height) {
    if ( !valid_coordinates(x, y, width, height) ) {
        return;
    }

    int octopus_index = y*width + x;

    if (flash_status[octopus_index] == FLASHED) {
        return;
    }

    data[octopus_index]++;
    if (data[octopus_index] == 10) {
        flash_status[octopus_index] = FLASHED;
        data[octopus_index] = 0;
        for (int i=-1; i<=1; i++) {
            for (int j=-1; j<=1; j++) {
                if ( i==0 && j==0 ) {
                    continue;
                }
                charge_octopus(data, flash_status, x+i, y+j, width, height);
            }
        }
    }
}
