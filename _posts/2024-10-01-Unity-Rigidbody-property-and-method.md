---
title : "유니티 Rigidbody 속성, 함수 총 정리 - CCGrape"
categories: [Unity3D]
tags: [Basic, Physics]
description: 유니티에서 Rigidbody는 GameObject에 물리적 특성을 부여하는 컴포넌트입니다. 물리 엔진의 영향을 받아 GameObject가 더욱 사실적으로 움직일 수 있게 도와줍니다.
---

## 목차
**[Step 1. Rigidbody의 속성](#step-1-rigidbody의-속성)<br/>**
**[Step 2. Rigidbody 자주 사용되는 함수](#step-2-rigidbody-자주-사용되는-함수)<br/>**
**[Step 3. 마무리](#step-3-마무리)<br/>**

---
유니티에서 **`Rigidybody`**는 GameObject에 **물리적 특성을 부여**하는 컴포넌트로 **중력, 충돌, 마찰 등** 물리적 현상에 반응하게 할 수 있습니다.
이를 활용하면 각 GameObject들이 사실적으로 움직이게하여 사용자에게 몰입감을 줄 수 있기 때문에 게임 개발에서 중요한 요소입니다.

이번 포스팅에서는 **Rigidbody**를 총 정리하는 시간을 가져보겠습니다. 

---
## **Step 1. Rigidbody 속성**

**Rigidbody**에는 **3D GameObject**에 사용하는 **`Rigidbody`**와 **2D GameObject**에 사용하는 **`Rigidbody2D`**가 있습니다.
두 컴포넌트 사이에는 **공통되는 속성**이 있어 그 속성들과 **자주 사용하는 속성**들을 위주로 설명하겠습니다.

### **① Rigidbody(3D GameObject)**
![Rigidbody]({{ site.baseurl }}/assets/postImgs/20241001/Rigidbody.png)
- **Mass**
    - **물체의 무게**를 나타내며, 힘을 적용했을때 물체가 얼마나 움직이는지를 결정합니다.

- **Drag**
    - 물체의 속도가 증가할 때 그 **속도를 감소시키는 효과**를 제공합니다. Drag가 크면 물체가 더 빨리 멈추고, 작으면 더 멀리 이동할 수 있습니다. 
    - 일반적으로 물체의 이동 속도를 감소시키는 데 중요한 역할을 합니다.

- **Angular Drag**
    - 물체의 **회전 속도를 감소**시키는 데 사용됩니다. 값이 클수록 회전이 더 빨리 멈춥니다.

- **Use Gravity**
    - 활성화 시 Rigidbody가 **중력의 영향**을 받습니다. 
    - 기본적으로 이 속성은 활성화되어 있어서 물체가 중력에 따라 떨어집니다. 비활성화하면 중력을 무시하게 됩니다.
    - Edit -> Project Settings -> Physics 또는 Physics 2D -> Gravity : **해당 X, Y, Z 값 만큼 중력을 받습니다.**
    ![Gravity]({{ stie.baseurl }}/assets/postImgs/20241001/Gravity.png)

- **Is Kinematic**
    - 활성화 시 **물리 엔진으로 제어되지 않고** Script에서 Transform을 이용하여 제어할 수 있습니다.

- **Interpolate**
    - 물체가 한 프레임에서 다음 프레임으로 **자연스럽게 이동**하도록 도와줍니다.
        - **None** : 보간이 적용되지 않음.
        - **Interpolate** : 이전 프레임의 Transform에 맞게 이동을 부드럽게 처리합니다.
        - **Extrapolate** : 다음 프레임의 Transform을 추정해 이동을 부드럽게 처리합니다.

- **Collision Detection**
    - Rigidbody가 **충돌을 감지하는 방식을 설정**합니다.
    - **Discrete(Dafault)**
        - Physics Loop 마다 충돌을 확인합니다.
        - 빠르게 움직이는 물체가 충돌 감지가 되지 않아 다른 물체를 통과하는 **'터널링'** 문제가 발생할 수 있습니다.
    - **Continuous**
        - **'터널링'**을 방지할 수 있어 **빠르게 움직이는 오브젝트에 사용**할 수 있습니다.
        - **마지막 물리 타임스텝에서 다음 타임스텝까지 미리 예측**하고 해당 시간 동안 GameObject가 무엇과 충돌하는지 확인합니다.
        - **Static Collider**에 대해서만 확인합니다.
    - **Continuous Dynamic**
        - Continuous와 비슷하지만 **Continuous Dynamic으로 설정된 다른 Dynamic Collider와의 충돌도 확인**합니다.
        - CPU를 가장 많이 사용하지만 가장 정확합니다.
    - **Continuous Speculative**
        - Continuous Dynamic과 유사한 정확도를 제공할 수 있지만 CPU 사용은 더 낮고 충돌감지에 **예측적 접근 방식**을 사용합니다.
        - 모든 GameObject가 현재 방향으로 계속 이동한다고 가정하고 이를 기반으로 잠재적인 충돌을 계산합니다.

- **Constraints**
    - 특정 축의 회전이나 위치를 잠글 수 있어 **물체의 움직임을 제한**할 수 있습니다. 
    - ex) X 축 방향으로만 회전하도록 제한할 수 있습니다.
    
### **② Rigidbody2D(2D GameObject)**
![Rigidbody2D]({{ site.baseurl }}/assets/postImgs/20241001/Rigidbody2D.png)
- **BodyType**
    - **Dynamic**
        - **모든 물리 현상을 받습니다.** (중력, 충돌에 의한 힘 등)
    - **Kinematic**
        - **물리 현상을 받지 않고** Script에서 Transform을 이용하여 제어할 수 있습니다.
        - 물리와 상관없이 프로그래머의 목적을 가지고 제어할 때 사용합니다.
        - **Dynamic Rigidbody**를 만나야 충돌합니다.
            - (Static - Kinematic)간의 충돌은 일어나지 않습니다.
            - **Use FullKinematic Contacts**를 활성화하면 모든 Body Type과 충돌 상호작용 합니다.
    - **Static**
        - **물리 현상을 받지 않고 움직이지 않습니다.**
        - `rigidbody.velocity`, `rigidbody.position`, `MovePosition()` 등을 사용해도 위치가 변경되지 않습니다.
        - 무조건 **Dynamic Type** 과만 충돌합니다.

- **Simulated**
    - 비활성화 시 물리적 상호작용을 하지 않습니다. (ex. 충돌하지 않습니다.)

> **`Rigidbody`**와 **`Rigidbody2D`**는 서로 충돌하지 않습니다!
{: .prompt-info}

---
## **Step 2. Rigidbody 자주 사용되는 함수**

### **① AddForce(Vector3 force)**

GameObject에 **힘**을 가합니다. 이 힘은 물체의 **질량과 속도**에 영향을 줍니다.

```cs
public class ApplyForce : MonoBehaviour
{
    Rigidbody rb;

    void Start() { rb = GetComponent<Rigidbody>(); }

    void Update()
    {
        //Space 키를 누를 때 위쪽 방향으로 힘을 추가하여 물체를 위로 상승시킵니다.
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.AddForce(Vector3.up * 500);
        }
    }
}
```

### **② AddTorque(Vector3 torque)**

GameObject에 **회전력**을 추가하여 **GameObject를 회전**시킵니다.

```cs
public class ApplyTorque : MonoBehaviour
{
    Rigidbody rb;

    void Start() { rb = GetComponent<Rigidbody>(); }

    void Update()
    {
        //'T' 키를 누르면 GameObject를 Y축을 기준으로 회전시키는 효과를 줍니다.
        if (Input.GetKeyDown(KeyCode.T))
        {
            rb.AddTorque(Vector3.up * 10, ForceMode.VelocityChange);
        }
    }
}
```

### **③ MovePosition(Vector3 position)**

`Rigidbody`가 있는 GameObject의 **위치를 부드럽게 이동**시킵니다. 

```cs
public class MoveObject : MonoBehaviour
{
    public float speed = 5f;
    Rigidbody rb;

    void Start() { rb = GetComponent<Rigidbody>(); }

    void FixedUpdate()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        //방향 값 계산
        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);
        rb.MovePosition(rb.position + movement * speed * Time.fixedDeltaTime);
    }
}
```

### **④ MoveRotation(Quaternion rot)**

`Rigidbody`가 있는 GameObject를 **부드럽게 회전**시킵니다. 

```cs
public class RotateObject : MonoBehaviour
{
    public float rotSpeed = 100f;
    Rigidbody rb;

    void Start() { rb = GetComponent<Rigidbody>(); }

    void FixedUpdate()
    {
        // 회전 값 계산 (y축을 기준으로 회전)
        Quaternion deltaRotation = Quaternion.Euler(0f, rotSpeed * Time.fixedDeltaTime, 0f);
        rb.MoveRotation(rb.rotation * deltaRotation);
    }
}
```

---
## **Step 3. 마무리**

이번 포스팅에서는 **`Rigidbody`**의 **속성값**들과 기본적으로 **자주 쓰이는 함수**에 대해서 알아보았습니다.
포스팅 내용을 참고하여 실감나고 몰입도 높은 게임을 만드는 데 도움이 되길 바랍니다!

궁금한 점은 댓글로 남겨주세요.      
감사합니다.