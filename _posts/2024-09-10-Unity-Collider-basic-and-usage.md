---
title : "유니티 Collider 기초와 활용법 - CCGrape"
categories: [Unity3D]
tags: [Basic, Physics]
description: 유니티에서 충돌을 감지하는 Collider의 기초 개념과 활용법에 대하여 알아봅니다. 
---

## 목차
**[Step 0. 유니티에서 Collider를 배워야하는 이유](#step-0-유니티에서-collider를-배워야하는-이유)<br/>**
**[Step 1. Collider란?](#step-1-collider란)<br/>**
**[Step 2. Rigidbody란?](#step-2-rigidbody란)<br/>**
**[Step 3. Trigger와 Collision의 차이](#step-3-trigger와-collision의-차이)<br/>**
**[Step 4. 활용 예시](#step-4-활용-예시)<br/>**
**[Step 5. 마무리 요약](#step-5-마무리-요약)<br/>**

---
## Step 0. 유니티에서 Collider를 배워야하는 이유

**`Collider`**를 아는 것은 **GameObject**들이 서로 **상호작용**하고 **물리적 충돌**을 처리하며 **다양한 이벤트를 처리**하는 데 필수적입니다. 
게임의 **몰입감**을 높이고 **자연스러운 움직임**과 **상호작용을 구현**하는데 **핵심적인 역할**을 하기 때문에 반드시 배워야 합니다. 

충돌 감지는 `Collider`와 `Rigidbody`를 사용하여 처리하기 때문에 **Collider**와 **Rigidbody**의 기본 개념을 설명하고, `2D와 3D 차이`를 포함해 `Trigger()`와 `Collision()` 함수들에 대해 다루겠습니다. 
또한, 상황에 맞는 활용법도 함께 소개하겠습니다.

---
## Step 1. Collider란?

`Collider`는 GameObject가 충돌을 감지할 수 있도록 해주는 컴포넌트입니다.    

단, 충돌만 감지하며 `물리적인 반응(중력, 가속 등)`은 **<u>하지 않습니다.</u>**
Collider는 GameObject의 **외곽선을 정의**하고, **다른 Collider와 겹칠 때 Unity가 충돌 이벤트를 처리**하게 됩니다.

### ① 2D Collider와 3D Collider의 차이
- **2D Collider** 
  - **2D 환경**에서 사용되며, 2D 게임에서 캐릭터나 GameObject의 충돌을 감지하는 데 사용합니다. 
  - 종류로는 **BoxCollider2D**, **CircleCollider2D**, **PolygonCollider2D** 등이 있습니다.    
  <br/>

- **3D Collider** 
  - **3D 환경**에서 사용되며, 3D 게임에서 캐릭터나 GameObject의 충돌을 감지하는 데 사용합니다. 
  - 종류로는 **BoxCollider**, **SphereCollider**, **CapsuleCollider** 등이 있습니다.

> 충돌 감지를 하려면 충돌하는 물체 중 **적어도 하나에는 `Rigidbody` 컴포넌트가 필요**합니다.    
예를 들어 A와 B가 충돌할때 **`Rigidbody`**가 **<u>둘 다 없으면</u> 충돌감지가 되지 않습니다.**     
반대로 **A 또는 B 중 <u>적어도 하나에만 있거나 둘 다 있어도 충돌을 감지</u>**합니다. 
{: .prompt-info}

---
## Step 2. Rigidbody란?

`Rigidbody`는 GameObject에 `물리적인 특성`을 부여하는 컴포넌트입니다. 
**중력, 가속도, 힘 등**을 적용할 수 있으며, GameObject가 자연스러운 **물리 법칙**을 따르도록 합니다. 
`Collider`와는 달리 `Rigidbody`는 GameObject의 **<u>물리적 반응을 처리합니다.</u>**

### ① 2D Rigidbody와 3D Rigidbody의 차이
- **Rigidbody2D** 
  - **2D 물리 엔진**을 통해 2D 게임에서 **중력, 충돌 반응을 처리**합니다.   
  <br/>
- **Rigidbody**
  - **3D 물리 엔진**을 사용하여 **3D GameObject의 물리적 특성을 제어**합니다.

이번 포스팅에서는 `Collider`를 중점적으로 다루겠습니다. `Rigidbody`에 대한 더 자세한 포스팅은 다음 링크를 참고해주세요.

<i class="far fa-hand-point-right"></i>
[**[더 자세한 Rigidbody 포스팅]**](https://cottoncandygrape.github.io/posts/Unity-Rigidbody-property-and-method/)

---
## Step 3. Trigger와 Collision의 차이

### ① Trigger
![Trigger non checked]({{ site.baseurl }}/assets/postImgs/20240910/boxCollider.png)     

`Trigger`는 **물리적으로 충돌을 발생시키지 않지만**, GameObject가 Collider 안으로 들어올 때 **<u>이벤트를 발생</u>**시킵니다.    

예를 들어, **문이 자동으로 열리는 이벤트를 설정하고 싶을 때** Trigger를 사용하면 좋습니다.

**Trigger**를 사용하려면 **Collider**의 `Is Trigger` 옵션을 **활성화**해야 합니다. 
그러면 GameObject 간의 **충돌은 발생하지 않고**, Collider 내부에 들어오면 **이벤트가 발생**합니다.    

- **관련 함수**
  - `OnTriggerEnter()`: 다른 Collider가 Trigger **영역에 진입할 때** 호출됩니다.
  - `OnTriggerStay()`: 다른 Collider가 Trigger **영역 내에 머무는 동안** 호출됩니다.
  - `OnTriggerExit()`: 다른 Collider가 Trigger **영역에서 나갈 때** 호출됩니다.

### ② Collision
`Collision`은 **물리적**으로 GameObject 간의 **충돌을 처리**하는 방식입니다. 
오브젝트가 서로 부딪히면, **충돌에 대한 물리적 반응(반동, 밀림 등)이 발생**합니다.

- **관련 함수**
  - `OnCollisionEnter()`: Collider가 다른 Collider와 **처음 충돌할 때** 호출됩니다.
  - `OnCollisionStay()`: Collider가 다른 Collider와 **계속해서 충돌할 때** 호출됩니다.
  - `OnCollisionExit()`: Collider가 다른 Collider와 **충돌을 종료할 때** 호출됩니다.

---
## Step 4. 활용 예시

### ① Trigger 활용 예시: 문 열기
![Trigger checked]({{ site.baseurl }}/assets/postImgs/20240910/boxCollider2.png)
1. **문 GameObject**에 `BoxCollider`를 추가하고, `Is Trigger`를 **체크**합니다.
2. 캐릭터가 문에 **접근할 때** `OnTriggerEnter()` 함수가 호출되어 문이 열립니다.

```csharp
void OnTriggerEnter(Collider other) {
    if (other.CompareTag("Player")) {
        // 문 열기
        OpenDoor();
    }
}
```

### ② Collision 활용 예시: 장애물 충돌
![Collision example]({{ site.baseurl }}/assets/postImgs/20240910/collision.png)
1. 장애물과 캐릭터 GameObject에 `Rigidbody`와 `BoxCollider`를 추가합니다.
2. 캐릭터가 장애물에 **부딪힐 때**, `OnCollisionEnter()` 함수를 통해 **충돌을 감지하고 반응**합니다.

```csharp
void OnCollisionEnter(Collision collision) {
    if (collision.gameObject.CompareTag("Obstacle")) {
        // 캐릭터가 장애물에 부딪혔을 때의 처리
        TakeDamage();
    }
}
```

---
## Step 5. 마무리 요약

- `Collider`는 GameObject가 **충돌할 수 있는 외곽선을 정의**합니다.
- `Rigidbody`는 GameObject에 **물리적인 특성**을 부여합니다.
- `Trigger`는 <u>물리적 충돌 없이</u> **이벤트만 감지**하는데 사용되며, `Collision`은 **물리적인 충돌**을 처리합니다.
  - 충돌 감지를 위해서 **충돌하는 물체들 중 적어도 1개에는 `Rigidbody` 컴포넌트가 필요**합니다.
- **2D와 3D** 게임 개발 시 각 환경에 맞는 **Collider와 Rigidbody를 사용**해야 합니다.