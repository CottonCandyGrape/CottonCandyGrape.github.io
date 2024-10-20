---
title : "힙 정렬(Heap Sort) 알아보기 (python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 힙 정렬(Heap Sort)의 개념 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 개념 및 동작 과정](#힙-정렬heap-sort-개념-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#힙-정렬heap-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#힙-정렬heap-sort-특징)<br/>**
**[4. 장단점](#힙-정렬heap-sort-장단점)<br/>**

---
## **힙 정렬(Heap Sort) 개념 및 동작 과정**

### **개념** 
**힙 정렬(Heap Sort)**은 **비교 기반의 정렬 알고리즘**으로, **데이터 구조인 힙(Heap)**을 이용하여 정렬을 수행합니다. 
주로 **최대 힙(Max Heap)** 또는 **최소 힙(Min Heap)**을 사용하여 구현됩니다. 

**힙**은 **완전 이진 트리의 형태**를 가지며, 특정 성질을 만족합니다. 
최대 힙의 경우, 부모 노드의 값이 자식 노드의 값보다 크거나 같아야 하며, 최소 힙의 경우는 반대입니다. 

### **동작 과정**

> **최대 힙(Max Heap)** 기준으로 설명하겠습니다.
{: .prompt-info}

1. **힙 생성**
   - 주어진 배열을 최대 힙으로 변환합니다. 
   - 이를 위해 배열의 중간 인덱스부터 0까지 역순으로 힙을 조정(Heapify)합니다. 

2. **정렬**
   - 최대 힙이 생성된 후, 루트 노드(최대값)를 배열의 마지막 요소와 교환합니다. 
   - 그 후, 힙의 크기를 1 줄이고, 루트 노드부터 다시 힙을 유지하도록 조정합니다(Heapify). 
   - 이 과정을 배열의 크기가 1이 될 때까지 반복합니다.

---
## **힙 정렬(Heap Sort) 예시 및 구현 코드**

### **예시**

**[5, 3, 8, 4, 2, 7, 1, 10] 를 오름차순 정렬해 보겠습니다.**

#### **1단계: 힙 생성(Heapify)**

- 중간 노드부터 힙을 생성하기 위해 아래에서부터 위로 진행합니다.
- 각 노드의 자식 노드와 비교하여 힙 속성을 유지합니다.

> **이진 트리에서 인덱스 규칙**
1. 부모 노드의 인덱스: **i**
2. 왼쪽 자식 노드의 인덱스 : **2i+1**
3. 왼쪽 자식 노드의 인덱스 : **2i+2**
{: .prompt-info}

- 초기 배열
    ```
    [5, 3, 8, 4, 2, 7, 1, 10]
    ```

1. **인덱스 3 (4)**: 자식 노드 10과 비교하여 교환.
    ```
    교환 후 : [5, 3, 8, 10, 2, 7, 1, 4]
    ```

2. **인덱스 2 (8)**: 자식 노드 7과 비교하여 변화 없음.
    ```
    교환 후 : [5, 3, 8, 10, 2, 7, 1, 4]
    ```

3. **인덱스 1 (3)**: 자식 노드 10과 비교하여 교환.
    ```
    교환 후 : [5, 10, 8, 3, 2, 7, 1, 4]
    ```

4. **인덱스 0 (5)**: 자식 노드 10과 비교하여 교환.
    ```
    교환 후 : [10, 5, 8, 3, 2, 7, 1, 4]
    ```

최종적으로 생성된 최대 힙 배열 입니다.       
**[10, 5, 8, 3, 2, 7, 1, 4]**

#### **2단계: 루트 노드를 배열 끝으로 보내고, 새 힙을 재구성하여 반복**

1. **루트 노드(10)**를 배열의 끝과 교환하고, 크기를 줄입니다.

    ```
    [4, 5, 8, 3, 2, 7, 1, 10]

    새 힙 구성. (Heapify)
    [8, 5, 4, 3, 2, 7, 1, 10]
    ```

2. **루트 노드(8)**를 배열의 끝과 교환.

    ```
    [1, 5, 4, 3, 2, 7, 8, 10]

    새 힙 구성. (Heapify)
    [7, 5, 4, 3, 2, 1, 8, 10]
    ```

3. **루트 노드(7)**를 배열의 끝과 교환.

    ```
    [1, 5, 4, 3, 2, 7, 8, 10]

    새 힙 구성. (Heapify)
    [5, 4, 3, 2, 1, 7, 8, 10]
    ```

4. 이 과정을 반복하여 모든 원소를 정렬합니다.

최종적으로 정렬된 배열입니다.       
**[1, 2, 3, 4, 5, 7, 8, 10]**

---
### **구현 코드**     

- **Python**

    ```python
    def heapify(arr, n, i):
        largest = i  # 루트
        left = 2 * i + 1  # 왼쪽 자식
        right = 2 * i + 2  # 오른쪽 자식

        # 왼쪽 자식이 루트보다 크면
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 오른쪽 자식이 지금까지의 가장 큰 값보다 크면
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 가장 큰 값이 루트가 아니라면
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 스왑
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)

        # 최대 힙 만들기
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # 하나씩 요소를 꺼내기
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # 스왑
            heapify(arr, i, 0)

    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    ```

- **C++**

    ```cpp
    #include <iostream>
    using namespace std;

    void heapify(int arr[], int n, int i) {
        int largest = i; // 루트
        int left = 2 * i + 1; // 왼쪽 자식
        int right = 2 * i + 2; // 오른쪽 자식

        // 왼쪽 자식이 루트보다 크면
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // 오른쪽 자식이 지금까지의 가장 큰 값보다 크면
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // 가장 큰 값이 루트가 아니라면
        if (largest != i) {
            swap(arr[i], arr[largest]); // 스왑
            heapify(arr, n, largest);
        }
    }

    void heap_sort(int arr[], int n) {
        // 최대 힙 만들기
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // 하나씩 요소를 꺼내기
        for (int i = n - 1; i > 0; i--) {
            swap(arr[0], arr[i]); // 스왑
            heapify(arr, i, 0);
        }
    }

    // 사용 예제
    int main() {
        int arr[] = {12, 11, 13, 5, 6, 7};
        int n = sizeof(arr) / sizeof(arr[0]);
        heap_sort(arr, n);
        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;

    class HeapSort
    {
        static void Heapify(int[] arr, int n, int i)
        {
            int largest = i; // 루트
            int left = 2 * i + 1; // 왼쪽 자식
            int right = 2 * i + 2; // 오른쪽 자식

            // 왼쪽 자식이 루트보다 크면
            if (left < n && arr[left] > arr[largest])
                largest = left;

            // 오른쪽 자식이 지금까지의 가장 큰 값보다 크면
            if (right < n && arr[right] > arr[largest])
                largest = right;

            // 가장 큰 값이 루트가 아니라면
            if (largest != i)
            {
                int swap = arr[i];
                arr[i] = arr[largest];
                arr[largest] = swap;

                Heapify(arr, n, largest);
            }
        }

        static void HeapSortMethod(int[] arr)
        {
            int n = arr.Length;

            // 최대 힙 만들기
            for (int i = n / 2 - 1; i >= 0; i--)
                Heapify(arr, n, i);

            // 하나씩 요소를 꺼내기
            for (int i = n - 1; i > 0; i--)
            {
                int temp = arr[0];
                arr[0] = arr[i];
                arr[i] = temp;

                Heapify(arr, i, 0);
            }
        }

        public static void Main()
        {
            int[] arr = { 12, 11, 13, 5, 6, 7 };
            HeapSortMethod(arr);
        }
    }
    ```

---
## **힙 정렬(Heap Sort) 특징**

- **제자리 정렬 (In-place Sort)** 
    - 추가적인 배열을 사용하지 않습니다.

- **불안정 정렬 (Unstable Sort)** 
    - 동일한 원소의 순서가 보장되지 않습니다.

- **시간 복잡도**
    - **힙 생성 단계** : $O(n)$
    - **정렬 단계** : $O(nlogn)$
    - **힙 정렬 최선, 평균, 최악** : $O(nlogn)$

- **공간 복잡도**
    - $O(1)$

---
## **힙 정렬(Heap Sort) 장단점**

- **장점**
    - **비교 기반 정렬**
        - 비교 기반 정렬 알고리즘으로, 다양한 데이터 구조에서 사용될 수 있습니다.

    - **우선순위 큐(Priority Queue)**
        - Heap 구조는 우선순위 큐를 구현하는 데 유용하며, Heap Sort는 이 구조를 활용하여 정렬을 수행합니다.

- **단점**
    - **상수 계수**
        - Quick Sort와 같은 다른 알고리즘에 비해 상수 계수가 크기 때문에, 실제 수행 시간은 느릴 수 있습니다. 
        - 특히, 작은 데이터 집합에서는 Quick Sort가 더 빠를 수 있습니다.      

    - **복잡한 구현**
        - 다른 알고리즘에 비해 구현이 상대적으로 복잡할 수 있습니다. 
        - Heap 구조를 제대로 이해하고 구현하는 데 시간이 걸릴 수 있습니다.

    - **캐시 효율성**
        - Heap 구조는 **메모리 접근 패턴이 불규칙**하여 **캐시 효율성이 낮을 수 있습니다.**

---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.
