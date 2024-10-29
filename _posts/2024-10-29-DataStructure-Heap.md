---
title : "Heap 자료구조 총 정리 (python, C++, C#) - CCGrape"
categories: [Data Structure]
tags: [Non-Linear]
description: 
math: true
---

## 목차
**[Step 1. Heap 자료구조 개념](#step-1-heap-자료구조-개념)<br/>**
**[Step 2. Heap 자료구조 특징](#step-2-heap-자료구조-특징)<br/>**
**[Step 3. Heap 자료구조 활용 예시](#step-3-heap-자료구조-활용-예시)<br/>**
**[Step 4. Heap 자료구조 연산](#step-4-heap-자료구조-연산)<br/>**
**[Step 5. Heap Sort 개념](#step-5-heap-sort-개념)<br/>**
**[Step 6. Heap 자료구조 구현 코드](#step-6-heap-자료구조-구현-코드)<br/>**

---
## **Step 1. Heap 자료구조 개념**

**Heap**은 **우선순위 큐(Priority Queue)**를 구현할 때 사용되는 **완전 이진 트리(Complete Binary Tree)** 기반의 자료구조입니다. 
주로 **최대값**이나 **최소값**을 빠르게 찾아야 하는 문제에서 유용하며, 두 가지 유형이 있습니다.

1. **최대 힙(Max Heap)**: 부모 노드의 값이 항상 자식 노드의 값보다 크거나 같음  
2. **최소 힙(Min Heap)**: 부모 노드의 값이 항상 자식 노드의 값보다 작거나 같음  

---
## **Step 2. Heap 자료구조 특징**

- **빠른 최대/최소값 접근**: <u>루트 노드에 항상 최대 또는 최소값</u>이 위치합니다.
- **삽입/삭제 시간 복잡도**: $O(\log n)$
- **부모-자식 간의 우선순위 관계**:
   - **최대 힙**: 부모 노드 ≥ 자식 노드
   - **최소 힙**: 부모 노드 ≤ 자식 노드
![Heap]({{ site.baseurl }}/assets/postImgs/20241029/Heap.png)
- **완전 이진 트리**: 마지막 레벨을 제외한 모든 레벨이 꽉 차 있어야 하고, 마지막 레벨은 왼쪽부터 차례로 채워져야 합니다.

> **이진 트리**에 대한 자세한 포스팅은 추후에 진행하겠습니다.
{: .prompt-info}

---
## **Step 3. Heap 자료구조 활용 예시**

- **우선순위 큐 구현** : 작업 스케줄링, 다익스트라 알고리즘 등에서 사용  
- **정렬 알고리즘** : 힙 정렬(Heap Sort)은 힙을 이용한 정렬 알고리즘으로, 시간 복잡도는 $O(n \log n)$입니다.
- **데이터 스트림 처리** : 실시간으로 들어오는 데이터에서 상위 k개의 요소를 찾을 때 유용합니다.

---
## **Step 4. Heap 자료구조 연산**
1. **삽입**
   - **새로운 노드**를 트리의 **가장 마지막 위치**에 삽입합니다.
   - 부모 노드와 비교하며 올바른 자리를 찾을 때까지 **Heapify-Up(상향 힙화)**을 수행합니다.
   - 아래는 **새로운 노드 8**을 삽입하는 과정입니다.
      - 1) 가장 마지막 위치에 8을 넣습니다.
      - 2) **부모 노드 4 < 8** => **교환**
      - 2) **부모 노드 7 < 8** => **교환**
      - 2) **부모 노드 9 > 8** => **종료**
   ![Heap Push]({{ site.baseurl }}/assets/postImgs/20241029/HeapPush.png)
   
2. **삭제**
   - 보통 **루트 노드(최대 또는 최소값)**를 삭제합니다.
   - **마지막 노드**를 **루트 위치**로 옮기고, 자식들과 비교하며 **Heapify-Down(하향 힙화)**을 수행합니다.
      - **왼쪽 노드를 먼저 비교**합니다. (완전 이진 트리 특성)
      - **두 자식이 모두 부모보다 크다**면 **더 큰 자식**과 교환.(최대 힙일 경우)
      - **두 자식이 같다**면 **왼쪽 자식과 교환**하는 것이 일반적.
   - 아래는 노드를 삭제하는 과정입니다.
      - 1) **루트 노드 9**를 삭제하고 **마지막 노드 3**을 루트에 위치시킵니다.
      - 2) **자식 노드 7 > 3** => **교환**
      - 3) **자식 노드 5 > 3** => **교환**
      - 4) **자식 노드 2 < 3** => **종료**
   ![Heap Pop]({{ site.baseurl }}/assets/postImgs/20241029/HeapPop.png)

---
## **Step 5. Heap Sort 개념**
- 힙을 사용해 정렬하는 알고리즘으로 **최대 힙을 사용하면 내림차순, 최소 힙을 사용하면 오름차순 정렬**을 수행합니다.
- **정렬 과정**
   1. 주어진 배열을 힙 구조로 변환(Heapify)합니다.
   2. 루트 노드를 반복적으로 추출하여 정렬된 배열에 추가합니다.

<i class="far fa-hand-point-right"></i>
[**[더 자세한 Heap Sort 포스팅]**](https://cottoncandygrape.github.io/posts/Algorithm-Heap-Sort/)

---
## **Step 6. Heap 자료구조 구현 코드**

### Python Heap 예제

- **heapq** 이용하기
- Python의 heapq는 기본적으로 **최소 힙(Min Heap)**으로 동작합니다. 

```python
import heapq

min_heap = [] # 빈 리스트를 힙으로 사용

# 삽입
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)

# 최소값 출력
print("최소값:", min_heap[0]) # 최소값: 5

# 최소값 삭제
print("삭제된 최소값:", heapq.heappop(min_heap)) # 삭제된 최소값: 5

# 힙 상태 출력
print("현재 힙:", min_heap) # 현재 힙: [10, 20]
```

---
### C++ Heap 예제

- 표준 라이브러리의 **priority_queue** 이용하기
- C++의 priority_queue는 기본적으로 **최대 힙(Max Heap)**으로 동작합니다.

```cpp
#include <iostream>
#include <queue>

int main() {
    std::priority_queue<int> maxHeap;

    // 삽입 (push)
    maxHeap.push(10);
    maxHeap.push(5);
    maxHeap.push(20);

    // 최대값 출력
    std::cout << "최대값: " << maxHeap.top() << std::endl; // 20

    // 최대값 제거 (pop)
    maxHeap.pop();
    std::cout << "최대값 제거 후: " << maxHeap.top() << std::endl; // 10

    return 0;
}
```

- **priority_queue**는 최대 힙이 기본이므로 **최소 힙**을 만들기 위해서는 **greater comparator**를 사용합니다.

```cpp
#include <iostream>
#include <queue>
#include <functional> // for std::greater

int main() {
   // <자료형, 구현체, 비교연산자>
   std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

   minHeap.push(10);
   minHeap.push(5);
   minHeap.push(20);

   std::cout << "최소값: " << minHeap.top() << std::endl; //5

   minHeap.pop();
   std::cout << "최소값 제거 후: " << minHeap.top() << std::endl; //10

   return 0;
}
```

- 배열처럼 저장된 데이터를 힙으로 변환(Heapify)하기 위해 **make_heap**을 사용합니다.

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // for make_heap, pop_heap, push_heap

int main() {
    std::vector<int> vec = {10, 5, 20};

    // 최대 힙 생성
    std::make_heap(vec.begin(), vec.end());

    std::cout << "최대값: " << vec.front() << std::endl;

    // 최대값 제거 (pop)
    std::pop_heap(vec.begin(), vec.end()); // 최대값이 맨 뒤로 이동
    vec.pop_back();

    std::cout << "최대값 제거 후: " << vec.front() << std::endl;

    return 0;
}
```

---
### C# Heap 예제

- C#에서는 **PriorityQueue** 클래스가 **.NET 6부터 제공**됩니다. 
- 이 클래스는 기본적으로 **최소 힙(Min Heap)**으로 동작합니다.

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 최소 힙 생성
        var minHeap = new PriorityQueue<int, int>();

        // 삽입 (값과 우선순위를 동일하게 사용)
        minHeap.Enqueue(10, 10);
        minHeap.Enqueue(5, 5);
        minHeap.Enqueue(20, 20);

        // 최소값 출력
        Console.WriteLine($"최소값: {minHeap.Peek()}"); //5

        // 최소값 제거
        minHeap.Dequeue();
        Console.WriteLine($"최소값 제거 후: {minHeap.Peek()}"); //10
    }
}
```

- **최대 힙(Max Heap) 구현**
- 최대 힙을 구현하려면 **우선순위를 음수로 바꾸는 방법**을 사용할 수 있습니다.


```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var maxHeap = new PriorityQueue<int, int>();

        // 음수 우선순위를 사용하여 최대 힙처럼 작동하게 만듦
        maxHeap.Enqueue(10, -10);
        maxHeap.Enqueue(5, -5);
        maxHeap.Enqueue(20, -20);

        Console.WriteLine($"최대값: {maxHeap.Peek()}"); //20

        maxHeap.Dequeue();
        Console.WriteLine($"최대값 제거 후: {maxHeap.Peek()}"); //10
    }
}
```

각 언어마다 heap이 동작하는 방식이 다릅니다. 이점 유의하여 사용하시기 바랍니다.

궁금한 점은 댓글로 남겨주세요.      
감사합니다.