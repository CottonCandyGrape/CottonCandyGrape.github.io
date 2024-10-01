---
title : "유니티 FixedUpdate(), Update(), LateUpdate()의 차이와 활용법 - CCGrape"
categories: [Unity3D]
tags: [Basic, Script]
description: "생명주기(Lifecycle)에서 반복해서 실행되는 메서드 FixedUpdate(), Update(), LateUpdate()에 대해서 알아봅니다."
---

## 목차
**[Step 0. 서론](#step-0-서론)<br/>**
**[Step 1. FixedUpdate()](#step-1-fixedupdate)<br/>**
**[Step 2. Update()](#step-2-update)<br/>**
**[Step 3. LateUpdate()](#step-3-lateupdate)<br/>**
**[Step 4. 차이점 요약](#step-4-차이점-요약)<br/>**
**[Step 5. 활용 시 주의사항](#step-5-활용-시-주의사항)<br/>**

---
## Step 0. 서론 

저번 [**[생명주기(Lifecycle) 포스팅]**](https://cottoncandygrape.github.io/posts/Unity-Lifecycle/)에서는 **기초**에 중점을 두었기 때문에 **반복되는 메서드**는 `Update()`만 다루었습니다.
이번 포스팅에서는 `Update()` 만큼 중요한 `FixedUpdate()`와 `LateUpdate()`까지 학습하도록 하겠습니다.

유니티에서 게임 오브젝트의 동작을 제어하는 스크립트는 주로 `FixedUpdate()`, `Update()`, `LateUpdate()` 메서드를 통해 이루어집니다. 이 메서드들은 각각 게임 오브젝트의 상태를 업데이트하는 데 사용되지만, 그 **<u>실행 시점</u>**과 **<u>목적</u>**이 다릅니다.

이번 포스팅에서는 이 세 가지 메서드를 **<u>생명주기(Lifecycle) 순서</u>**에 따라 자세히 설명하겠습니다.     
다음 이미지는 생명주기(Lifecycle) 중 세 가지 메서드 관련 부분입니다.
![Update Cycle]({{ site.baseurl }}/assets/postImgs/20240904/updateCycle.png)

---
## Step 1. FixedUpdate()

- **정의**
    - `FixedUpdate()` 메서드는 **물리 연산(Physics)**과 관련된 작업에 사용됩니다. 
    - **고정된 시간 간격(default 0.02초)**마다 호출되며, **프레임 레이트와 무관**하게 **일정한 주기**로 실행됩니다.
        - **고정된 시간 간격 수정 방법** : Edit → Project Setting → Time → Fixed TimeStep

- **활용**
    - **물리적인 힘 적용이나 속도, 중력** 등과 같은 `물리 연산`을 처리하는 데 사용됩니다. 
    - 물리 엔진은 **일정한 시간 간격**을 기준으로 연산되므로, 이 메서드에 물리 관련 코드를 작성해야 정확한 물리 시뮬레이션이 가능합니다.

- **코드 예시** 
```cs
void FixedUpdate() {
    // 물리적인 힘을 적용
    Rigidbody rb = GetComponent<Rigidbody>();
    rb.AddForce(Vector3.forward * force);
}
```

> Time.timeScale == 0 이면 **Physics Loop**가 실행되지 않습니다.    
**=> FixedUpdate() 실행 안됨.**
{: .prompt-info}

---
## Step 2. Update()

- **정의**
    - `Update()` 메서드는 **매 프레임(frame)마다 호출**됩니다. 
    - 게임의 **프레임 레이트(frame rate)**에 따라 호출 빈도가 달라질 수 있으며, **화면의 새로고침 주기와 일치**합니다.

- **활용**
    - 주로 게임의 **메인 로직, 사용자 입력 처리, 오브젝트의 상태 업데이트** 등에 사용됩니다.
        - 예) 사용자의 입력에 따라 **캐릭터를 이동**, **애니메이션 실행** 로직.
    - 프레임 기반으로 실행되므로 **실시간 상호작용**이 중요한 경우에 적합합니다.

- **코드 예시**
```cs
void Update() {
    // 캐릭터 이동 처리
    float move = Input.GetAxis("Horizontal") * speed * Time.deltaTime;
    transform.Translate(move, 0, 0);
}
```

---
## Step 3. LateUpdate()

- **정의**
    - `LateUpdate()` 메서드는 `Update()`가 **모두 실행된 후에 호출**됩니다. 
    - 주로 **카메라의 위치를 업데이트**하거나 다른 오브젝트의 움직임을 따라가야 하는 경우에 유용합니다.

- **활용**
    - 주로 다른 오브젝트가 이동한 후 그 위치에 따라 **카메라를 이동시키는 데 사용**됩니다. 
        - 예를 들어, 캐릭터가 이동한 후 **카메라가 해당 캐릭터를 따라가는 로직**을 작성할 수 있습니다.
    - `Update()`가 **끝난 후 실행**되므로, 오브젝트 간의 상호작용이 완료된 후에 추가적으로 처리할 로직을 넣기에 적합합니다.

- **코드 예시**
```cs
void LateUpdate() {
    // 캐릭터를 따라가는 카메라 위치 업데이트
    Vector3 newPosition = player.transform.position + offset;
    transform.position = newPosition;
}
```

- **캐릭터를 따라가는 카메라 구현 영상**    
![LateUpdate()]({{ site.baseurl }}/assets/postImgs/20240904/lateUpdate.webp)

---
## Step 4. 차이점 요약

- **Update()**
    - **호출 주기** : 매 프레임마다 호출
    - **주 사용 용도** : 게임 로직, 사용자 입력 처리
    - **주의점** : 프레임 레이트에 따라 호출 빈도가 달라질 수 있음      
<br/>

- **FixedUpdate()**
    - **호출 주기** : 고정된 시간 간격마다 호출
    - **주 사용 용도** : 물리 연산 처리
    - **주의점** : 일정한 주기로 호출되며, 물리 연산의 정확성 보장      
<br/>

- **LateUpdate()**
    - **호출 주기** : Update() 이후에 호출
    - **주 사용 용도** : 카메라 위치 업데이트, 후처리 로직 
    - **주의점** : Update() 이후 실행되므로 오브젝트의 최종 상태에 접근 가능

---
## Step 5. 활용 시 주의사항

- **효율적인 처리** 
    - 불필요한 연산을 피하기 위해 `FixedUpdate()`와 `Update()`의 역할을 명확히 구분해야 합니다. 
    - 물리 연산이 아닌 코드는 `Update()`에서 처리하는 것이 **성능상 유리**합니다.

- **FixedUpdate()와 Update()의 다른 연산 주기**     
앞서 말씀드렸다시피 두 메서드의 **연산 주기는 다릅니다.** 이를 방지하기 위해 특정 변수를 `FixedUpdate()`와 `Update()`에서 **동시에 사용하지 않도록 주의**해야 합니다.      
따라서 **물리 연산**과 관련한 것들은 **FixedUpdate()**에 구현하고 그 외 **게임로직**에 대한 것은 **Update()**에 구현하는 것이 좋습니다.

    - 예를 들어 **충돌(물리)**과 관련한 연산은 **FixedUpdate()**에 포함시키는 것이 좋습니다.
        - **Update()**에 **충돌 계산**을 포함시킬 경우 **버벅이는 현상**이 있을 수 있습니다.    
        <br/>

    - **[Update()에 구현한 경우]** : 벽에 부딪힐 때 버벅거리는 현상이 있습니다.      
    ![Update()]({{ site.baseurl }}/assets/postImgs/20240904/update.webp)
    - **[FixedUpdate()에 구현한 경우]** : 버벅이지 않고 부드럽습니다.     
    ![FixedUpdate()]({{ site.baseurl }}/assets/postImgs/20240904/fixedUpdate.webp)      

---
**포스팅의 예시로 사용된 게임을 플레이하고 싶으신 분들은 스토어에 `bunnybunny`를 검색하시거나 해당 `스토어 이미지`를 클릭해 주세요~!**


[![애플 앱 스토어]({{ site.baseurl }}/assets/postImgs/appstore.png)](https://apps.apple.com/kr/app/bunnybunny-io/id6504274647?platform=iphone)
[![구글 플레이 스토어]({{ site.baseurl }}/assets/postImgs/google.png)](https://play.google.com/store/apps/details?id=com.ccGrape.BunnyBunny)

이만 포스팅을 마치겠습니다.     
감사합니다.