

int increases(int* depths, int n_depths) {
	int increases = 0;
	for (int i=1; i<n_depths; i++) {
		if (depths[i] > depths[i-1]) {
			increases++;
		}
	}
	return increases;
}


int windowed_increases(int* depths, int n_depths) {
	/**
	 * Count how many three-measurement windows are deeper than the previous
	 * one.
	 *
	 * This is done by moving a "core" of two consecutive measurements along
	 * the array, and counting how many times core + measurement after is
	 * deeper than core + measurement before. After each comparison, the first
	 * depth in the core of the window is substracted from the total depth in
	 * the window, and the depth right after the core is added to it.
	 */
	int increases = 0;
	int window_core = depths[1] + depths[2];

	for (int i=3; i<n_depths; i++) {
		int depth_before = depths[i-3];
		int depth_after = depths[i];
		if (window_core + depth_after > window_core + depth_before) {
			increases++;
		}
		window_core = window_core - depths[i-2] + depth_after;
	}
	return increases;
}
