---
title : "[Unity3D] 유니티 생명주기(Lifecycle) - CCGrape"
categories: [Unity3D]
tags: [Basic, Script]
description: 유니티의 생명주기(Lifecycle)의 기초에 대해서 알아봅니다. 자주 사용되는 함수들의 특징과 활용 방법에 대해서 알아봅니다.
---

## 목차
**[Step 0. 유니티 생명주기(Lifecycle)이란?](#step-0-유니티-생명주기lifecycle이란)**<br/>
**[Step 1. 자주 사용하는 유니티 생명주기(Lifecycle) 함수들](#step-1-자주-사용하는-유니티-생명주기lifecycle-함수들)**<br/>
**[Step 2. 구체적인 유니티 생명주기(Lifecycle)](#step-2-구체적인-유니티-생명주기lifecycle)**<br/>

---
이번 포스팅에서는 유니티 **생명주기(Lifecycle)**의 **기초를 중심**으로 알아봅니다.      
그리고 생명주기에서 **자주 사용되는 함수**들 위주로 학습하겠습니다.

---
## Step 0. 유니티 생명주기(Lifecycle)이란?

유니티의 `생명주기(Lifecycle)`는 GameObject가 시작되고, 업데이트되고, 종료되는 과정을 관리하는 **일련의 함수들**로 이루어져 있습니다. 
이러한 함수들은 **특정한 순서로 호출**되며, 게임의 흐름을 제어하는 데 중요한 역할을 합니다.

---
## Step 1. 자주 사용하는 유니티 생명주기(Lifecycle) 함수들

### ① Awake()

- GameObject가 **'생성'**될 때 `가장 먼저 호출`되고, `단 한 번만 호출`됩니다.     
- 이 함수는 GameObject가 활성화되기 전에 `초기화 작업`을 수행하는 데 사용됩니다.
- 다른 스크립트나 GameObject에 접근하여 **초기 설정**을 하거나, **기본값을 초기화**하는 데 사용됩니다.

```cs
void Awake() {
    // 초기화 코드
    Debug.Log("Awake 호출");
}
```

### ② Start()

- Start는 Awake가 호출된 후, GameObject가 **'활성화'**되었을 때 `한 번 호출`됩니다.
- **모든 Awake 함수가 호출된 이후에 호출**되며 `스크립트`가 **처음 실행될 때** `한 번만 호출`됩니다.
- GameObject가 완전히 **초기화된 후에 실행되어야 하는 작업**을 여기에 정의합니다.

```cs
void Start() {
    // 초기화 완료 후 코드
    Debug.Log("Start 호출");
}
```

**Tip** : GameObject의 **'생성'**과 **'활성화'**의 차이   
**생성** : 게임 오브젝트를 처음으로 메모리에 할당하고 씬에 추가하는 과정.   
**활성화** : 그 오브젝트가 씬에서 동작할 수 있도록 상태를 변경하는 과정.    
<i class="far fa-hand-point-right"></i>
[**[생성과 활성화의 차이 포스팅]**](https://cottoncandygrape.github.io/2024/09/03/Unity-Instantiation-vs-Activation.html)
{:.warning}

### ③ Update()

- `매 프레임마다 호출`되는 함수로, 게임의 주요 로직이 이곳에서 실행됩니다.
- 초당 여러 번 호출되며, 게임의 **프레임률에 따라 호출 빈도가 달라집니다.**
- `지속적으로 반복되어야 하는 작업`을 이곳에 구현합니다.
    - `플레이어 입력 처리`, `물체 이동`, `게임 상태 체크` 등 

```cs
void Update() {
    // 매 프레임 호출
    Debug.Log("Update 호출");
}
```
<i class="far fa-hand-point-right"></i>
[**[더 자세한 Update() 함수 포스팅]**](https://cottoncandygrape.github.io/2024/08/29/Unity-object-translate(feat.Update()).html)


### ④ OnEnable() & OnDisable()

- `OnEnable`은 GameObject가 `활성화`될 때 호출되고, `OnDisable`{:.warning}은 `비활성화`{:.warning}될 때 호출됩니다.
- 이 함수들은 오브젝트의 활성화 상태에 따라 **여러 번 호출될 수 있습니다.**
- 오브젝트가 **활성화될 때 필요한 리소스를 로드**하거나, **비활성화될 때 리소스를 해제**하는 작업에 사용됩니다.

```cs
void OnEnable() {
    Debug.Log("OnEnable 호출");
}

void OnDisable() {
    Debug.Log("OnDisable 호출");
}
```

### ⑤ OnDestroy()

- OnDestroy는 GameObject가 **파괴**될 때 호출됩니다.
- `메모리 해제`나, `오브젝트 파괴 전` 마지막 정리 작업을 수행할 수 있습니다.

```cs
void OnDestroy() {
    Debug.Log("OnDestroy 호출");
}
```

---
## Step 2. 구체적인 유니티 생명주기(Lifecycle)

다음은 유니티 내부에서 **실제로 실행되는 생명주기(Lifecycle)**입니다.     
각 함수들의 **순서에 유의**하여 암기하고 있으면 개발에 큰 도움이 됩니다. 
모두 암기할 필요는 없고 **오늘 학습한 것 위주**로 알고 계시면 충분할 것 같습니다.

![Unity Lifecycle]({{ site.baseurl }}/assets/postImgs/20240903/lifecycle.png)
[[이미지 자료 출처 링크]](https://docs.unity3d.com/kr/2021.3/Manual/ExecutionOrder.html)

---
이만 포스팅을 마치겠습니다.     
감사합니다.