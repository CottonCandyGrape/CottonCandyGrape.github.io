---
title : "삽입 정렬(Insertion Sort) 알아보기 (python, C++, C#) - CCGrape"
categories: [Algorithm]
tags: [Sort]
description: 삽입 정렬(Insertion Sort)의 원리 및 동작 과정, 특징, 장단점에 대해서 알아봅니다. Python, C++, C#으로 예시코드를 구현합니다.
math: true
---

## 목차
**[1. 원리 및 동작 과정](#삽입-정렬insertion-sort-원리-및-동작-과정)<br/>**
**[2. 예시 및 구현 코드](#삽입-정렬insertion-sort-예시-및-구현-코드)<br/>**
**[3. 특징](#삽입-정렬insertion-sort-특징)<br/>**
**[4. 장단점](#삽입-정렬insertion-sort-장단점)<br/>**

> 이번 포스팅에서는 **`오름차순`**으로 정렬합니다.
{: .prompt-info}

---
## **삽입 정렬(Insertion Sort) 원리 및 동작 과정**

### **원리** 

**삽입 정렬(Insertion Sort)**은 **특정한 데이터를 적절한 위치**에 **삽입**한다는 의미에서 **삽입 정렬(Insertion Sort)**이라고 부릅니다.
**첫 번째 요소는 이미 정렬된 것으로 가정**하고, **두 번째 요소부터 시작**하여 각 요소를 왼쪽의 정렬된 배열 부분에 삽입하여 전체를 정렬된 상태로 만듭니다.

이 알고리즘은 직관적으로 사람들이 카드를 손에 쥐고 정렬하는 방법과 비슷합니다. 

### **동작 과정**
1. 배열의 **두 번째 요소부터 시작**합니다.
2. **현재 요소를 key로 저장**하고 그 앞에 있는 요소들과 비교하여 알맞은 위치를 찾습니다.
3. key보다 큰 요소들은 한 칸씩 오른쪽으로 이동시킵니다.
4. key보다 작은 요소를 만나면 그 위치에 key 값을 삽입합니다.
5. 전체 배열이 정렬될 때까지 1~4 과정을 반복합니다.

---
## **삽입 정렬(Insertion Sort) 예시 및 구현 코드**

### **예시**

**[5, 3, 8, 6, 2]을 오름차순으로 정렬해 보겠습니다.**

- 1번째 라운드

    ```
    첫 번째 원소(5)는 이미 정렬된 상태로 가정합니다.
    두 번째 원소(3)를 정렬된 부분에 삽입합니다.
    [5] → 3이 5보다 작으므로 5 앞에 삽입
    정렬된 상태: [3, 5, 8, 6, 2]
    ```

- 2번째 라운드

    ```
    세 번째 원소(8)는 3, 5보다 크므로 그대로 위치합니다.
    정렬된 상태: [3, 5, 8, 6, 2]
    ```

- 3번째 라운드

    ```
    네 번째 원소(6)를 정렬된 부분에 삽입합니다.
    6은 8보다 작으므로 8 앞에 삽입
    정렬된 상태: [3, 5, 6, 8, 2]
    ```

- 4번째 라운드 

    ```
    다섯 번째 원소(2)를 정렬된 부분에 삽입합니다.
    2는 3보다 작으므로 맨 앞에 삽입
    정렬된 상태: [2, 3, 5, 6, 8]
    ```

- 5번째 라운드 

    ```
    최종 결과: [2, 3, 5, 6, 8]
    ```

---
### **구현 코드**     

> 매번 비교하면서 **Swap**하는 방식은 비효율적이기 때문에 하나씩 **Shift**하는 방식으로 구현했습니다.
{: .prompt-info}

- **Python**

    ```python
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    arr = [5, 2, 4, 6, 1, 3]
    insertion_sort(arr) # 1, 2, 3, 4, 5, 6
    ```

- **C++**

    ```cpp
    #include <iostream>
    #include <vector>

    void insertionSort(std::vector<int>& arr) {
        for (int i = 1; i < arr.size(); i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    int main()
    {
        std::vector<int> arr = {5, 2, 4, 6, 1, 3};
        insertionSort(arr); //1, 2, 3, 4, 5, 6

        return 0;
    }
    ```

- **C#**

    ```csharp
    using System;

    class InsertionSortExample
    {
        static void InsertionSort(int[] arr) {
            for (int i = 1; i < arr.Length; i++) {
                int key = arr[i];
                int j = i - 1;
                while (j >= 0 && arr[j] > key) {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = key;
            }
        }

        static void Main()
        {
            int[] arr = { 5, 2, 4, 6, 1, 3 };
            InsertionSort(arr); //1, 2, 3, 4, 5, 6
        }
    }
    ```

---
## **삽입 정렬(Insertion Sort) 특징**

- **제자리 정렬 (In-place Sort)** 
    - 추가적인 배열을 사용하지 않습니다.

- **안정 정렬 (Stable Sort)** 
    - 동일한 원소의 순서가 보장됩니다.

- **시간 복잡도**: 
    - **최선(이미 정렬된 경우)** : $O(n)$
    - **최악, 평균** : $O(n^2)$ 

- **공간 복잡도**:
    - $O(1)$ 
    
---
## **삽입 정렬(Insertion Sort) 장단점**

- **장점**
    - 간단하고 직관적이며 구현이 용이한 알고리즘입니다.
    - 데이터가 **거의 정렬되어 있을 때**는 굉장히 빠릅니다. (최선의 경우 시간 복잡도 $O(n)$)
    - 다른 영역으로의 메모리 이동이 적어 **메모리 오버헤드가 적습니다.**

- **단점**
    - 일반적으로 **큰 데이터 세트에서는 비효율적**입니다.
    - 대부분의 다른 정렬 알고리즘(예: QuickSort, MergeSort)보다 **속도가 느립니다.**

---
궁금한 점은 댓글로 남겨주세요.      
감사합니다.
