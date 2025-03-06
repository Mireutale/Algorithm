#include <iostream>
#include <vector>
using namespace std;

/**
 * @brief  무작위 재배열이 가능한지를 확인하는 코드입니다. map을 활용하면 더욱 효율적일 것이나, 배열로 푸는 것이 목적으로 보입니다.
 * @return
 */
void func1() {
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
}

/**
 * @brief 이런 방법도 있음. 벡터 컨테이너로 비교하는 방식.
 */
void func2(){
    int num = 0;
    cin >> num;
    while(num--){
        vector<int> vecFirst(26, 0);
        vector<int> vecSecond(26, 0);
        string FirstString, SecondString;
        cin >> FirstString >> SecondString;

        for (auto word : FirstString)
        {
            ++vecFirst[word - 'a'];
        }
        for (auto word : SecondString)
        {
            ++vecSecond[word - 'a'];
        }

        if(vecFirst == vecSecond)
            cout << "Possible\n";
        else
            cout << "Impossible\n";
    }
}

int main(){
    func1();
//    func2();
    return 0;
}