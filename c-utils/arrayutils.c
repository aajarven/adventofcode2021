#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int* split_decimal_to_digits(int input, int n_digits) {
	/**
	 * Return a pointer to an array containing each individual digit in input.
	 */
	int* output = malloc(n_digits * sizeof(int));
	for (int i=n_digits-1; i>=0; i--) {
		output[i] = input % 10;
		input /= 10;
	}
	return output;
}

void add(int* arr1, int* arr2, int n_elements) {
	/**
	 * Add arr2 into arr1 element-wise. Modifies arr1 in place.
	 */
	for (int i=0; i<n_elements; i++) {
		arr1[i] += arr2[i];
	}
}

void print_int_array(int* arr, int n_elements) {
	printf("[ ");
	for (int i=0; i<n_elements; i++) {
		printf("%d ", arr[i]);
	}
	printf("]\n");
}

void print_2d_int_array(int* arr, int n_rows, int row_length) {
	for (int i=0; i<n_rows; i++) {
		printf("[ ");
		for (int j=0; j<row_length; j++) {
			printf("%d ", arr[i*row_length + j]);
		}
		printf("]\n");
	}
}

int* char_array_to_digits(char* arr, int n_rows, int data_row_length, int extra_chars) {
	/**
	 * Return a new array containing the digits in the given array.
	 *
	 * Each row must be the same length. row_length represents the length
	 * of the data: after this can be a number of extra characters that are not
	 * considered when crafting the new array.
	 */
	int* digits = malloc(n_rows * data_row_length * sizeof(int));
	int line_length = data_row_length + extra_chars;
	for (int i=0; i<n_rows; i++) {
		for (int j=0; j<data_row_length; j++) {
			char current_char[1];
			memcpy(current_char, &arr[i*line_length + j], sizeof(char));
			int digit = atoi(current_char);
			digits[i*data_row_length + j] = digit;
		}
	}
	return digits;
}


int sum(int* arr, int len) {
    /**
     * Return the sum of the integers in the given array.
     */
    int sum = 0;
    for (int i=0; i<len; i++) {
        sum += arr[i];
    }
    return sum;
}


long long_sum(long* arr, int len) {
    /**
     * Return the sum of the long integers in the given array.
     */
    long sum = 0;
    for (int i=0; i<len; i++) {
        sum += arr[i];
    }
    return sum;
}

int count_number_frequency(int* arr, int counted_number, int n_elements) {
	/**
	 * Return the number of times a given number is found in the given array.
	 */
	int count = 0;
	for (int i=0; i<n_elements; i++) {
		if (arr[i] == counted_number) {
			count++;
		}
	}
	return count;

}

void quicksort(int* arr, int len) {
	/**
	 * Sort given array in place
	 */
	if (len < 2) {
		return;
	}

	int pivot = arr[len/2];

	int start = 0;
	int end = len - 1;
	while (start < end) {
		while (arr[start] < pivot) {
			start++;
		}
		while (arr[end] > pivot) {
			end--;
		}

		if (start < end) {
			int tmp = arr[start];
			arr[start] = arr[end];
			arr[end] = tmp;

			start++;
			end--;
		}
	}

	quicksort(arr, start);
	quicksort(arr + start, len - start);
}

void quicksort_long(long* arr, int len) {
	/**
	 * Sort given array in place
	 */
	if (len < 2) {
		return;
	}

	long pivot = arr[len/2];

	long start = 0;
	long end = len - 1;
	while (start < end) {
		while (arr[start] < pivot) {
			start++;
		}
		while (arr[end] > pivot) {
			end--;
		}

		if (start < end) {
			long tmp = arr[start];
			arr[start] = arr[end];
			arr[end] = tmp;

			start++;
			end--;
		}
	}

	quicksort_long(arr, start);
	quicksort_long(arr + start, len - start);
}
