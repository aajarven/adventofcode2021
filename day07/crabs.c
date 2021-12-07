#include<stdlib.h>
#include <limits.h>
#include"../c-utils/arrayutils.h"

int total_fuel_to(int* initial_positions, int destination, int n_crabs);
int total_crab_engineering_fuel_to(int* initial_positions, int destination, int n_crabs);


int least_fuel_to_alignment(int* initial_positions, int n_crabs, int max_coordinate) {
	int min_fuel = INT_MAX;
	for (int destination=0; destination<max_coordinate; destination++) {
		int fuel_to_destination = total_fuel_to(initial_positions, destination, n_crabs);
		min_fuel = fuel_to_destination < min_fuel ? fuel_to_destination : min_fuel;
	}
	return min_fuel;
}


int total_fuel_to(int* initial_positions, int destination, int n_crabs) {
	int distances[n_crabs];
	for (int i=0; i<n_crabs; i++) {
		distances[i] = abs(initial_positions[i] - destination); 
	}
	return sum(distances, n_crabs);
}


int least_crab_engineering_fuel_to_alignment(int* initial_positions, int n_crabs, int max_coordinate) {
	int min_fuel = INT_MAX;
	for (int destination=0; destination<max_coordinate; destination++) {
		int fuel_to_destination = total_crab_engineering_fuel_to(initial_positions, destination, n_crabs);
		min_fuel = fuel_to_destination < min_fuel ? fuel_to_destination : min_fuel;
	}
	return min_fuel;
}


int total_crab_engineering_fuel_to(int* initial_positions, int destination, int n_crabs) {
	int distances[n_crabs];
	for (int i=0; i<n_crabs; i++) {
		int traditional_distance = abs(initial_positions[i] - destination);
		distances[i] = traditional_distance * (1 + traditional_distance) / 2;
	}
	return sum(distances, n_crabs);
}
