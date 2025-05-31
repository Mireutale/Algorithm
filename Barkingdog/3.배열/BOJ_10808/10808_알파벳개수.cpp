#include <iostream>

using namespace std;

/**
 * @brief 백준 10808 알파벳 개수
 * @authors KimGiyun
 * @return null
 */
int main() {
    int eng_arr[26] = {0,};
    string lower_case_str;
    cin >> lower_case_str; // String 입력

    for (auto i: lower_case_str) eng_arr[i - 'a']++; // ASCII 코드 활용
    for (auto i: eng_arr) cout << i << " "; // 출력부

    return 0;
}