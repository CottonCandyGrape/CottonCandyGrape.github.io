---
title : "유니티 Prefab 기초와 활용법 - CCGrape"
categories: [Unity3D]
tags: [Basic, Script, Editor]
description: 유니티에서 가장 편리한 기능 중 하나인 Prefab에 대해서 알아봅니다.
---

## 목차
**[Step 0. 유니티 Prefab : 게임 개발의 핵심 도구](#step-0-유니티-prefab--게임-개발의-핵심-도구)**      
**[Step 1. Prefab 정의](#step-1-prefab-정의)**        
**[Step 2. Prefab의 활용법](#step-2-prefab의-활용법)**    
**[Step 3. Prefab의 장단점](#step-3-prefab의-장단점)**    

---
## Step 0. 유니티 Prefab : 게임 개발의 핵심 도구

게임 개발을 하면서 같은 오브젝트를 **여러 번 재사용**해야 하는 경우가 많습니다. 
이를 **효율적으로 관리하고 사용**하기 위해 Unity에서는 `Prefab`이라는 훌륭한 개념을 제공합니다. 

이번 포스팅에서는 Prefab의 **정의**에서부터 그 **활용 방법**, **장단점**까지 속속들이 파헤쳐 봅니다.

---
## Step 1. Prefab 정의

`Prefab`은 Unity의 강력한 기능 중 하나로, GameObject와 해당 구성 요소들을 저장하여 **<u>재사용</u>**할 수 있게 도와줍니다. 
이는 **<u>일종의 템플릿</u>**이라고 생각할 수 있으며, 다양한 환경에서 **<u>여러 번 동일한 오브젝트를 생성하고 사용</u>**할 수 있게 해줍니다.

---
## Step 2. Prefab의 활용법 

- 게임에서 **'아이템'**을 **여러 번 생성**해야 하는 경우가 있다고 가정해 봅시다. 
    - 매번 새롭게 게임 오브젝트를 만들고, 동일한 구성 요소(스프라이트, 애니메이션, 스크립트 등)를 추가하는 것은 매우 **비효율적**입니다. 
    - 이럴 때 한 번 **'아이템'**를 만들어 놓고 이를 `Prefab`으로 저장해 두면, 필요할 때마다 쉽게 같은 아이템을 생성할 수 있습니다.

1. **아이템 Prefab 생성**
    - 아이템 모델을 설정하고 필요한 컴포넌트(예: Rigidbody, Collider 등)를 추가합니다.
    - 완성된 아이템 오브젝트를 **프로젝트 창으로 <u>드래그</u>하여 Prefab**으로 만듭니다.
    - Prefab이 생성되면 GameObject **아이콘이 파란색**으로 변합니다.
        - <u>파란색 GameOjbect는 프리팹이라는 뜻입니다.</u>
    ![Bomb Prefab]({{ site.baseurl }}/assets/postImgs/20240906/bombPrefab.png)      
    <br/>

2. **사용**
    - 스크립트나 Unity의 하이라키 창을 통해 언제든지 해당 아이템 Prefab을 인스턴스화하여 게임에 추가할 수 있습니다.

    - **예시 코드**     

    ```csharp
    public GameObject bombPrefab;

    void SpawnBomb(Vector3 position)
    {
        Instantiate(bombPrefab, position, Quaternion.identity);
    }
    ```

---
## Step 3. Prefab의 장단점

### 3.1 장점 
- **재사용성**
    - 한 번 만든 오브젝트를 필요할 때마다 쉽게 생성할 수 있습니다. 
    - 이는 시간이 절약될 뿐만 아니라 코드와 프로젝트의 **일관성을 유지**할 수 있게 합니다.      
- **효율적인 관리**
    - Prefab으로 생성된 모든 인스턴스들은 **원본 Prefab을 수정하는 것만으로 일관되게 변경**됩니다. 
    - 따라서 **일괄적인 수정**이 매우 용이합니다.   
- **모듈화**
    - Prefab을 사용하면 프로젝트를 **모듈화**할 수 있어, **코드와 메모리 관리가 더 용이**해집니다. 
    - 필요할 때 마다 모듈 단위로 개발하고 테스트할 수 있습니다.     
- **협업 강화**
    - 여러 개발자들이 동시에 같은 프로젝트를 작업할 때, Prefab은 **중앙 제어용 오브젝트를 제공**하여 **작업 충돌을 최소화**해 줍니다.

### 3.2 단점
- **의존성 문제**
    - **원본 Prefab에 많은 수정**이 가해질 경우, 이를 사용하는 **모든 인스턴스에서 예기치 않은 문제**가 발생할 수 있습니다.     
- **복잡성 증가**
    - 복잡한 Prefab을 다루는 데 있어서, 특히 **여러 계층의 Prefab이 중첩되면 관리가 오히려 어려워질 수 있습니다.**      
- **메모리 사용**
    - **많은 수의 Prefab 인스턴스를 생성**하면 **메모리 사용량이 급증**할 수 있어 **성능 저하**를 초래할 수 있습니다.

---
이만 포스팅을 마치겠습니다.     
감사합니다.