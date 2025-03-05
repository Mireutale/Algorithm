#include <iostream>

using namespace std;

/**
 * @brief 필요한 플라스틱 숫자 개수를 판별하는 문제입니다.
 * @return null
 */
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int arr[10] = {0,};
    int min = 0;
    string num;
    cin >> num;

    for (char c : num) {
        arr[c - '0']++;
    }

    for (int i = 0; i<=9; ++i) {
        if ((i != 6 && i != 9)) {
            if (min < arr[i]) min = arr[i];
        }
    }

    cout << max((arr[6] + arr[9] + 1) / 2, min);

    return 0;
}
