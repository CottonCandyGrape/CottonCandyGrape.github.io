---
title : "[Unity3D] 유니티 허브 다운로드(+사용 방법) - CCGrape"
categories: [Unity3D]
tags: [Basic, Editor]
description: Unity Hub를 설치하여 에디터 버전을 관리하고 프로젝트를 생성하는 방법을 알아봅니다.
---

## 목차
**[Step 0. Unity를 설치하기 전에](#step-0-unity를-설치하기-전에)**<br/>
**[Step 1. Unity Hub 설치하기](#step-1-unity-hub-설치하기)**<br/>
**[Step 2. Unity Hub 로그인하기](#step-2-unity-hub-로그인하기)**<br/>
**[Step 3. Unity Hub로 버전 관리하기](#step-3-unity-hub로-버전-관리하기)**<br/>
**[Step 4. 프로젝트 생성하기](#step-4-프로젝트-생성하기)**<br/>

---
## Step 0. Unity를 설치하기 전에
유니티를 설치하려면 **`버전 정보`**를 먼저 알아야합니다. 그리고 현재 유니티에는 굉장히 많은 버전이 있습니다. 이 많은 버전들을 사용자가 원하는 것들만 관리할 수 있게 해주는 도구가 **`Unity Hub`** 입니다.

이번 포스팅은 **`Windows OS`**, **`Uniny Hub 3.8.0`**을 기반으로 진행하겠습니다.
<br/><br/>

---
## Step 1. Unity Hub 설치하기
- **[Unity Hub Download Link](https://unity.com/kr/download)**

위 링크에 접속하면 아래와 같은 화면이 나오고 빨간 박스 중 편한것을 골라 **Unity Hub 설치 파일**을 다운로드 합니다.

![Unity Hub 다운로드 페이지]({{ site.baseurl }}/assets/postImgs/20240821/UnityHubDownloadPage.png)

**`설치 파일을 실행`**시키고 다음과 같은 순서로 설치를 진행합니다.

- **`동의함`** 선택.

![Unity Hub install 01]({{ site.baseurl }}/assets/postImgs/20240821/hubInstall01.png)
<br/>

- 설치하기 원하는 **`경로 선택`** 후 **`설치`** 버튼 선택.

![Unity Hub install 02]({{ site.baseurl }}/assets/postImgs/20240821/hubInstall02.png)
<br/>

- 그리고 기다리시면 **`자동으로 설치가 완료`**되고 다음과 같은 화면이 나옵니다.

![Unity Hub install 03]({{ site.baseurl }}/assets/postImgs/20240821/hubInstall03.png)

---
## Step 2. Unity Hub 로그인하기

- Unity Hub를 실행하면 맨 처음 로그인을 하라고 다음과 같은 화면이 나옵니다. 빨간 박스를 누르면 유니티 로그인 웹 페이지로 이동하게 되는데 로그인을 하고 돌아옵니다. 아직 계정이 없으신 분들은 회원가입을 해주세요.

![Unity Hub Setting 01]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting01.png)
<br/>

> - <u>로그인 후 다음 화면이 바로 나오면</u> 빨간 박스의 **`Agree`**를 누르고 **<u>이번 Step 은 건너뛰셔도 됩니다.</u>** 아닌 분들은 이 다음 과정들을 진행해 주세요.


![Unity Hub Setting 0202]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting0202.png)
<br/>

- 로그인을 하면 `왼쪽 상단`에 **`계정 이미지`**가 나타나고 `가운데`에 **`라이센스가 없다는 경고`**가 나옵니다. **`톱니바퀴`**나 **`Manage licenses`** 버튼을 눌러서 라이센스를 등록해 줍니다.

![Unity Hub Setting 0201]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting0201.png)
<br/>

- 좌측의 **`Licenses`**탭을 선택하고 **`Add license`**를 클릭합니다.

![Unity Hub Setting 03]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting03.png)
<br/>

- 기존에 사용하고 있던 라이센스가 있지 않고 학습, 취미 등 일반적인 사용자라면 빨간 박스의 **`Get a free personal license`**를 클릭합니다. 그리고 다음 순서대로 빨간 박스를 클릭합니다.

![Unity Hub Setting 04]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting04.png)
![Unity Hub Setting 05]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting05.png)
<br/>

- 최종적으로 **`Personal License가 생성`**되었고 다시 **`Projects`** 탭으로 돌아가면 `경고 표시가 사라진 것`을 확인할 수 있습니다.

![Unity Hub Setting 06]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting06.png)
![Unity Hub Setting 07]({{ site.baseurl }}/assets/postImgs/20240821/hubSetting07.png)

---
## Step 3. Unity Hub로 버전 관리하기

제목을 <u>"버전 관리하기"</u>라고 적었지만 사실 **Hub가 알아서 해주기 때문에** 사용자는 **사용할 버전을 다운받기**만 하면 됩니다.

- **[Unity 다운로드 아카이브 Link](https://unity.com/kr/releases/editor/archive)**

위 링크에 접속하면 아래와 같은 화면이 나오고 자신이 원하는 버전을 선택하여 다운로드 받으면 됩니다. **`LTS(Long Term Support)`** 버전은 쉽게 말해 **안정된 버전**이라는 뜻이니 무조건 최신 버전보다는 **LTS 버전을 다운받는 것을 권장**합니다.

- 원하는 버전을 선택했으면 허브 설치의 **`INSTALL->`** 버튼을 클릭합니다. 저는 **<u>2022.3.39f1 버전</u>**을 설치해보겠습니다.

![Editor Download 01]({{ site.baseurl }}/assets/postImgs/20240821/editorDownload01.png)
<br/>

- 첫 번째 체크박스는 **`Visual Studio 2022`**를 설치할 것인지 선택합니다. 다른 버전을 쓰고 계시면 굳이 설치하지 않으셔도 됩니다. 
다음 체크박스는 **`안드로이드 빌드`**를 할 것이면 그림처럼 3개를 다 체크해 주시고 아니면 다 체크해제 해주세요.

> 그 밑에 `IOS Build Support`는 `Mac`에서만 정상 작동합니다. <u>Windows에서는 IOS 빌드가 안됩니다.</u> (하는 방법이 있다고는 하는데 Mac을 사용하는 것이 정신건강에 더 좋다고 합니다...)

![Editor Download 02]({{ site.baseurl }}/assets/postImgs/20240821/editorDownload02.png)
<br/>

- 안드로이드 관련 동의를 해주시고 **`Install`**

![Editor Download 03]({{ site.baseurl }}/assets/postImgs/20240821/editorDownload03.png)
![Editor Download 04]({{ site.baseurl }}/assets/postImgs/20240821/editorDownload04.png)
<br/>

- 설치가 완료되고 Unity Hub 좌측의 **`Installs`** 탭을 선택하면 방금 설치한 버전(**2022.3.39f1 LTS**)이 추가된 것을 볼 수 있습니다.

![Editor Download 05]({{ site.baseurl }}/assets/postImgs/20240821/editorDownload05.png)

---
## Step 4. 프로젝트 생성하기

- **`Projects`**탭의 우측 상단에서 **`New project`** 버튼을 눌러 프로젝트를 생성합니다.

![Create Project 01]({{ site.baseurl }}/assets/postImgs/20240821/createProj01.png)
<br/>

- 화면 `상단 가운데`에 `설치된 버전`이 표시되고 여러개가 설치되면 클릭하여 버전을 선택할 수 있습니다. 그 밑의 박스는 **프로젝트를 2D로 할 것인지 3D로 할 것인지 정하는 것**인데 <u>그리 중요하지 않습니다.</u> **프로젝트를 생성한 후에 내부에서도 수정할 수 있습니다.**

- `화면 우측`에서 프로젝트 **`이름`**과 **`경로`**를 정해주고 **`Create project`**를 눌러 **프로젝트를 생성**합니다.

![Create Project 02]({{ site.baseurl }}/assets/postImgs/20240821/createProj02.png)
<br/>

- 다시 **`Projects`**탭으로 돌아오면 **`설정한 버전`**으로 **`프로젝트가 생성된 것`**을 확인할 수 있습니다.

![Create Project 03]({{ site.baseurl }}/assets/postImgs/20240821/createProj03.png)