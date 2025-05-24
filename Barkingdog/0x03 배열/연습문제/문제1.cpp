#include <iostream>

using namespace std;

void insert(int idx, int num, int arr[], int &len) {
    for (int i = len - 1; i > idx; --i)
        arr[i] = arr[i - 1];
    arr[idx] = num;
    len++;
}

void erase(int idx, int arr[], int &len) {
    for (int i = idx; i < len - 2; ++i)
        arr[i] = arr[i + 1];
    len--;
}

int main() {
    int arr[10] = {10, 50, 40, 30, 70, 20, 0, 0, 0, 0};
    int len = sizeof(arr) / 4;
    cout << "------ array ------\n";
    for (auto i: arr)
        cout << i << " "; // 10 50 40 30 70 20 0 0 0 0

    insert(3, 60, arr, len);
    cout << "\n------ insert ------\n";
    for (auto i: arr)
        cout << i << " "; // 10 50 40 60 30 70 20 0 0 0

    erase(4, arr, len);
    cout << "\n------ erase ------\n";
    for (auto i: arr)
        cout << i << " "; // 10 50 40 60 70 20 0 0 0 0

    cout << "\n------ result ------\n";
    for (auto i: arr)
        cout << i << " "; // 10 50 40 60 70 20 0 0 0 0
    return 0;
}
