---
layout: article 
title : 유니티 에디터 기초 용어(+레이아웃)
tags: Basic Editor
excerpt: 유니티 에디터 기초 용어와 사용법을 알아봅니다. 각 개발 상황별로 알맞는 레이아웃을 선택합니다.
---

## 목차
**[Step 1. 유니티 에디터 각 부분 용어 및 설명](#step-1-유니티-에디터-각-부분-용어-및-설명)**<br/>
**[Step 2. 개발 상황별 알맞는 에디터 레이아웃](#step-2-개발-상황별-알맞는-에디터-레이아웃)**<br/>

---
해당 포스팅은 `Windows OS`{:.info}, `Unity 2022.3.15f1`{:.info}을 기준으로 작성되었습니다.

## Step 1. 유니티 에디터 각 부분 용어 및 설명 
### ① Scene View (씬 뷰)
![Scene View]({{ site.baseurl }}/assets/postImgs/20240827/sceneView.png){:.rounded}

- **설명**      
    - 게임 오브젝트를 배치하고 편집하는 창입니다. 
    - 2D, 3D로 전환할 수 있으며, 카메라나 라이트와 같은 요소를 배치하고 조작할 수 있습니다.             

- **기능**      
    - 오브젝트 선택 및 이동, 회전, Gizmo 사용, 다양한 뷰 모드 제공 등이 있습니다.   
    
- **Tip(마우스 활용법)**
    - 휠 버튼 클릭하면서 움직이면 수평, 수직 이동이 가능합니다.
    - 우 클릭하면서 움직이면 시야가 회전 됩니다.
    - 우 클릭하면서 w,a,s,d 를 누르면 카메라 방향대로 시야가 이동합니다.

### ② Game View (게임 뷰)
![Game View]({{ site.baseurl }}/assets/postImgs/20240827/gameView.png){:.rounded}

- **설명**
    - 현재 개발 중인 게임이 어떻게 보일지를 실시간으로 미리볼 수 있는 창입니다.
    - 플레이 모드를 통해 게임을 실행하고 테스트할 수 있습니다.

- **기능** 
    - 해상도, 화면 비율, 다양한 뷰 옵션을 설정할 수 있습니다.

### ③ Hierarchy View (하이라키 뷰)
![Hierarchy View]({{ site.baseurl }}/assets/postImgs/20240827/hierarchyView.png){:.rounded}

- **설명**
    - 씬(Scene)에 있는 모든 게임 오브젝트(GameObject)를 계층 구조로 표시하는 창입니다. 
    - 오브젝트를 부모-자식 관계로 배치할 수 있습니다.

- **기능** 
    - 게임 오브젝트 추가/삭제, 계층 구조 편집, 오브젝트 검색 및 필터링을 할 수 있습니다.

### ④ Project View (프로젝트 뷰)
![Project View01]({{ site.baseurl }}/assets/postImgs/20240827/projectView01.png){:.rounded}

- **설명**
    - 프로젝트 내의 모든 에셋(Assets)을 파일 및 폴더 구조로 관리하는 창입니다.
    - 스크립트, 프리팹, 오디오, 텍스처 등의 모든 리소스가 여기에 포함됩니다.

- **기능**
    - 에셋 관리 및 조직화, 에셋 임포트/익스포트, 새로운 에셋 생성이 가능합니다.

- **Tip**
    - 파일 및 폴더가 **사전순으로 배치**되기 때문에 자주 쓰는 것들은 `_(언더바)`{:.info}를 붙여 맨 앞으로 보낼 수 있습니다.
    - 오른쪽 하단 빨간 박스의 스크롤을 조정하면 파일 및 폴더 보기를 수정할 수 있습니다. 다음은 가장 작게 했을때의 예시입니다.
    ![Project View02]({{ site.baseurl }}/assets/postImgs/20240827/projectView02.png){:.rounded}

### ⑤ Console View (콘솔 뷰)
![Console View]({{ site.baseurl }}/assets/postImgs/20240827/consoleView.png){:.rounded}

- **설명** 
    - 디버깅과 로그 메시지, 경고, 오류 메시지를 표시하는 창입니다. 
    - 코드 오류를 확인하고 디버깅할 수 있습니다.

- **기능** 
    - 로그 메시지 확인, 오류 메시지 분석, 메시지 필터링 등을 합니다.

- **Tip**
    - Console View가 꺼졌을 때
        - Window -> General -> Console      
        `OR`
        - Ctrl + Shift + C `(Windows)`{:.info}
        - Command + Shift + C `(Mac)`{:.info}

---
## Step 2. 개발 상황별 알맞는 에디터 레이아웃 

### ① Default Layout    
![Default Layout]({{ site.baseurl }}/assets/postImgs/20240827/default.png){:.rounded}

- **설명** 
    - 유니티의 기본 레이아웃으로, 좌측에 Hierarchy, 하단에 Project 뷰, 중앙에 Scene 뷰와 Game 뷰가 배치되어 있습니다.

- **장점**
    - 다양한 작업에 적합한 균형 잡힌 레이아웃입니다. 초보자에게 익숙한 환경입니다.
- **단점**
    - 특정 작업에 최적화되지 않아, 필요에 따라 자주 창을 이동해야 할 수 있습니다.
- **추천 사용 상황**
    - 일반적인 게임 개발 작업, 멀티 작업 환경

### ② 2 by 3 Layout      
![2 by 3 Layout]({{ site.baseurl }}/assets/postImgs/20240827/2by3.png){:.rounded}

- **설명**
    - 상단에 큰 Scene 뷰와 하단에 Game 뷰, Project 뷰, Inspector, Hierarchy 창을 나란히 배치한 레이아웃입니다.
- **장점**
    - Scene과 Game 뷰를 동시에 볼 수 있어, 레벨 디자인이나 오브젝트 배치를 할 때 유용합니다.
- **단점**
    - 각 창이 크지 않아 작업 공간이 다소 협소할 수 있습니다.
- **추천 사용 상황**
    - 레벨 디자인, 씬 편집, 3D 오브젝트 배치

### ③ 4 Split Layout    
![4 Split Layout]({{ site.baseurl }}/assets/postImgs/20240827/4split.png){:.rounded}

- **설명**
    - Scene 뷰가 4개의 창으로 분할되어 X, Y, Z 축 방향을 동시에 볼 수 있는 레이아웃입니다.
- **장점**
    - 3D 오브젝트의 정확한 배치와 이동이 가능하며, 여러 각도에서 작업할 수 있습니다.
- **단점**
    - Scene 뷰 외의 창(Inspector, Hierarchy 등)들이 작아져 다른 작업이 불편할 수 있습니다.
- **추천 사용 상황**
    - 복잡한 3D 모델링, 정밀한 오브젝트 배치 작업

### ③ Custom Layout    

유니티에서 제공하는 레이아웃 프리셋은 작업 특성에 따라 변경할 수 있습니다. 
Default 레이아웃은 균형 잡힌 구성이지만, 프로젝트 특성에 따라 `커스터마이징`{:.info}하는 것이 효율적입니다.

저는 현재 개발 중인 `모바일 게임`{:.info}이 있습니다. 
스마트폰을 세로로 놓고 하는 게임이라 `2 by 3`{:.info} 를 세로로 놓는 방식으로 약간 변형하여 사용하고 있습니다.
이렇게 Scene과 Game View를 실제 스마트폰에서 구동되는 것과 같이 볼수 있으므로 개발에 큰 도움이 됩니다.

![Custom Layout]({{ site.baseurl }}/assets/postImgs/20240827/bunny.png){:.rounded}

- **Tip(레이아웃 저장하기)**
    - 오른쪽 상단 박스의 버튼을 누르면 `Save Layout`{:.info}라는 버튼이 나옵니다.
    - 그 후 이름을 정하면 현재 레이아웃이 저장이 됩니다.
    - 작업 중 레이아웃이 흐트러져도 저장된 레이아웃을 불러올 수 있습니다. 

---
**제 게임을 플레이하고 싶으신 분들은 다음 링크를 이용해 주세요~!**

**구글 플레이 스토어**
<!--{% linkpreview "https://play.google.com/store/apps/details?id=com.ccGrape.BunnyBunny" %}

**애플 앱스토어**
{% linkpreview "https://apps.apple.com/kr/app/bunnybunny-io/id6504274647?platform=iphone" %}
-->