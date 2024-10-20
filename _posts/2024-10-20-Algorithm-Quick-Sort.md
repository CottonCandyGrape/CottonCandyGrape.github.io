---
title : "퀵 정렬(Quick Sort) 알아보기 (python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 퀵 정렬(Quick Sort)의 개념 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 개념 및 동작 과정](#퀵-정렬quick-sort-개념-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#퀵-정렬quick-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#퀵-정렬quick-sort-특징)<br/>**
**[4. 장단점](#퀵-정렬quick-sort-장단점)<br/>**

---
## **퀵 정렬(Quick Sort) 개념 및 동작 과정**

### **개념** 
퀵 정렬은 **피벗(pivot)**을 기준으로 데이터를 작은 값은 왼쪽, 큰 값은 오른쪽으로 나누어 정렬하는 **분할 정복(Divide and Conquer)** 알고리즘입니다. 
나눠진 부분 배열에 대해 같은 과정을 **재귀적으로 반복**하여 정렬을 완성합니다.

### **동작 과정**
1. **분할(Divide)**
    - 리스트에서 하나의 요소를 **피벗(pivot)**으로 선택합니다. 
        - 일반적으로 리스트의 첫 번째 요소, 마지막 요소 또는 중간 요소를 피벗으로 선택할 수 있습니다. 
    - **피벗을 기준으로 리스트를 두 부분으로 분할합니다.**
    - **피벗**보다 <u>작은 요소들은 피벗의 왼쪽 부분</u>으로, 피벗보다 <u>큰 요소들은 피벗의 오른쪽 부분</u>으로 이동합니다.

2. **정복(Conquer)** 
    - 피벗을 기준으로 분할된 두 개의 하위 리스트에 대해 **재귀적으로 퀵 정렬을 수행**합니다. 
        - 이 과정은 리스트의 크기가 0 또는 1이 될 때까지 반복됩니다. 
    - <u>리스트의 크기가 0 또는 1이면 이미 정렬된 상태로 간주합니다.</u>

3. **결합(Combine)**
    - 분할된 리스트들이 모두 정렬되면, 이들을 결합하여 최종 정렬된 리스트를 얻습니다. 
    - 결합 과정이 따로 필요하지 않고 **재귀 호출이 완료되면서 자연스럽게 리스트가 정렬됩니다.**

---
## **퀵 정렬(Quick Sort) 예시 및 구현 코드**

### **예시**

**[5, 3, 8, 4, 2, 7, 1, 10]을 오름차순으로 정렬해 보겠습니다.**

- 1단계 : **피벗 선택**
    - 배열의 첫 번째 원소나 마지막 원소를 피벗으로 고를 수 있습니다. 여기서는 **5를 피벗**으로 선택합니다.

    ```
    배열: [5, 3, 8, 4, 2, 7, 1, 10]
    피벗: 5
    ```

- 2단계 : **피벗을 기준으로 분할**
    - **5**보다 **작거나 같은 값은 왼쪽**으로, **큰 값은 오른쪽**으로 보냅니다.

    ```
    왼쪽: [3, 4, 2, 1]
    피벗: 5
    오른쪽: [8, 7, 10]
    ```

- 3단계 : **재귀적 정렬**
    - **왼쪽 부분 배열 [3, 4, 2, 1]**과 **오른쪽 부분 배열 [8, 7, 10]**을 각각 정렬합니다.

    ```
    (1) 왼쪽 배열 [3, 4, 2, 1] 정렬
    피벗: 3
    왼쪽: [2, 1], 피벗: 3, 오른쪽: [4] //분할 

    왼쪽 배열 [2, 1]을 다시 정렬합니다.
    피벗: 2
    왼쪽: [1], 피벗: 2, 오른쪽: [] //분할
    정렬된 결과: [1, 2]

    왼쪽 배열 최종 결과: [1, 2, 3, 4]
    ```

    ```
    (2) 오른쪽 배열 [8, 7, 10] 정렬
    피벗: 8
    왼쪽: [7], 피벗: 8, 오른쪽: [10] //분할

    정렬된 결과: [7, 8, 10]
    ```

- 4단계 : **전체 배열 합치기**
    - 이제 정렬된 두 부분 배열과 피벗을 합칩니다.

    ```
    왼쪽: [1, 2, 3, 4]
    피벗: 5
    오른쪽: [7, 8, 10]
    ```

**최종 결과: [1, 2, 3, 4, 5, 7, 8, 10]**

---
### **구현 코드**     

- **Python**

    ```python
    def quick_sort(arr):
        if len(arr) <= 1:  # 배열의 길이가 1 이하이면 정렬 불필요
            return arr

        pivot = arr[len(arr) // 2]  # 중간 값으로 피벗 선택
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

    # 사용 예시
    arr = [5, 3, 8, 4, 2, 7, 1, 10]
    print(quick_sort(arr)) # [1, 2, 3, 4, 5, 7, 8, 10]
    ```

- **C++**

    ```cpp
    #include <iostream>
    #include <vector>
    using namespace std;

    void quick_sort(vector<int>& arr, int low, int high) {
        if (low >= high) return;

        int pivot = arr[high];  // 마지막 원소를 피벗으로 선택
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);

        int pivot_index = i + 1;
        quick_sort(arr, low, pivot_index - 1);
        quick_sort(arr, pivot_index + 1, high);
    }

    // 사용 예시
    int main() {
        vector<int> arr = {5, 3, 8, 4, 2, 7, 1, 10};
        quick_sort(arr, 0, arr.size() - 1); // [1, 2, 3, 4, 5, 7, 8, 10]
        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;

    class Program {
        static void QuickSort(int[] arr, int low, int high) {
            if (low >= high) return;

            int pivot = arr[high];  // 마지막 원소를 피벗으로 선택
            int i = low - 1;

            for (int j = low; j < high; j++) {
                if (arr[j] < pivot) {
                    i++;
                    Swap(arr, i, j);
                }
            }
            Swap(arr, i + 1, high);

            int pivotIndex = i + 1;
            QuickSort(arr, low, pivotIndex - 1);
            QuickSort(arr, pivotIndex + 1, high);
        }

        static void Swap(int[] arr, int a, int b) {
            int temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        }

        static void Main() {
            int[] arr = {5, 3, 8, 4, 2, 7, 1, 10};
            QuickSort(arr, 0, arr.Length - 1); // [1, 2, 3, 4, 5, 7, 8, 10]
        }
    }
    ```

---
## **퀵 정렬(Quick Sort) 특징**

- **제자리 정렬 (In-place Sort)** 
    - 단, 재귀 호출 스택에 메모리가 사용됩니다. (최악의 경우 스택 깊이 $O(n)$)

- **불안정 정렬 (Unstable Sort)** 
    -  동일한 원소의 순서가 보장되지 않습니다.

- **시간 복잡도** 
    - **최선(균형있게 분할될 때)** : $O(nlogn)$
    - **평균** : $O(nlogn)$
    - **최악(매번 피벗이 가장 크거나 작은 값을 선택할 때)** : $O(n^2)$

- **공간 복잡도**
    - **평균** : $O(logn)$ (재귀 호출 스택의 깊이)
    - **최악** : $O(n)$ (재귀 호출이 깊게 일어날 때)
    
---
## **퀵 정렬(Quick Sort) 장단점**

- **장점**
    - **빠른 평균 성능**  
       - 평균 시간 복잡도가 $O(nlogn)$으로 **대부분의 경우 매우 빠릅니다.**
       - **대규모 데이터셋에서 효율적**이며, **힙 정렬(heap sort)**이나 **병합 정렬(merge sort)**보다 실전에서 빠른 경우가 많습니다.

    - **구현이 간단함**  
       - **피벗 선택**과 **재귀 호출**만으로 간단하게 구현할 수 있습니다.

    - **캐시 친화적**  
       - 메모리 접근이 연속적이어서 캐시 메모리의 활용이 좋아 실제 성능이 뛰어납니다.


- **단점**
    - **최악의 경우 시간 복잡도** $O(n^2)$ 
       - 피벗이 매번 가장 큰 값이나 작은 값으로 선택될 때, 정렬 성능이 크게 저하됩니다.  
       - 이미 정렬된 배열에서 성능이 나빠질 수 있습니다.

    - **재귀 호출 문제**  
       - 재귀 호출이 깊어지면 **스택 오버플로(Stack Overflow)**가 발생할 수 있습니다.  
       - 최악의 경우 **공간 복잡도** $O(n)$이 됩니다.  

퀵 정렬은 **빠르고 메모리 효율적**인 장점이 있지만, 피벗 선택에 따라 **최악의 시간 복잡도** $O(n^2)$ 가 될 위험이 있습니다.
이러한 문제를 개선하기 위해 **랜덤 피벗 선택**과 같은 최적화 기법이 자주 사용됩니다.


---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.
