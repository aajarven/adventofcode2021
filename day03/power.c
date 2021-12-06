#include<stdbool.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include"../c-utils/arrayutils.h"

int to_decimal(int* binary_array, int n_bits);
int* char_to_binary(char* char_array, int n_bits);
int gamma_power(int* one_counts, int n_measurements, int threshold);
int epsilon_power(int* one_counts, int n_measurements, int threshold);
int oxygen(int* report, int len_report, int measurement_length);
int co2(int* report, int len_report, int measurement_length);
bool not_discarded(int* entry, int* known_measurements, int measurement_length);


int power(char* report, int len_report, int n_measurements) {
	int one_counts[n_measurements];
	memset(one_counts, 0, sizeof one_counts);

	int line_length = n_measurements + 2; // account for newline and null

	for (int i=0; i<len_report; i++) {
		int* entries = char_to_binary(&report[i*line_length], n_measurements);

		add(one_counts, entries, n_measurements);
		free(entries);
	}

	int threshold = len_report/2;

	return gamma_power(one_counts, n_measurements, threshold)
		   *
		   epsilon_power(one_counts, n_measurements, threshold);
}

int lifesupport(int* report, int len_report, int measurement_length) {
	int oxygen_rating = oxygen(report, len_report, measurement_length);
	int co2_rating = co2(report, len_report, measurement_length);
	printf("oxygen: %d\n", oxygen_rating);
	printf("co2: %d\n", co2_rating);
	return oxygen_rating * co2_rating;
}

int oxygen(int* report, int len_report, int measurement_length) {
	int known_measurements[measurement_length];
	memset(known_measurements, -1, sizeof known_measurements);

	int last_included_index;

	for (int i=0; i<measurement_length; i++) {
		int included_measurements = 0;
		int ones = 0;
		int zeros = 0;
		for (int j=0; j<len_report; j++) {
			if (not_discarded(&report[j*measurement_length], known_measurements, measurement_length)) {
				included_measurements++;
				last_included_index = j;
				ones += report[j*measurement_length + i];
				zeros += report[j*measurement_length + i] == 1 ? 0 : 1;
			}
		}
		if (included_measurements == 1) {
			return to_decimal(&report[last_included_index*measurement_length], measurement_length);
		}
		known_measurements[i] = ones >= zeros;
	}
	return to_decimal(known_measurements, measurement_length);
}

int co2(int* report, int len_report, int measurement_length) {
	int known_measurements[measurement_length];
	memset(known_measurements, -1, sizeof known_measurements);

	int last_included_index;

	for (int i=0; i<measurement_length; i++) {
		int included_measurements = 0;
		int ones = 0;
		int zeros = 0;
		for (int j=0; j<len_report; j++) {
			if (not_discarded(&report[j*measurement_length], known_measurements, measurement_length)) {
				included_measurements++;
				last_included_index = j;
				ones += report[j*measurement_length + i];
				zeros += report[j*measurement_length + i] == 1 ? 0 : 1;
			}
		}

		if (included_measurements == 1) {
			return to_decimal(&report[last_included_index*measurement_length], measurement_length);
		}

		known_measurements[i] = ones >= zeros ? 0 : 1;
	}
	return to_decimal(known_measurements, measurement_length);
}

bool not_discarded(int* entry, int* known_measurements, int measurement_length) {
	for (int i=0; i<measurement_length; i++) {
		if (known_measurements[i] == -1) {
			return true;
		}
		if (entry[i] != known_measurements[i]) {
			return false;
		}
	}
	return true;
}

int to_decimal(int* binary_array, int n_bits) {
	int decimal = 0;
	for (int i=0; i<n_bits; i++) {
		decimal += pow(2, i) * binary_array[n_bits - i - 1];
	}
	return decimal;
}

int* char_to_binary(char* char_array, int n_bits) {
	int* output = malloc(n_bits * sizeof(int));
	for (int i=0; i<n_bits; i++) {
		output[i] = char_array[i] == '1';
	}
	return output;
}

int gamma_power(int* one_counts, int n_measurements, int threshold) {
	int power = 0;

	for (int i=0; i<n_measurements; i++) {
		power += pow(2, n_measurements-i-1) * (one_counts[i]<threshold ? 1 : 0);
	}
	return power;
}

int epsilon_power(int* one_counts, int n_measurements, int threshold) {
	int power = 0;

	for (int i=0; i<n_measurements; i++) {
		power += pow(2, n_measurements-i-1) * (one_counts[i]>threshold ? 1 : 0);
	}
	return power;
}
