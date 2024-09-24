---
title : "유니티 오브젝트 이동시키기(feat. Update()) - CCGrape"
categories: [Unity3D]
tags: [Basic, Script]
description: Script를 이용하여 오브젝트를 이동시키는 방법을 알아봅니다. Update() 함수의 원리와 사용 방법을 알아봅니다.
---

## 목차
**[Step 0. Update() 함수를 사용하여 오브젝트 이동시키기](#step-0-update-함수를-사용하여-오브젝트-이동시키기)**<br/>
**[Step 1. Update() 함수란?](#step-1-update-함수란)**<br/>
**[Step 2. 오브젝트 이동시키기](#step-2-오브젝트-이동시키기)**<br/>
**[Step 3. Time.deltaTime을 사용하는 이유](#step-3-timedeltatime을-사용하는-이유)**<br/>
**[Step 4. 마무리](#step-4-마무리)**<br/>

---
## Step 0. Update() 함수를 사용하여 오브젝트 이동시키기 

Unity에서 오브젝트를 이동시키는 것은 매우 기본적이지만 중요한 작업 중 하나입니다. 
이 글에서는 `Update()` 함수를 활용하여 오브젝트를 이동시키는 방법과, 왜 `Time.deltaTime`을 곱해야 하는지에 대해 자세히 설명하겠습니다.

---
## Step 1. Update() 함수란?

Update() 함수는 Unity의 MonoBehaviour 클래스에 내장된 함수 중 하나로, **매 프레임마다 호출**됩니다. 
쉽게 말해, 게임이 실행될 때 **프레임마다 반복적으로 실행**되는 함수입니다.

```cs
void Update()
{
    // 매 프레임마다 실행될 코드
}
```

게임의 **프레임 레이트**는 <u>하드웨어 성능에 따라 달라질 수 있기 때문에</u>, 어떤 컴퓨터에서는 **초당 60프레임**이 나올 수도 있고, 다른 컴퓨터에서는 **30프레임**이 나올 수도 있습니다.     
Update() 함수는 이러한 프레임 레이트에 맞춰 호출되므로, 특정 코드가 프레임마다 한 번씩 실행됩니다.

---
## Step 2. 오브젝트 이동시키기

이제 Update() 함수를 이용해 오브젝트를 이동시켜보겠습니다. 
예를 들어, **로켓을 오른쪽으로 발사하는 스크립트**를 작성할 수 있습니다.

```cs
public class Rocket : MonoBehaviour
{
    Vector2 initPos = new Vector2(-5.0f, 0.0f); //시작 위치
    float speed = 10.0f; //로켓 속도
    float limit = 8.5f; //화면 밖 좌표

    void Update()
    {
        transform.position += Vector3.right * speed * Time.deltaTime;

        if (limit < transform.position.x) // 화면 밖으로 나갔을 경우 시작 위치로 이동
            transform.position = initPos;
    }
}
```
위 코드는 Rocket의 `position`을 `Vector3.right 방향`으로 `speed의 속도`로 이동시킵니다.     
그 다음 if 문은 화면 밖으로 로켓이 나갔을때 다시 로켓을 원위치 시켜주는 코드입니다.

위 코드를 다음 사진처럼 로켓 오브젝트에 붙여줍니다.
![Rocket Hierarchy]({{ site.baseurl }}/assets/postImgs/20240829/rocketHierarchy.png)


다음 영상은 위 코드의 실행 화면 입니다.     
![rocket.gif]({{ site.baseurl }}/assets/postImgs/20240829/rocket.gif)

---
## Step 3. Time.deltaTime을 사용하는 이유

코드에서 왜 `Time.deltaTime`을 사용하는 걸까요?

**Time.deltaTime**은 **"지난 프레임과 현재 프레임 사이의 시간 간격"**을 나타내는 값입니다.      

이 값은 초 단위로 나타내며, 프레임 간격이 짧을수록 (즉, 높은 프레임 레이트) Time.deltaTime 값은 작아집니다.     
반대로, 프레임 간격이 길수록 (즉, 낮은 프레임 레이트) 이 값은 커집니다.

프레임 레이트가 다른 두 환경에서 같은 속도로 오브젝트가 이동하도록 하려면, 속도에 Time.deltaTime을 곱해줘야 합니다. 
이렇게 하면 프레임 레이트가 높아지거나 낮아지더라도 이동 속도는 일정하게 유지됩니다.

예시:
```
이동속도 : 10, 1초 동안 이동거리
프레임 레이트가 60FPS인 경우 : 10 * 60 = 600 
프레임 레이트가 30FPS인 경우 : 10 * 30 = 300 
```
이렇게 Time.deltaTime을 곱하지 않는다면, 프레임 레이트가 높은 컴퓨터에서는 오브젝트가 더 빠르게 이동하고, 프레임 레이트가 낮은 컴퓨터에서는 느리게 이동하는 문제가 발생합니다.        

하지만 Time.deltaTime을 곱해준다면?

```
프레임 레이트가 60FPS인 경우: Time.deltaTime ≈ 1/60초 ≈ 0.0167초
10 * 60 * (1/60) = 10
프레임 레이트가 30FPS인 경우: Time.deltaTime ≈ 1/30초 ≈ 0.0333초
10 * 30 * (1/30) = 10 
```
이렇게 프레임 레이트가 달라도 이동 거리가 같아집니다.       
이는 사용자 경험에 큰 영향을 미칠 수 있으므로, 항상 Time.deltaTime을 곱하여 프레임 레이트에 관계없이 일정한 속도로 오브젝트를 이동시켜야 합니다.

---
## Step 4. 마무리 
**Update() 함수는 게임의 프레임마다 호출**되므로, **오브젝트의 이동, 애니메이션 처리 등 반복적으로 실행**되어야 하는 코드에 적합합니다. 하지만 **프레임 레이트가 변할 수 있기 때문에**, 일정한 이동 속도를 유지하려면 **Time.deltaTime을 곱해줘야 합니다.** 이를 통해 다양한 환경에서 일관된 사용자 경험을 제공할 수 있습니다.

궁금한 점은 댓글로 남겨주세요.      
감사합니다.