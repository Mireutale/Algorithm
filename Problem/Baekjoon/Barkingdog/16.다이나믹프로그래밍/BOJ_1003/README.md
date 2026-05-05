# 백준 1003번 - 피보나치 함수

[문제 보러 가기](https://www.acmicpc.net/problem/1003)

## 요약

피보나치(N) 호출 시 0과 1이 각각 몇 번 출력되는지 구하는 프로그램

## 핵심 규칙

```
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
```

위 피보나치 함수 코드에 대해서, 출력되는 fibonacci(0)과 fibonacci(1)의 개수를 구하는 프로그램ㅎ

## 예제 입출력

입력 및 출력 예시는 [문제 링크](https://www.acmicpc.net/problem/1003) 참고.

## 문제풀이

1. 로직

fibonacci(0) = 0

fibonacci(1) = 1

fibonacci(2) = fibonacci(1) + fibonacci(0)

fibonacci(3) = fibonacci(2) + fibonacci(1) = 2 \* fibonacci(1) + fibonacci(0)

fibonacci(4) = fibonacci(3) + fibonacci(2) = 3 _ fibonacci(1) + 2 _ fibonacci(0)

fibonacci(5) = fibonacci(4) + fibonacci(3) = 5 _ fibonacci(1) + 3 _ fibonacci(0)

fibonacci(6) = fibonacci(5) + fibonacci(4) = 8 _ fibonacci(1) + 5 _ fibonacci(0)

결국 fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) 이므로, n-1과 n-2에서 구할 수 있는 0과 1의 출력 수를 더하면 된다.

이때 0과 1을 잘 보면..?

fibo[1]은 0, 1, 1, 2, 3, 5, 8 .. 그냥 피보나치 수열과 같음

fibo[0]은 1, 0, 1, 1, 2, 3, 5 .. 0 제외 1부터 피보나치 수열과 같음, 즉 기본적인 fibo[n-1]
