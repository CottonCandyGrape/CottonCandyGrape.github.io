---
title : "계수 정렬(Counting Sort) 알아보기 (python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 계수 정렬(Counting Sort)의 개념 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 개념 및 동작 과정](#계수-정렬counting-sort-개념-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#계수-정렬counting-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#계수-정렬counting-sort-특징)<br/>**
**[4. 장단점](#계수-정렬counting-sort-장단점)<br/>**
**[5. 다른 정렬 알아보기](#다른-정렬-알아보기)<br/>**

---
## **계수 정렬(Counting Sort) 개념 및 동작 과정**

### **개념** 
**계수 정렬(Counting Sort)**은 정수로 표현된 데이터의 개수를 **셈(count)**하여 정렬하는 알고리즘입니다.      
**값의 범위가 제한된 경우**에 매우 빠르게 동작하며, **비교 기반 정렬 알고리즘이 아니**라는 특징이 있습니다. 
주로 **원소의 크기 범위가 좁을 때** 유용합니다. 

### **동작 과정**
1. 입력 배열의 **최대값을 찾기**
    - 정렬할 데이터의 최대값을 기준으로 배열을 생성합니다.

2. 각 원소의 **개수를 세기**
    - 입력 배열의 원소가 등장하는 빈도를 기록한 **카운트 배열(count array)**을 만듭니다.

3. 카운트 배열을 **누적합으로 변환**
    - 누적합 배열로 변환하여 각 원소가 최종 배열에서 들어갈 위치를 계산합니다.

4. 입력 배열을 **역순으로 순회**하면서 정렬된 배열에 삽입
    - 입력 배열의 끝에서부터 순회하며 **정렬된 결과 배열**에 값을 넣습니다. 
    - **이 과정에서 안정 정렬이 보장됨.**

---
## **계수 정렬(Counting Sort) 예시 및 구현 코드**

### **예시**

**입력 배열: [1, 4, 1, 2, 7, 5, 2] 을 오름차순으로 정렬해 보겠습니다.**

1. **최대값 찾기** 및 **카운트 배열** 만들기

    - 최대값이 7이므로 인덱스 0~7까지 카운트 배열 생성.

    ```
    카운트 배열: [0, 0, 0, 0, 0, 0, 0, 0]
    ```

2. **입력 배열의 원소**를 **카운트 배열의 인덱스**로 사용하여 **원소 등장 횟수 기록**

    ```
    카운트 배열: [0, 2, 2, 0, 1, 1, 0, 1]
    ```

3. **누적합 배열** 만들기
    - 카운트 배열을 **왼쪽부터 누적**하여 **누적합 배열로 변환**합니다.
    - **누적합 배열의 값**은 해당 숫자가 결과 배열에서 들어갈 **마지막 위치 + 1**을 나타냅니다.

    ```
    누적합 배열: [0, 2, 4, 4, 5, 6, 6, 7]
    ```

4. 결과 배열에 **역순으로 값 채우기**
    - **입력 배열을 역순으로 순회**하면서, 누적합 배열을 이용해 정렬된 결과 배열에 값을 넣습니다.
    - 이 과정에서 **누적합 배열의 값이 줄어들며 원소의 위치가 계산**됩니다.

    ```
    입력 배열: [1, 4, 1, 2, 7, 5, 2]
    누적합 배열: [0, 2, 4, 4, 5, 6, 6, 7]
    초기 상태 결과 배열: [_, _, _, _, _, _, _]

    (1) 입력 배열의 마지막 원소 2
    누적합 배열의 인덱스 2 값: 4 → 2는 결과 배열의 3번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 2, 3, 4, 5, 6, 6, 7]
    결과 배열: [_, _, _, 2, _, _, _]

    (2) 다음 원소 5
    누적합 배열의 인덱스 5 값: 6 → 5는 결과 배열의 5번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 2, 3, 4, 5, 5, 6, 7]
    결과 배열: [_, _, _, 2, _, 5, _]

    (3) 다음 원소 7
    누적합 배열의 인덱스 7 값: 7 → 7은 결과 배열의 6번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 2, 3, 4, 5, 5, 6, 6]
    결과 배열: [_, _, _, 2, _, 5, 7]

    (4) 다음 원소 2
    누적합 배열의 인덱스 2 값: 3 → 2는 결과 배열의 2번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 2, 2, 4, 5, 5, 6, 6]
    결과 배열: [_, _, 2, 2, _, 5, 7]

    (5) 다음 원소 1
    누적합 배열의 인덱스 1 값: 2 → 1은 결과 배열의 1번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 1, 2, 4, 5, 5, 6, 6]
    결과 배열: [_, 1, 2, 2, _, 5, 7]

    (6) 다음 원소 4
    누적합 배열의 인덱스 4 값: 5 → 4는 결과 배열의 4번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 1, 2, 4, 4, 5, 6, 6]
    결과 배열: [_, 1, 2, 2, 4, 5, 7]

    (7) 마지막 원소 1

    누적합 배열의 인덱스 1 값: 1 → 1은 결과 배열의 0번 위치에 배치됩니다.
    누적합 배열 업데이트: [0, 0, 2, 4, 4, 5, 6, 6]
    결과 배열: [1, 1, 2, 2, 4, 5, 7]

    최종 정렬된 배열
    [1, 1, 2, 2, 4, 5, 7]
    ```

---
### **구현 코드**     

- **Python**

    ```python
    def counting_sort(arr):
        max_value = max(arr)  # 배열의 최대값 찾기
        count = [0] * (max_value + 1)  # 카운트 배열 생성

        # 1. 각 숫자의 등장 횟수 카운트
        for num in arr:
            count[num] += 1

        # 2. 누적합 계산
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # 3. 결과 배열 생성 및 역순으로 값 채우기
        result = [0] * len(arr)
        for num in reversed(arr):
            count[num] -= 1
            result[count[num]] = num

        return result

    arr = [1, 4, 1, 2, 7, 5, 2]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)  # [1, 1, 2, 2, 4, 5, 7]
    ```

- **C++**

    ```cpp
    #include <iostream>
    #include <vector>
    #include <algorithm>  // std::max

    std::vector<int> countingSort(const std::vector<int>& arr) {
        int max_value = *std::max_element(arr.begin(), arr.end());
        std::vector<int> count(max_value + 1, 0);

        // 1. 각 숫자의 등장 횟수 카운트
        for (int num : arr) {
            count[num]++;
        }

        // 2. 누적합 계산
        for (int i = 1; i < count.size(); ++i) {
            count[i] += count[i - 1];
        }

        // 3. 결과 배열 생성 및 역순으로 값 채우기
        std::vector<int> result(arr.size());
        for (int i = arr.size() - 1; i >= 0; --i) {
            count[arr[i]]--;
            result[count[arr[i]]] = arr[i];
        }

        return result;
    }

    int main() {
        std::vector<int> arr = {1, 4, 1, 2, 7, 5, 2};
        std::vector<int> sorted_arr = countingSort(arr); // [1, 1, 2, 2, 4, 5, 7]
        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;

    class Program
    {
        static int[] CountingSort(int[] arr)
        {
            int max_value = arr.Max();
            int[] count = new int[max_value + 1];

            // 1. 각 숫자의 등장 횟수 카운트
            foreach (int num in arr)
            {
                count[num]++;
            }

            // 2. 누적합 계산
            for (int i = 1; i < count.Length; i++)
            {
                count[i] += count[i - 1];
            }

            // 3. 결과 배열 생성 및 역순으로 값 채우기
            int[] result = new int[arr.Length];
            for (int i = arr.Length - 1; i >= 0; i--)
            {
                count[arr[i]]--;
                result[count[arr[i]]] = arr[i];
            }

            return result;
        }

        static void Main(string[] args)
        {
            int[] arr = { 1, 4, 1, 2, 7, 5, 2 };
            int[] sorted_arr = CountingSort(arr); // [1, 1, 2, 2, 4, 5, 7]
        }
    }
    ```

---
## **계수 정렬(Counting Sort) 특징**

- **제자리 정렬 (In-place Sort)이 아닙니다.**
    - 추가적인 메모리를 사용해야 합니다.

- **안정 정렬 (Unstable Sort)** 
    - 입력 배열을 **역순으로 순회**해야 안정 정렬이 보장됩니다.

- **시간 복잡도** 
    - $O(n+k)$

- **공간 복잡도**
    - $O(n+k)$
    
---
## **계수 정렬(Counting Sort) 장단점**

- **장점**
    - 매우 빠름 
        - 값의 범위가 작을 때 $O(n)$ 에 가까운 성능을 보임.

- **단점**
    - 값의 범위가 너무 넓으면 비효율적(공간 복잡도 증가).
         - 예를 들면 **입력 배열이 [0, 99999]인 경우**
         
    - 실수(float)와 같은 자료형에는 사용이 어려움.

---
## 다른 정렬 알아보기
- **[버블 정렬(Bubble Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Bubble-Sort/)**
- **[삽입 정렬(Insertion Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Insertion-Sort/)**
- **[선택 정렬(Selection Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Selection-Sort/)**
- **[퀵 정렬(Quick Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Quick-Sort/)**
- **[병합 정렬(Merge Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Merge-Sort/)**
- **[힙 정렬(Heap Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Heap-Sort/)**

---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.
