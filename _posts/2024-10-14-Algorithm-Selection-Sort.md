---
title : "선택 정렬(Selection Sort) 알아보기 (python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 선택 정렬(Selection Sort)의 개념 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 개념 및 동작 과정](#선택-정렬selection-sort-개념-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#선택-정렬selection-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#선택-정렬selection-sort-특징)<br/>**
**[4. 장단점](#선택-정렬selection-sort-장단점)<br/>**
**[5. 다른 정렬 알아보기](#다른-정렬-알아보기)<br/>**

> 이번 포스팅에서는 **`오름차순`**으로 정렬합니다.
{: .prompt-info}

---
## **선택 정렬(Selection Sort) 개념 및 동작 과정**

### **개념** 

**선택 정렬(Selection Sort)**은 <u>비교 기반의 단순 정렬 알고리즘</u>입니다.   
이 알고리즘은 주어진 리스트에서 가장 작은 원소를 찾고, 그것을 현재 정렬되지 않은 부분의 가장 앞에 있는 원소와 교환하는 과정을 반복합니다. 
이 과정이 리스트의 처음부터 끝까지 순차적으로 이루어지며, 모든 원소가 정렬될 때까지 반복됩니다.

### **동작 과정**
1. 배열의 첫 번째 위치부터 시작해, 정렬되지 않은 부분의 가장 작은 원소를 찾습니다.
2. 가장 작은 원소를 현재 위치의 원소와 교환합니다.
3. 다음 위치로 이동하여 위의 과정을 반복합니다.
4. 배열의 끝에 도달하면 정렬이 완료됩니다.

---
## **선택 정렬(Selection Sort) 예시 및 구현 코드**

### **예시**

**[64, 25, 12, 22, 11]를 오름차순으로 정렬해 보겠습니다.**

- 1번째 라운드

    ```
    탐색 구간: [64, 25, 12, 22, 11]
    최솟값 = 11 → 교환(64 ↔ 11)
    결과: [11, 25, 12, 22, 64]
    ```

- 2번째 라운드

    ```
    탐색 구간: [25, 12, 22, 64]
    최솟값 = 12 → 교환(25 ↔ 12)
    결과: [11, 12, 25, 22, 64]
    ```

- 3번째 라운드

    ```
    탐색 구간: [25, 22, 64]
    최솟값 = 22 → 교환(25 ↔ 22)
    결과: [11, 12, 22, 25, 64]
    ```

- 4번째 라운드

    ```
    탐색 구간: [25, 64]
    최솟값 = 25 (이미 정렬)
    결과: [11, 12, 22, 25, 64]
    ```

- 5번째 라운드

    ```
    정렬 완료: [11, 12, 22, 25, 64]
    ```

---
### **구현 코드**     
- **Python**

    ```python
    def selection_sort(arr):
        for i in range(len(arr)-1):
            # 가장 작은 원소 찾기
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            # 가장 작은 원소를 현재 위치에 교환
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    arr = [64, 25, 12, 22, 11] 
    selection_sort(arr) # 결과 : [11, 12, 22, 25, 64]
    ```

- **C++**

    ```cpp
    #include <iostream>
    #include <vector>
    using namespace std;

    void selectionSort(vector<int>& arr) {
        for (size_t i=0; i<arr.size()-1; i++) {
            size_t minIndex = i;
            for (size_t j=i+1; j<arr.size(); j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            swap(arr[i], arr[minIndex]);
        }
    }

    int main() {
        vector<int> arr = {64, 25, 12, 22, 11};
        selectionSort(arr); //결과 : 11, 12, 22, 25, 64
        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;

    class Program {
        static void SelectionSort(int[] arr) {
            for (int i=0; i<arr.Length-1; i++) {
                int minIndex = i;
                for (int j=i+1; j<arr.Length; j++) {
                    if (arr[j] < arr[minIndex]) {
                        minIndex = j;
                    }
                }
                int temp = arr[minIndex];
                arr[minIndex] = arr[i];
                arr[i] = temp;
            }
        }

        static void Main() {
            int[] arr = {64, 25, 12, 22, 11}; 
            SelectionSort(arr); //결과 : 11, 12, 22, 25, 64
        }
    }
    ```

---
## **선택 정렬(Selection Sort) 특징**

- **제자리 정렬 (In-place Sort)** 
    - 추가적인 배열을 사용하지 않습니다.

- **불안정 정렬 (Unstable Sort)** 
    -  동일한 원소의 순서가 보장되지 않습니다.

- **시간 복잡도**
    - **최선, 평균, 최악** : $O(n^2)$ 
    
- **공간 복잡도**
    - $O(1)$ 
    
---
## **선택 정렬(Selection Sort) 장단점**

- **장점**
    - 구현이 매우 간단하여 이해와 구현이 쉽습니다.
    - 작은 데이터 세트를 정렬할 때 유용할 수 있습니다.

- **단점**
    - 시간 복잡도가 $O(n^2)$ 로, **대규모 데이터 세트에 비효율적**입니다.
    - 실질적으로 사용되기보다는 **교육 목적**으로 주로 사용됩니다.

---
## 다른 정렬 알아보기
- **[버블 정렬(Bubble Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Bubble-Sort/)**    
- **[삽입 정렬(Insertion Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Insertion-Sort/)**       
- **[퀵 정렬(Quick Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Quick-Sort/)**    
- **[병합 정렬(Merge Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Merge-Sort/)**      
- **[힙 정렬(Heap Sort) 포스팅](https://cottoncandygrape.github.io/posts/Algorithm-Heap-Sort/)**
- **[계수 정렬(Counting Sort) 포스팅](http://localhost:4000/posts/Algorithm-Counting-Sort/)**

---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.