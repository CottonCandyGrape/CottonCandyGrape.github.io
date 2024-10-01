---
title : "유니티 GameObject 생성(Instantiation)과 활성화(Activation)의 차이 - CCGrape"
categories: [Unity3D]
tags: [Basic, Script]
description: 헷갈릴 수 있는 GameOjbect의 생성(Instantiation)과 활성화(Activation)의 차이에 대해서 알아봅니다. 추가로 Awake()와 Start() 함수의 차이에 대해서도 알아봅니다.
---

## 목차
**[Step 1. GameObject의 생성(Instantiation)](#step-1-gameobject의-생성instantiation)<br/>**
**[Step 2. GameObject의 활성화(Activation)](#step-2-gameobject의-활성화activation)<br/>**
**[Step 3. 생성과 활성화의 차이](#step-3-생성과-활성화의-차이)<br/>**

---
유니티에서 **GameObject**의 `생성(Instantiation)`과 `활성화(Activation)`는 서로 다른 개념입니다.   
이 두 개념을 이해하는 것은 게임 개발에서 중요한 부분입니다. 아래에서 각각의 **정의**와 **차이점**을 살펴보겠습니다.

---
## Step 1. GameObject의 생성(Instantiation)

- **정의**    
  - 새로운 GameObject를 **메모리에 할당**하고, **유니티 씬(Scene) 내에 배치**하는 과정을 의미합니다.       
  - 주로 `Instantiate()` 함수를 사용하여 기존 프리팹(Prefab)이나 다른 GameObject를 복제하여 새로 생성할 수 있습니다.
  
- **특징**
  - GameObject가 생성될 때, 해당 오브젝트에 연결된 컴포넌트의 `Awake()` 함수가 호출됩니다.
  - 생성된 오브젝트는 씬에 존재하지만, <u>반드시 활성화된 상태로 존재하지 않을 수도 있습니다.</u>
  - 생성된 오브젝트는 <u>활성화 여부와 관계없이 메모리에 할당</u>됩니다.

- **예시 코드**
  ```cs
  GameObject newObject = Instantiate(prefab);
  ```

- **활용** 
  - 게임 중 특정 이벤트나 조건이 충족될 때 **새로운 GameObject를 생성하고 싶을 때** 사용합니다.      
  - 예를 들어, `적 캐릭터를 생성`하거나 `특정 아이템을 스폰`할 때 유용합니다.

## Step 2. GameObject의 활성화(Activation)

- **정의** 
  - GameObject의 활성화는 생성된 오브젝트를 `활성화`하거나 `비활성화`{:.warning}하는 것을 의미합니다.   
  - 게임 오브젝트는 **생성된 이후에도 비활성화될 수 있으며**, **활성화된 상태**에서는 **씬에서 보이고, 동작을 수행**합니다.

- **특징**
  - GameObject가 활성화될 때, 해당 오브젝트에 연결된 컴포넌트의 `OnEnable()`함수가 호출됩니다. 
    - 비활성화될 때는 `OnDisable()`{:.warning} 함수가 호출됩니다.
  - `활성화`된 오브젝트는 **씬에서 보이며**, 그에 따라 해당 오브젝트의 `Update() 등의 생명주기(Lifecycle) 함수들이 호출됩니다.`
  - `비활성화`{:.warning}된 오브젝트는 **씬에 존재하지만, 렌더링되지 않고, 상호작용도 발생하지 않으며**, `Update() 등 생명주기(Lifecycle) 함수도 호출되지 않습니다.`{:.warning}

- **예시 코드**
  ```cs
  // 오브젝트 활성화
  gameObject.SetActive(true);
  
  // 오브젝트 비활성화
  gameObject.SetActive(false);
  ```

- **활용** 
  - 일시적으로 GameObject를 **보이지 않게 하거나** **상호작용을 중단**하고 싶을 때 사용합니다. 
  - 예를 들어, 플레이어가 특정 아이템을 습득한 후 그 `아이템을 비활성화`하거나, 특정 조건이 충족되면 오브젝트를 `다시 활성화`하는 데 유용합니다.

## Step 3. 생성과 활성화의 차이

- **메모리 할당 vs 상태 제어** 
  - **생성** : GameObject를 `메모리에 할당`하고 **씬에 추가하는 과정**인 반면, 
  - **활성화** : 이미 생성된 **오브젝트를 보이거나 보이지 않게** 하고, `동작 여부를 제어`하는 과정입니다.
  
- **Awake() vs OnEnable()** 
  - 오브젝트가 **생성**될 때는 `Awake()`가 호출되지만, **활성화**될 때는 `OnEnable()`이 호출됩니다. 
  - 즉, 오브젝트가 생성된 이후에도 `OnEnable()`이 **여러 번 호출될 수 있지만**, `Awake()`는 오브젝트가 **처음 생성될 때 한 번만 호출**됩니다.

- **Awake() vs Start()** 
  - 오브젝트가 생성됐지만 **스크립트(Script)가 비활성화** 되어있으면 `Awake()`만 호출되고 `Start()`는 호출되지 않습니다.
    - 다음 이미지는 **오브젝트가 생성됐지만 스크립트가 비활성화 된 상태**를 보여줍니다.
    ![Script Deactivation]({{ site.baseurl }}/assets/postImgs/20240903/scriptDeactivation.png)
  - 앞선 [**[생명주기 포스팅]**](https://cottoncandygrape.github.io/posts/Unity-Lifecycle/)에서도 설명했다시피 `Start()` 함수는 **한 번만 호출**됩니다.
    - 즉, 스크립트(Script)를 여러 번 활성, 비활성화 시켜도 `Start()` 함수는 한 번만 호출됩니다.

---
이만 포스팅을 마치겠습니다.   
감사합니다.