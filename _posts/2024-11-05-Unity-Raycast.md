---
title : "유니티 레이캐스트(Raycast)란? 사용법, 예제 총 정리 - CCGrape"
categories: [Unity3D]
tags: [Script, Physics]
description: 가상의 레이(광선)을 쏘아 그 레이와 충돌하는 객체를 탐지하는 기술인 레이캐스트(Raycast)에 대해서 알아보겠습니다. 
---

## 목차
**[Step 1. 레이케스트(Raycast) 기본 개념](#step-1-레이케스트raycast-기본-개념)<br/>**
**[Step 2. 레이케스트(Raycast)의 적절한 사용처](#step-2-레이케스트raycast의-적절한-사용처)<br/>**
**[Step 3. 레이케스트(Raycast)의 사용법](#step-3-레이케스트raycast의-사용법)<br/>**
**[Step 4. 레이케스트(Raycast)의 예시](#step-4-레이케스트raycast의-예시)<br/>**

---
## **Step 1. 레이케스트(Raycast) 기본 개념**

Unity에서 **레이캐스트(Raycast)**는 <u>가상의 레이(광선)를 쏘아 그 레이와 충돌하는 객체를 탐지하는 기술</u>입니다. 

이는 주로 **물리적인 충돌 감지**, **캐릭터 시야 범위 체크**, **총알 발사 방향 설정** 등에서 사용됩니다. 
레이캐스트를 통해 개발자는 게임 내에서 **특정 방향으로 쏜 광선이 무엇과 어디에서 충돌**하는지 알 수 있게 되며, 이를 활용해 다양한 게임 메커니즘을 구현할 수 있습니다.

레이캐스트(Raycast)는 주로 **`Physics.Raycast`** 메서드를 사용하여 수행됩니다. 
개발자가 **레이(Ray)를 쏠 위치와 방향**을 지정하면, Unity는 해당 **방향으로 가상의 레이를 쏴 그 레이가 닿는 물체의 정보를 반환**해 줍니다. 
레이캐스트(Raycast)의 핵심 파라미터로는 **시작점(Origin), 방향(Direction), 최대 거리, 충돌 가능한 레이어** 등이 있으며, 이를 적절히 설정해 원하는 목적에 맞게 사용할 수 있습니다.

![Raycast]({{ site.baseurl }}/assets/postImgs/20241106/Raycast.png)

---
## **Step 2. 레이케스트(Raycast)의 적절한 사용처**
Unity에서 레이캐스트는 다양한 게임 개발 상황에서 사용되며, 대표적인 예시는 다음과 같습니다.

- **플레이어 슈팅 및 발사체 충돌**
    - **총알이 발사**되는 경우, 레이캐스트를 사용해 발사 방향으로 충돌하는 지점을 탐지하여 총알이 도달하는 위치를 빠르게 계산할 수 있습니다.
    - 특히 **1인칭 슈팅(FPS) 게임**에서, 레이캐스트를 통해 적중 위치를 계산하여 피격 효과를 연출하거나 적의 체력을 줄이는 데 유용합니다.

- **마우스 클릭으로 오브젝트 선택**
    - 레이캐스트는 **카메라에서 마우스 위치로 광선을 쏴서 마우스 클릭으로 선택한 오브젝트를 감지**하는 데 사용할 수 있습니다. 
        - 이 방법은 **3D 환경에서 마우스가 클릭한 지점의 위치나 오브젝트를 파악**할 때 유용합니다.
    - 주로 RTS(Real-Time Strategy)나 시뮬레이션 게임에서 **플레이어가 선택한 유닛이나 오브젝트를 인식**하는 데 쓰입니다.

- **적 탐지 및 시야 체크**
    - 게임에서 **적 캐릭터가 플레이어를 탐지**하는 데 사용됩니다. 
        - 레이를 플레이어가 있는 방향으로 쏴서 장애물 없이 적이 플레이어를 볼 수 있는지 판단할 수 있습니다.
        - 예를 들어, 플레이어가 장애물 뒤에 숨어 있을 때, 레이캐스트를 통해 장애물에 먼저 충돌하면 플레이어가 가려져 있는 것으로 간주됩니다.

- **VR/AR 환경에서 조작 대상 인식**
    - **VR 환경**에서는 컨트롤러나 손끝에서 레이캐스트를 쏴서 가리키는 오브젝트를 인식하고 조작할 수 있습니다. 
        - 예를 들어, **가상 공간에서 특정 오브젝트를 손으로 선택하거나 이동**하려면 레이캐스트를 사용해 해당 지점을 탐지합니다.
        - 또한, 인터랙션이 필요한 UI 버튼을 가리킬 때도 레이캐스트를 활용해 선택할 수 있습니다.

---
## **Step 3. 레이케스트(Raycast)의 사용법**

**`Physics.Raycast`** 함수들을 사용하기 이전에 **`RaycastHit`**, **`Ray`**를 알아야 합니다. 

### **1) RaycastHit**

**`RaycastHit`**는 Unity에서 레이캐스트의 충돌 결과 정보를 저장하는 **구조체**입니다. 
**레이캐스트가 충돌한 오브젝트와 관련된 다양한 정보를 제공**하며, 주로 다음과 같은 필드를 포함하고 있습니다.

- **collider**  
    - 레이와 충돌한 객체의 `Collider`를 반환합니다. 이를 통해 충돌한 객체의 정보를 가져올 수 있습니다.
    - 예: `hitInfo.collider.gameObject`로 충돌한 게임 오브젝트 접근.

- **point**  
    - **충돌 지점의 월드 좌표**를 나타냅니다.
    - 예: 충돌 위치에 이펙트를 추가하거나, 캐릭터 이동 시 사용할 수 있습니다.

- **normal**  
    - **충돌 지점의 표면 법선 벡터**를 제공합니다. 
    - 충돌한 면의 방향을 알 수 있어 반사나 물리 효과를 계산할 때 유용합니다.

- **distance**  
    - **레이의 시작점에서 충돌 지점까지의 거리**입니다. 
    - 가까운 충돌체를 확인하거나 거리 기반 로직에 활용할 수 있습니다.

- **transform**  
    - 충돌한 오브젝트의 `Transform`을 반환합니다. 
    - 오브젝트 위치, 회전 등을 쉽게 가져올 수 있습니다.

### **2) Ray**  
**`Ray`**는 **시작점(origin)과 방향(direction)**으로 정의된 **직선 광선**을 생성하는 클래스입니다.
주로 **`Physics.Raycast`**와 함께 사용됩니다. 
이 클래스는 레이캐스트를 통해 특정 방향으로 쏘는 가상의 광선을 생성하여 충돌을 감지할 수 있습니다.

다음과 같은 필드를 가지고 있습니다.

- **origin**  
    - 레이의 **시작점**입니다. `Vector3`로 위치를 지정하며, 레이가 **시작하는 좌표**를 나타냅니다.
    - 예: 카메라 위치나 캐릭터 위치에서 시작하도록 설정.

- **direction**  
    - 레이의 **방향**입니다. `Vector3`로 방향을 나타내며, 레이가 **뻗어나가는 방향**을 지정합니다.
    - 이 값은 **정규화(길이 1의 벡터)된 상태로 사용**하는 것이 좋습니다.


### **3) Raycast 사용법 예시**
Unity의 **`Physics.Raycast`** 함수는 다양한 오버로딩이 되어 있어 개발자가 상황에 맞게 사용할 수 있습니다.

```cs
//1
bool Raycast(Vector3 origin, Vector3 direction, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, QueryTriggerInteraction queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

//2
bool Raycast(Vector3 origin, Vector3 direction, out RaycastHit hitInfo, float maxDistance, int layerMask, QueryTriggerInteraction queryTriggerInteraction);

//3
bool Raycast(Ray ray, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, QueryTriggerInteraction queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

//4
bool Raycast(Ray ray, out RaycastHit hitInfo, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, QueryTriggerInteraction queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);
```

> 매개변수가 많아서 복잡해 보이지만 **자주 쓰는 매개변수만 신경쓰면 됩니다.**       
자주 사용하는 **origin(Vector3)**, **direction(Vector3)**, **hitInfo(RaycastHit)**, **ray(Ray)** 을 위주로 설명드리겠습니다.
{: .prompt-info}

#### **1. bool Raycast(Vector3 origin, Vector3 direction)**

이 형태의 함수는 **origin**(시작 지점)에서 **direction**(특정 방향)으로 레이을 쏩니다. 
이 형태는 **충돌 여부만 확인**할 때 유용합니다.

다음 예시코드는 충돌이 발생했을때 로그를 출력합니다.

```cs
if (Physics.Raycast(origin, direction))
{
    Debug.Log("Ray hit something!");
}
```

---
#### **2. bool Raycast(Vector3 origin, Vector3 direction, out RaycastHit hitInfo)**

이 형태의 함수는 광선이 충돌한 지점의 정보를 **RaycastHit** 구조체에 저장합니다. 
앞서 설명한 **RaycastHit**의 정보를 얻을 수 있습니다.

다음 예시는 충돌이 발생했을때 RaycastHit 정보를 로그에 출력합니다.
```cs
RaycastHit hitInfo;
if (Physics.Raycast(origin, direction, out hitInfo))
{
    Debug.Log($"Ray hit {hitInfo.collider.name} at {hitInfo.point}");
}
```


> **Tip : 'out' 키워드란?**<br/>
- **용도**: 함수가 값을 반환하는 데 사용됩니다.       
- **초기화 요구사항** : <u>함수 내부에서 반드시 초기화</u>해야 하고 <u>함수가 호출되기 전에는 변수가 초기화 되어있지 않아도 됩니다.</u>
```csharp
int result;
void ExampleOut(out int result)
{
    result = 10;  // 함수 내부에서 반드시 값을 할당해야 함
}
```
{: .prompt-info}

---
#### **3. bool Raycast(Ray ray, float maxDistance = Mathf.Infinity)**

이 형태는 1번과 유사하지만 **Ray 클래스를 사용**하는 차이가 있습니다.
**Ray** 클래스는 주로 **Camera.ScreenPointToRay**를 통해 **마우스 위치에서 월드 좌표로 레이를 변환**하는 데 사용됩니다. 

이를 통해 **스크린 좌표의 특정 지점**을 기준으로 **3D 레이를 생성하여 오브젝트 선택, 클릭 위치 확인** 등을 처리할 수 있습니다.

다음 예시는 충돌이 발생했을때 로그를 출력합니다.
```cs
Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition); //Camera.main은 주 카메라
if (Physics.Raycast(ray, 100)) //최대 거리 100 unit
{
    print("Hit something!");
}
```

> **Tip : Camera.ScreenPointToRay 이해하기**    
위 예시 코드에서 `Input.mousePosition`에서 얻어지는 마우스 위치는 **스크린 좌표계의 좌표**입니다. 
`Camera.ScreenPointToRay`를 이용하면 **'스크린 좌표'를 '월드 좌표'로 변환**할 수 있습니다. 
이 메서드는 **Ray를 반환**하고 이 Ray는 **카메라 위치에서 해당 월드 좌표 방향으로 쏘는 레이를 생성**합니다.
{: .prompt-info}


---
#### **4. bool Raycast(Ray ray, out RaycastHit hitInfo, float maxDistance = Mathf.Infinity)**

이 형태는 2번과 유사하지만 **Ray 클래스를 사용**하는 차이가 있습니다.

다음 예시는 충돌이 발생했을때 **DrawLine 함수를 이용하여 Ray를 시각적**으로 보여줍니다.
```cs
Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
RaycastHit hit;

if (Physics.Raycast(ray, out hit, 100))
{
    Debug.DrawLine(ray.origin, hit.point);
}
```

> **Tip : Debug.DrawLine이란?**     
```cs
Debug.DrawLine(Vector3 start, Vector3 end, Color color = Color.white, float duration = 0, bool depthTest = true);
```
디버깅 용도로 **두 점 사이에 선을 그려주는 기능**을 제공하는 함수입니다.
매개 변수가 많아서 복잡해 보이지만 **시작점(start)와 끝점(end)**를 주로 사용합니다.
{: .prompt-info}

---
#### **5. bool Raycast(Vector3 origin, Vector3 direction, float maxDistance, int layerMask)**

이 형태는 **지정한 Layer만 레이와 충돌**합니다.  

다음 예시는 지정된 Layer에만 충돌하고 충돌된 정보를 `hit`에 저장합니다.
```cs
Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
RaycastHit hit;
int layerMask = 1 << LayerMask.NameToLayer("YourLayerName"); // 특정 레이어 이름을 사용해 레이어 마스크 설정

if (Physics.Raycast(ray, out hit, 100, layerMask))
{
    Debug.Log("Hit object on specified layer: " + hit.collider.gameObject.name);
    Debug.DrawLine(ray.origin, hit.point, Color.red);
}
```

---
## **Step 4. 레이케스트(Raycast)의 예시**

다음 영상은 [Raycast 사용법 예시의 3번](#3-bool-raycastray-ray-float-maxdistance--mathfinfinity) 을 구현한 것입니다.
마우스를 클릭한 위치에 노란색 원이 생기고 그 방향으로 캐릭터가 달려갑니다.

![Raycast Example]({{ site.baseurl }}/assets/postImgs/20241106/RaycastExample.webp)

**[예시 코드 일부]**

```cs
void MouseClickPoint()
{
    if (Input.GetMouseButtonDown(1)) //마우스 우클릭
    {
        if (!pickPoint) pickPoint = Instantiate(PointPref); //노란색 원 생성

        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition); //마우스 위치에서 Ray 생성
        RaycastHit hitInfo;

        if (Physics.Raycast(ray, out hitInfo)) //충돌시 hitInfo에 정보 저장
            pickPoint.transform.position = hitInfo.point; //노란색 원 좌표를 hitInfo좌표로 초기화
    }
}
```

전체 코드가 궁금하신 분들은 댓글로 질문주세요~

이만 포스팅을 마치겠습니다.     
감사합니다.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3142924323482085"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-3142924323482085"
     data-ad-slot="4010443563"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>