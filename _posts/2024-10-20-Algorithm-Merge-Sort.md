---
title : "병합 정렬(Merge Sort) 알아보기 (python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 병합 정렬(Merge Sort)의 개념 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 개념 및 동작 과정](#병합-정렬merge-sort-개념-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#병합-정렬merge-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#병합-정렬merge-sort-특징)<br/>**
**[4. 장단점](#병합-정렬merge-sort-장단점)<br/>**
**[5. 다른 정렬 알아보기](#다른-정렬-알아보기)<br/>**

---
## **병합 정렬(Merge Sort) 개념 및 동작 과정**

### **개념** 
**Merge Sort**는 효율적인 정렬 알고리즘 중 하나로, **분할 정복(Divide and Conquer)** 전략을 기반으로 합니다. 
이 알고리즘은 **큰 데이터 세트를 작은 데이터 세트로 나누고, 정렬한 후 다시 합치는 방식**으로 동작합니다.

### **동작 과정**
1. **분할 (Divide)**
   - 배열을 **중간 인덱스를 기준**으로 **두 개의 하위 배열로 나눕니다.**
   - 이 과정을 반복하여 **각 배열의 크기가 1이 될 때까지** 계속 나눕니다.

2. **정복 (Conquer)**
   - 크기가 1인 배열(즉, 더 이상 분할할 수 없는 상태)은 기본적으로 정렬된 상태입니다.
   - 이제 이 배열들을 차례대로 합쳐서 정렬된 배열을 만들기 시작합니다.

3. **병합 (Merge)**
   - **두 개의 정렬된 배열을 비교하여 작은 요소부터 순서대로 새로운 배열에 추가합니다.**
   - 한 배열의 모든 요소가 다 추가되면, 다른 배열에 남아 있는 요소들을 모두 추가합니다.

---
## **병합 정렬(Merge Sort) 예시 및 구현 코드**

### **예시**

**[38, 27, 43, 3, 9, 82, 10]을 오름차순으로 정렬해 보겠습니다.**

- 1단계 : **분할 단계**:

    ```
    [38, 27, 43, 3, 9, 82, 10] → [38, 27, 43]와 [3, 9, 82, 10]

    [38, 27, 43] → [38]와 [27, 43]
    [27, 43] → [27]와 [43]

    [3, 9, 82, 10] → [3, 9]와 [82, 10]
    [3, 9] → [3]와 [9]
    [82, 10] → [82]와 [10]
    ```

- 2단계 : **정복 단계**:
    ```
    [27]와 [43]를 병합 → [27, 43]
    [38]와 [27, 43]를 병합 → [27, 38, 43]

    [3]와 [9]를 병합 → [3, 9]
    [82]와 [10]를 병합 → [10, 82]
    [3, 9]와 [10, 82]를 병합 → [3, 9, 10, 82]
    ```

- 3단계 : **최종 병합 단계**:
    ```
    [27, 38, 43]와 [3, 9, 10, 82]를 병합하여 최종 정렬된 배열을 만듭니다:
    결과: [3, 9, 10, 27, 38, 43, 82]
    ```

---
### **구현 코드**     

- **Python**

    ```python
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # 중간 인덱스 계산
            left_half = arr[:mid]  # 왼쪽 절반
            right_half = arr[mid:]  # 오른쪽 절반

            merge_sort(left_half)  # 왼쪽 절반 재귀 정렬
            merge_sort(right_half)  # 오른쪽 절반 재귀 정렬

            i = j = k = 0

            # 왼쪽과 오른쪽 배열을 비교하여 정렬
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # 남은 요소들 추가
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    arr = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr) # [3, 9, 10, 27, 38, 43, 82]   
    ```

- **C++**

    ```cpp
    #include <iostream>
    #include <vector>

    void merge(std::vector<int>& arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        std::vector<int> L(n1), R(n2);

        for (int i = 0; i < n1; ++i) //왼쪽 절반
            L[i] = arr[left + i]; 
        for (int j = 0; j < n2; ++j) //오른쪽 절반
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) { // 왼쪽과 오른쪽 배열을 비교하여 정렬
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // 남은 요소들 추가
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    void merge_sort(std::vector<int>& arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2; //중간 인덱스 계산

            merge_sort(arr, left, mid); //왼쪽 절반 재귀 정렬
            merge_sort(arr, mid + 1, right); //오른쪽 절반 재귀 정렬
            merge(arr, left, mid, right);
        }
    }

    int main() {
        std::vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
        merge_sort(arr, 0, arr.size() - 1); // [3, 9, 10, 27, 38, 43, 82]
        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;
    
    class MergeSort
    {
        public static void Merge(int[] arr, int left, int mid, int right)
        {
            int n1 = mid - left + 1;
            int n2 = right - mid;
    
            int[] L = new int[n1];
            int[] R = new int[n2];
    
            for (int i = 0; i < n1; i++) //왼쪽 절반
                L[i] = arr[left + i];
            for (int j = 0; j < n2; j++) //오른쪽 절반
                R[j] = arr[mid + 1 + j];
    
            int k = left;
            int i = 0, j = 0;
    
            while (i < n1 && j < n2) // 왼쪽과 오른쪽 배열을 비교하여 정렬
            {
                if (L[i] <= R[j])
                {
                    arr[k] = L[i];
                    i++;
                }
                else
                {
                    arr[k] = R[j];
                    j++;
                }
                k++;
            }
    
            // 남은 요소들 추가
            while (i < n1)
            {
                arr[k] = L[i];
                i++;
                k++;
            }
    
            while (j < n2)
            {
                arr[k] = R[j];
                j++;
                k++;
            }
        }
    
        public static void MergeSortArray(int[] arr, int left, int right)
        {
            if (left < right)
            {
                int mid = left + (right - left) / 2; //중간 인덱스 계산
    
                MergeSortArray(arr, left, mid); //왼쪽 절반 재귀 정렬
                MergeSortArray(arr, mid + 1, right); //오른쪽 절반 재귀 정렬
                Merge(arr, left, mid, right);
            }
        }
    
        static void Main(string[] args)
        {
            int[] arr = { 38, 27, 43, 3, 9, 82, 10 };
            MergeSortArray(arr, 0, arr.Length - 1); // [3, 9, 10, 27, 38, 43, 82]
        }
    }
    ```

---
## **병합 정렬(Merge Sort) 특징**

- **제자리 정렬(in-place sorting) 알고리즘이 아닙니다.** 
    - 데이터 구조를 변경하지 않고 정렬할 수 있는 방법이 아니기 때문에, 추가적인 메모리를 사용해야 합니다.

- **안정 정렬 (Stable Sort)** 
    -  동일한 원소의 순서가 보장됩니다.

- **시간 복잡도** 
    - **최선, 평균, 최악** : $O(nlogn)$

- **공간 복잡도**
    - $O(n)$ (추가적인 배열 공간이 필요하기 때문)
    
---
## **병합 정렬(Merge Sort) 장단점**

- **장점**
    - **대용량 데이터 처리**
        - 큰 데이터 세트를 정렬할 때도 효율적입니다. 외부 정렬(예: 디스크에 저장된 데이터 정렬)에서도 유용하게 사용될 수 있습니다.

    - **재귀적 구조**
        - 직관적이고 이해하기 쉬운 재귀적 방식으로 구현할 수 있습니다.

    - **분할 정복**
        - 문제를 작은 문제로 나누어 푸는 분할 정복 전략을 사용하여, 병렬 처리와 같은 최적화가 가능합니다.

- **단점**
    - **단순한 경우의 비효율성**
        - 데이터가 이미 정렬되어 있는 경우에도 $O(nlogn)$ 의 시간 복잡도를 유지하므로, 간단한 정렬(예: 삽입 정렬)보다 비효율적일 수 있습니다.

    - **구현 복잡성**
        - 다른 정렬 알고리즘에 비해 구현이 다소 복잡할 수 있습니다. 특히, 비재귀적 구현은 추가적인 작업이 필요합니다.

    - **재귀 호출의 오버헤드**
        - 재귀적으로 구현할 경우, 함수 호출에 따른 오버헤드가 발생할 수 있습니다.

---
## 다른 정렬 알아보기
- **[버블 정렬(Bubble Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Bubble-Sort/)**
- **[삽입 정렬(Insertion Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Insertion-Sort/)**
- **[선택 정렬(Selection Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Selection-Sort/)**
- **[퀵 정렬(Quick Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Quick-Sort/)**
- **[힙 정렬(Heap Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Heap-Sort/)**
- **[계수 정렬(Counting Sort) 포스팅](http://cottoncandygrape.github.io/posts/Algorithm-Counting-Sort/)**

---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.
