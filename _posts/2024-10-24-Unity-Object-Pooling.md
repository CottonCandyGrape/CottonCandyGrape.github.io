---
title : "유니티 오브젝트 풀링(Object Pooling) 구현하기 - CCGrape"
categories: [Unity3D]
tags: [Script]
description: 생성과 소멸이 자주 반복적으로 일어나는 객체들을 오브젝트 풀로 효율적으로 관리하는 방법을 알아봅니다.
---

## 목차
**[Step 1. 개념](#step-1-오브젝트-풀링object-pooling-개념)<br/>**
**[Step 2. 기본 원리](#step-2-오브젝트-풀링의-기본-원리)<br/>**
**[Step 3. 사용하는 이유](#step-3-오브젝트-풀링을-사용하는-이유)<br/>**
**[Step 4. 사용 시기](#step-4-오브젝트-풀링-사용-시기)<br/>**
**[Step 5. 구현하기](#step-5-오브젝트-풀링-구현하기)<br/>**
**[Step 6. 장단점](#step-6-오브젝트-풀링의-장단점)<br/>**
**[Step 7. 최적화 팁](#step-7-오브젝트-풀링-최적화-팁)<br/>**

---
## **Step 1. 오브젝트 풀링(Object Pooling) 개념**

성능을 최적화하기 위해 **필요한 오브젝트를 미리 생성해 두고 재사용**하는 기법입니다. 
이 방법은 **실시간 생성(Instantiate())과 소멸(Destroy())에 따른 비용**(CPU, 메모리)을 줄이는 데 유용합니다.

반복적으로 사용되는 오브젝트(총알, 몬스터, 파편 등)를 매번 **생성(Instantiate()), 파괴(Destroy())**하지 않고, **재사용 가능한 풀에 보관**하는 것이 핵심입니다.

---
## **Step 2. 오브젝트 풀링의 기본 원리**  
1. **초기화 단계**  
    - 게임이 시작될 때, 사용할 오브젝트(예: 몬스터)를 **미리 여러 개 생성**합니다.  
    - 이 생성된 오브젝트는 **비활성화 상태**로 풀에 저장됩니다.

2. **사용 단계**
    - 오브젝트가 필요할 때 풀에서 하나를 꺼내 **활성화**합니다.
    - 예를 들어, 몬스터가 죽을 때 마다 새로 생성하지 않고 **미리 생성된 몬스터 오브젝트를 사용.**

3. **반환 단계**  
    - 오브젝트의 사용이 끝나면(예:몬스터 죽음) **비활성화** 시켜 풀로 **반환**합니다. 이후 다시 필요할 때 재사용됩니다.

---
## **Step 3. 오브젝트 풀링을 사용하는 이유**

1. **GC(Garbage Collection) 비용 절감**  
    - C#과 같은 언어에서는 메모리에서 오브젝트를 파괴할 때 **가비지 컬렉터(GC)**가 주기적으로 메모리를 회수합니다. 그러나 이는 **프레임 드랍**을 유발할 수 있습니다.
    - 오브젝트 풀링은 오브젝트의 <u>생성, 소멸을 최소화</u>해 **GC 호출을 줄여** 성능을 유지합니다.

2. **메모리 단편화(Memory fragmentation) 방지하기**
    - 메모리 단편화에는 **내부 메모리 단편화**와 **외부 메모리 단편화**가 있는데 생성, 소멸을 반복할 때는 **외부 메모리 단편화**가 발생합니다.
    - 이를 해결하기 위해 **미리 생성한 오브젝트를 재사용**합니다.

    > **메모리 단편화**는 추후 포스팅에서 자세히 다루겠습니다.
    {: .prompt-info}

--- 
## **Step 4. 오브젝트 풀링 사용 시기**

- **몬스터, 총알, 파편** 등 자주 생성되고 빨리 사라지는 오브젝트가 있을 때.
- **파티클 이펙트**처럼 자주 사용되는 효과가 있을 때.
- **메모리 최적화**와 **일관된 성능 유지**가 중요할 때.

--- 
## **Step 5. 오브젝트 풀링 구현하기**

> **오브젝트 풀을 관리할 클래스(ObjectPoolMgr.cs)**와 **풀에 사용될 객체(Monster.cs) 클래스** <u>2개</u>를 만들어야 합니다.
{: .prompt-info}


### ObjectPoolMgr.cs 설명

- **몬스터 프리팹**과 **몬스터 풀이 될 리스트**를 선언합니다.
- **초기 생성 개수**를 정해줍니다.
- Start()에서 시작하자마자 **미리 초기 생성 개수만큼 생성하고 비활성화** 시킵니다.
- **AddMonsterPool()** 함수를 호출하여 필요할때마다 몬스터를 풀에서 꺼내옵니다.
    > 호출 후 그 몬스터 객체를 반드시 **"활성화(gameObject.SetActive(true))"**하여 사용해야 합니다!
    {: .prompt-warning}

```cs
//ObjectPoolMgr.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectPoolMgr : MonoBehaviour
{
    public GameObject Monster = null; //몬스터 프리팹
    List<MonsterCtrl> MonCtrlPool = new List<MonsterCtrl>(); //몬스터 풀

    int initMonCnt = 30; //초기 생성 개수

    void Start()
    {
        for (int i = 0; i < initMonCnt; i++) //몬스터 생성 후 비활성화
        {
            GameObject mon = Instantiate(Monster);
            mon.SetActive(false);
            MonCtrlPool.Add(mon.GetComponent<MonsterCtrl>());
        }
    }

    public MonsterCtrl AddMonsterPool() //풀에 몬스터 추가 또는 몬스터 꺼내는 함수 
    {
        for (int i = 0; i < MonCtrlPool.Count; i++)
        {
            if (!MonCtrlPool[i].gameObject.activeSelf) //풀에 비활성화 되있는 것이 하나라도 있으면 꺼내기
                return MonCtrlPool[i];
        }

        //하나도 없으면 
        GameObject mon = Instantiate(Monster); //새 몬스터 생성
        mon.SetActive(false); //비활성화
        MonsterCtrl monCtrl = mon.GetComponent<MonsterCtrl>();
        MonCtrlPool.Add(monCtrl); //풀에 추가 후

        return monCtrl; //꺼내기
    }
}
```

### MonsterCtrl.cs 설명

- 몬스터가 죽으면 **비활성화 시켜 풀에 반환**됩니다.

```cs
//MonsterCtrl.cs 
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MonsterCtrl : MonoBehaviour
{
    void MonsterDie() //몬스터 죽을때 호출되는 함수
    {
        gameObject.SetActive(false); //비활성화 하면서 풀에 반환
    }
}
```

### 구현 예시
- 게임 제작 중 오브젝트 풀링을 이용하여 몬스터를 스폰시키는 장면입니다.
- 몬스터들이 나타나고 죽으면서 오브젝트가 **활성, 비활성** 되는 것을 볼 수 있습니다.

![ObjectPooling Example]({{ site.baseurl }}/assets/postImgs/20241024/MemoryPool.webp)


> **AddMonsterPool()**을 호출하여 몬스터를 조작하는 코드나 **MonsterDie()**가 호출되는 부분은 넣지 않았습니다.    
각자의 상황과 조건에 맞게 호출하여 사용해보세요~!
{: .prompt-info}

---
## **Step 6. 오브젝트 풀링의 장단점**

### **장점**
1. **성능 최적화**  
    - 실시간 게임에서 <u>자주 사용되는 오브젝트</u>를 **매번 생성, 소멸하지 않아 성능이 개선**됩니다.
   
2. **GC 호출 최소화**  
    - 가비지 컬렉션으로 인한 성능 저하를 줄입니다.

3. **일관된 프레임 속도 유지**  
    - 오브젝트 풀링을 통해 오브젝트 생성, 소멸에 따른 일시적 성능 저하를 방지합니다.

### **단점**
1. **초기 메모리 부담**  
    - 처음부터 다수의 오브젝트를 생성하기 때문에 메모리 사용량이 증가할 수 있습니다.

2. **관리 복잡성 증가**  
    - 풀을 관리하는 로직이 필요하며, 잘못된 관리로 메모리 누수가 발생할 수 있습니다.

3. **동적 상황 대응이 어려움**  
    - 예측하기 힘든 오브젝트 수요가 발생할 경우, 풀의 크기가 부족해 새 오브젝트를 생성해야 할 수 있습니다.

---
## **Step 7. 오브젝트 풀링 최적화 팁**  
1. **초기 생성 개수(풀 크기) 조정**  
    - 오브젝트를 너무 많이 생성하면 초기 메모리 사용량이 높아지므로 **적절한 수를 설정**합니다.  

2. **비동기 생성**  
    - 초기 생성 개수가 많다면 플레이 시작시 잠시 버벅이는 현상이 있을 수 있습니다.
    - 이때 **게임 로딩시부터 비동기적으로 생성**하면 부드럽게 시작할 수 있습니다.

<br/>

---
**포스팅의 예시로 사용된 게임을 플레이하고 싶으신 분들은 스토어에 `bunnybunny`를 검색하시거나 해당 `스토어 이미지`를 클릭해 주세요~!**

[![애플 앱 스토어]({{ site.baseurl }}/assets/postImgs/appstore.png)](https://apps.apple.com/kr/app/bunnybunny-io/id6504274647?platform=iphone)
[![구글 플레이 스토어]({{ site.baseurl }}/assets/postImgs/google.png)](https://play.google.com/store/apps/details?id=com.ccGrape.BunnyBunny)

궁금한 점은 댓글로 남겨주세요.      
감사합니다.