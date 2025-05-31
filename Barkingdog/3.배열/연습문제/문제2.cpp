#include <iostream>

using namespace std;

/**
 * @brief func2 함수는 배열 내 임의의 두 숫자 간 합이 100이 되면 1을, 아니면 0을 반환합니다.
 * @author KimGiyun
 * @param arr 배열
 * @param N 배열 내 원소 개수
 * @return if (num1+num2 == 100) 1 else 0
 */
int func2(const int arr[], int N){
    bool num_arr[101] = {false,};

    for(int i = 0; i<N; ++i){
        if(num_arr[100-arr[i]])
            return 1;
        num_arr[arr[i]] = true;
    }
    return 0;
}

int main(){
    int arr[] = {4, 13, 63, 87};
    cout << func2(arr, 4) << "\n";
    return 0;
}
