#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	while (1) {
		int k;
		cin >> k;
		if (k == 0) {
			return 0;
		}
		vector<int> v(k);
		vector<bool> use(k);

		for (int i = 0; i < 6; i++) {
			use[i] = 1;
		}
		for (int i = 0; i < k; i++) {
			cin >> v[i];
		}
		sort(v.begin(), v.end());
		
		do {
			for (int i = 0; i < k; i++) {
				if (use[i]) {
					cout << v[i] << " ";
				}
			}
			cout << "\n";
		} while (prev_permutation(use.begin(), use.end()));
		cout << '\n';
	}
	return 0;
}