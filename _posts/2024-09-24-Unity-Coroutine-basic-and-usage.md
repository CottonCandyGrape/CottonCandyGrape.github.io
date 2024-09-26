---
title : "유니티 Coroutine 알아보기 - CCGrape"
categories: [Unity3D]
tags: [Basic, Script]
description: 유니티에서 Coroutine의 정의와 사용 이유부터 최적화 사용법과 Thread, Invoke와의 차이까지 모두 알아봅니다.
---

## 목차
**[Step 0. Coroutine의 정의](#step-0-coroutine의-정의)<br/>**
**[Step 1. Coroutine 사용 이유](#step-1-coroutine-사용-이유)<br/>**
**[Step 2. Coroutine 최적화 사용법](#step-2-coroutine-최적화-사용법)<br/>**
**[Step 3. Coroutine과 Thread, Invoke 비교](#step-3-coroutine과-thread-invoke-비교)<br/>**
**[Step 4. 마무리](#step-4-마무리)<br/>**

---
**유니티에서 Coroutine**은 코드 실행을 **일시 중지**하고 **일정 시간 동안 대기**하거나 **조건을 기다리며 코드를 단계별로 실행**할 수 있습니다. 
이는 **복잡한 타이머, 반복 작업, 프레임 단위의 작업을 비동기적으로 처리**할 수 있어 게임 개발에 상당한 편리함을 줍니다. 
하지만 단점도 있어 **남발하여 사용하지 않는 게 중요**합니다. 

이번 포스팅에서는 유니티에서 **Coroutine**의 모든 것에 대해서 알아보겠습니다.

---
## **Step 0. Coroutine의 정의**

```cs
IEnumerator CoroutineName()
{ 
    yield return null; 
}
```

1. 리턴 타입 : **IEnumerator**
2. 함수 내에 **`yield return`** 을 <u>반드시 포함</u>하여야함.
    - **yield return의 종류**
        - **yield return null** : 다음 프레임에서 실행
        - **yield return new WaitForSeconds(float t)**: 매개변수 숫자만큼 기다렸다가 실행
            - **TimeScale**에 따라 달라질 수 있다.
        - **yield return new WaitForSecondsRealTime(float t)** : 매개변수 숫자만큼 기다렸다가 실행
            - **실제 시간**을 기준으로 한다.
        - **yield return new WaitForFixedUpdate()** : 모든 스크립트에서 모든 FixedUpdate()가 호출된 후에 실행
        - **yield return new WiatForEndOfFrame()** : 모든 카메라와 GUI가 렌더링을 완료하고 스크린에 프레임을 표시하기 전에 실행
        - **yield break** : Coroutine 끝내기
        - **yield return StartCoroutine(OtherCoroutine())** : 해당 Coroutine이 완료될 때까지 기다렸다가 실행

---
## **Step 1. Coroutine 사용 이유**

1. **시간의 경과에 따라** 코드를 실행시키고 싶을 때 사용합니다.
2. **반복중 일시중지** 하거나 **특정 조건에 의해 코드를 실행, 반복**시키기 위해 사용합니다.
3. Coroutine 대신 Update()에서도 처리가 가능하지만 **Update()가 필요하지 않을 때 호출되는 것은 바람직하지 않습니다.**

> **주의!!!**      
**`Coroutine`**은 유니티 내부에서 **병렬처리**하기 때문에 **순서가 명확하지 않아** 문제가 생기면 **버그 잡기가 힘들다는 단점**이 있습니다.
따라서 **남발하여 사용하지 않는 것**이 중요합니다.
{: .prompt-warning }

---
## **Step 2. Coroutine 최적화 사용법**

### ① **Coroutine 호출 방법 2가지**
1. 직접 호출 방법
    ```cs
    StartCoroutine(Method());
    StartCoroutine(Method(object value)); // 매개변수
    ```
2. string 호출 방법
    ```cs
    StartCoroutine("Method");
    StartCoroutine("Method", value); //매개변수
    ```

### ② **캐싱(Caching) 사용법**
`yield return new WaitForSeconds()`처럼 코루틴 함수가 반복될 때마다 **new**를 사용하게 되면 **가비지가 많이 쌓이게 됩니다.**
이를 해결하기 위해 **변수에 할당**하여 **`캐싱(Caching)`**하여 사용하는 것이 효율적입니다.

```cs
IEnumerator Run()
{
    WaitForSeconds waitForSeconds = new WaitForSeconds(1f);
 
    while (true)
    {
        //yield return new WaitForSeconds(1f); //보다는 밑에 줄 처럼
        yield return waitForSeconds;
    }
}
```

### ③ **StopCorouinte() 사용법**

- **'직접 호출 방식'으로 호출한 Coroutine은 string 방법으로 중지 시킬 수 없습니다.**

    ```cs
    StartCoroutine(Method());
    StopCoroutine(Method()); // 중지되지않음(새로운 인스턴스를 생성하므로 잘못된 방법) 

    StartCoroutine(Method());
    StopCoroutine("Method"); // 중지되지않음

    StartCoroutine("Method");
    StopCoroutine("Method"); // 중지됨
    ```

- **StopCoroutine()의 올바른 사용법**
    - **string**으로 호출한 Coroutine은 **string**으로 멈추기.
    - **직접 호출 방식**으로 호출한 Coroutine은 리턴값을 **변수에 저장**하고 그 **변수를 이용**해 멈추기.       

        ```cs
        //1개의 Coroutine만 돌리기 위해 변수에 저장
        Coroutine runningCoroutine = null;

        //이미 실행중인 Coroutine이 있다면, 정지 후 코루틴을 실행
        if(runningCoroutine != null)
            StopCoroutine(runningCoroutine);

        //Coroutine을 시작하는 동시에 저장한다.
        runningCoroutine = StartCoroutine(Method());
        ```     

> **Tip!!!**    
- Coroutine을 **여러 개 실행**한다면 **변수에 할당하는 방식**으로 해야합니다.
- **string 호출 방법은 이름이 같은 모든 코루틴을 조작합니다.**
- **`StopAllCoroutines()`**는 **해당 스크립트 안에 있는 것만 중지**한다. 
{: .prompt-info }

---
## **Step 3. Coroutine과 Thread, Invoke 비교**

### ① **Coroutine의 특징**
- 단일 **Main Thread**에서 동작합니다.
- **여러 개의 일**을 나누어 **하나씩 처리**합니다.
- **Thread** 보다 **메모리와 리소스를 덜 사용**합니다.
- **복잡한 반복 작업**이나 **대기 로직 처리**가 가능합니다.
    - 자유롭게 대기 시간 조정이 가능합니다.

---

### ② **Thread의 특징**
- 별개의 **Thread**에서 동작합니다.
- **동시에 여러 개의 일을 처리**할 수 있습니다.
- **I/O처리, 네트워크 요청, 데이터 처리** 등에 적합합니다.
    - ex) 대규모 데이터를 서버에서 받아오고 그 데이터를 처리할 때
- **CPU를 많이 사용하는 연산에 적합**하지만 **Unity API**와 상호 작용할 수 없습니다.

---

- **Coroutine과 Thread의 흐름 비교**
    ![Coroutine vs Thread]({{ site.baseurl }}/assets/postImgs/20240924/Coroutine_vs_Thread.png)

---

### ③ **Invoke의 특징**
- 특정 메서드를 일정 시간 뒤에 **한 번 호출합니다.**
- 코드가 복잡하지 않은 **간단한 지연 작업에 적합**합니다.
    - ex) 버튼 클릭 후 3초 뒤에 창을 닫고 싶은 경우
- **`InvokeRepeating()`**을 사용하여 **반복 호출**할 수 있습니다.
- **`Time.timeScale = 0`** 일 때 동작하지 않습니다.

---

- **Coroutine은 GameObject가 활성화 된 상태에서만 작동합니다.**
    - **스크립트 비활성화 시** : Coroutine, Invoke 둘 다 실행 유지
    - **GameObject 비활성화 시** : Coroutine은 정지, Invoke는 상태 유지

> **활성, 비활성 반복시 중복 실행 문제**    
**OnEnable()**에 실행 함수가 있다면 꼭 **OnDisable()**에 중지시키는 코드를 작성해야 한다. 
{: .prompt-warning }

---
## Step 4. 마무리
이번 포스팅에서는 **Coroutine의 정의, 사용 이유, 최적화 사용법, Thread, Invoke와 비교**까지 다루어 보았습니다. 
이 모든 것들을 고려하여 적재적소에 맞는 활용법을 이용하는 것이 게임 개발에 큰 도움이 됩니다. 

궁금한 점은 댓글로 남겨주세요.      
감사합니다.