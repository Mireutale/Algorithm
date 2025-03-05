#include <iostream>

using namespace std;

/**
 * @brief 세 숫자 간 곱한 결과 값에 0-9가 사용된 빈도수를 출력하는 문제입니다.
 * @return null
 */
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int arr[10] = {0,};
    int a, b, c;
    cin >> a >> b >> c;
    a = a * b * c;
    while (a > 0) {
        arr[a % 10]++;
        a /= 10;
    }

    for (auto i: arr) cout << i << "\n";

    return 0;
}
