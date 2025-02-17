---
title : "버블 정렬(Bubble Sort) 알아보기 (Python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 버블 정렬(Bubble Sort)의 개념 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 개념 및 동작 과정](#버블-정렬bubble-sort-개념-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#버블-정렬bubble-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#버블-정렬bubble-sort-특징)<br/>**
**[4. 장단점](#버블-정렬bubble-sort-장단점)<br/>**
**[5. 다른 정렬 알아보기](#다른-정렬-알아보기)<br/>**

> 이번 포스팅에서는 **`오름차순`**으로 정렬합니다.
{: .prompt-info}

---
## **버블 정렬(Bubble Sort) 개념 및 동작 과정**

### **개념** 

**버블 정렬(Bubble Sort)**의 핵심은 **인접한 두 원소를 비교하고 교환**하면서 큰 값을 뒤로 밀어내는 것입니다. 
이 과정이 반복되면서 가장 큰 값이 맨 뒤로, 그 다음 큰 값이 그 앞에, 이런 식으로 정렬됩니다.     

거품이 위로 떠오르듯이 큰 값들이 리스트의 끝으로 밀려가는 모습에서 **버블(Bubble)**이라는 이름이 붙었습니다.

### **동작 과정**

인접한 두 원소를 반복적으로 비교하여, 큰 값을 뒤로 밀어내는 방식으로 정렬합니다. 

1. 인접한 두 원소를 비교하여 앞의 원소가 더 크다면, 두 값을 교환합니다.
2. 리스트의 끝까지 이 과정을 반복합니다.
3. 한 번의 반복(라운드)이 끝나면 가장 큰 값이 리스트의 맨 뒤에 위치합니다.
4. 다음 라운드에서는 **이미 정렬된 마지막 원소를 제외하고 반복**합니다.
5. 모든 원소가 정렬될 때까지 과정을 반복합니다.

---
## **버블 정렬(Bubble Sort) 예시 및 구현 코드**

### **예시**

**[5, 3, 8, 4, 2]를 오름차순으로 정렬해 보겠습니다.**

- 1번째 라운드 (전체 리스트를 훑음)

    ```
    [5, 3, 8, 4, 2]  # 초기 상태
    (5 > 3) -> 교환: [3, 5, 8, 4, 2]
    (5 < 8) -> 교환 안 함
    (8 > 4) -> 교환: [3, 5, 4, 8, 2]
    (8 > 2) -> 교환: [3, 5, 4, 2, 8]
    ```
    - **가장 큰 값(8)**이 맨 뒤로 이동합니다.

- 2번째 라운드 (마지막 값 8은 이미 정렬됨)

    ```
    [3, 5, 4, 2, 8]
    (3 < 5) -> 교환 안 함
    (5 > 4) -> 교환: [3, 4, 5, 2, 8]
    (5 > 2) -> 교환: [3, 4, 2, 5, 8]
    ```
    - **두 번째로 큰 값(5)**이 그 자리로 고정됩니다.

- 3번째 라운드 (마지막 두 값 5, 8은 정렬됨)

    ```
    [3, 4, 2, 5, 8]
    (3 < 4) -> 교환 안 함
    (4 > 2) -> 교환: [3, 2, 4, 5, 8]
    ```
    - **세 번째로 큰 값(4)**이 자리 잡습니다.

- 4번째 라운드 (마지막 세 값 4, 5, 8은 정렬됨)

    ```
    [3, 2, 4, 5, 8]
    (3 > 2) -> 교환: [2, 3, 4, 5, 8]
    ```
    - **나머지 작은 값들**이 정렬됩니다.

- 5번째 라운드 (이미 모든 값 정렬 완료)

    ```
    [2, 3, 4, 5, 8]
    ```

---
### **구현 코드**     
- **Python**

    ```python
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    data = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(data) #[11, 12, 22, 25, 34, 64, 90]
    ```

- **C++**

    ```cpp
    #include <iostream>
    using namespace std;

    void bubbleSort(int arr[], int n) {
        for (int i=0; i<n-1; i++) {
            for (int j=0; j<n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    swap(arr[j], arr[j+1]);
                }
            }
        }
    }

    int main() {
        int arr[] = {64, 34, 25, 12, 22, 11, 90};
        int n = sizeof(arr)/sizeof(arr[0]);
        bubbleSort(arr, n); //11, 12, 22, 25, 34, 64, 90
        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;

    class Program
    {
        static void BubbleSort(int[] arr)
        {
            int n = arr.Length;
            for (int i=0; i<n-1; i++)
            {
                for (int j=0; j<n-i-1; j++)
                {
                    if (arr[j] > arr[j+1])
                    {
                        // Swap arr[j] and arr[j + 1]
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }

        static void Main()
        {
            int[] arr = new int[] {64, 34, 25, 12, 22, 11, 90};
            BubbleSort(arr); //11, 12, 22, 25, 34, 64, 90
        }
    }
    ```

---
## **버블 정렬(Bubble Sort) 특징**

- **제자리 정렬 (In-place Sort)** 
    - 추가적인 메모리 공간을 사용하지 않고 배열 내에서 정렬을 수행합니다.

- **안정 정렬 (Stable Sort)** 
    - 같은 값의 요소 간에 순서를 유지합니다.

- **단순한 구조** 
    - 구현이 간단하여 교육용으로 자주 사용됩니다.

- **효율성**
    - 대량의 데이터 정렬에 비효율적이며, 다른 알고리즘에 비해 속도가 느립니다. 

- **시간 복잡도**
    - **최선**: $ O(n) $ (정렬된 경우, 단 한 번의 비교만 필요)
    - **최악**: $ O(n^2) $ (역순으로 정렬된 경우)
    - **평균**: $ O(n^2) $

- **공간 복잡도**
   - $ O(1) $

---
## **버블 정렬(Bubble Sort) 장단점**

- **장점**
    - 구현이 간단하고 직관적입니다.
    - 적은 수의 데이터에 대해 경우에 따라 효율적일 수 있습니다.

- **단점**
    - 대량의 데이터를 정렬할 때 비효율적입니다.
    - $ O(n^2) $ 시간 복잡도로 인해 대규모 데이터 세트에서는 성능이 좋지 않습니다.

---
## 다른 정렬 알아보기
- **[삽입 정렬(Insertion Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Insertion-Sort/)**
- **[선택 정렬(Selection Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Selection-Sort/)**
- **[퀵 정렬(Quick Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Quick-Sort/)**
- **[병합 정렬(Merge Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Merge-Sort/)**
- **[힙 정렬(Heap Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Heap-Sort/)**
- **[계수 정렬(Counting Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Counting-Sort/)**

---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.