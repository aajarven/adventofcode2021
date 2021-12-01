

int increases(int* depths, int n_depths) {
	int increases = 0;
	for (int i=1; i<n_depths; i++) {
		if (depths[i] > depths[i-1]) {
			increases++;
		}
	}
	return increases;
}
