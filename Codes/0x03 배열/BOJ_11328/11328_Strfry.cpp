#include <iostream>

using namespace std;

/**
 * @brief  무작위 재배열이 가능한지를 확인하는 코드입니다. map을 활용하면 더욱 효율적일 것이나, 배열로 푸는 것이 목적으로 보입니다.
 * @return
 */
int main() {
    int eng_arr[26];
    int num = 0;

    cin >> num;

    while (num--) {
        fill_n(eng_arr, 26, 0);
        string eng;
        cin >> eng;
        for (auto i: eng)
            eng_arr[i - 'a']++;

        cin >> eng;
        for (auto i: eng) {
            if (--eng_arr[i - 'a'] < 0) {
                cout << "Impossible" << "\n";
                goto cont;
            }
        }
        for (auto i: eng_arr) {
            if (i != 0) {
                cout << "Impossible" << "\n";
                goto cont;
            }
        }
        cout << "Possible" << "\n";
        cont:;
    }

    return 0;
}