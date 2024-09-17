---
title : "[Unity3D] 유니티 PlayerPrefs를 활용한 데이터 관리 - CCGrape"
categories: [Unity3D]
tags: [Basic, Script]
description: 유니티에서 정보를 저장하는 유용한 방법 중 하나인 PlayerPrefs에 대해서 알아봅니다. 
---

## 목차
**[Step 1. PlayerPrefs란 무엇인가?](#step-1-playerprefs란-무엇인가)<br/>**
**[Step 2. 게임에서의 PlayerPrefs 활용법](#step-2-게임에서의-playerprefs-활용법)<br/>**
**[Step 3. PlayerPrefs의 사용 용도](#step-3-playerprefs의-사용-용도)<br/>**
**[Step 4. PlayerPrefs 데이터 저장 경로](#step-4-playerprefs-데이터-저장-경로)<br/>**
**[Step 5. 마무리 요약](#step-5-마무리-요약)<br/>**

---
Unity3D에서 게임 데이터 관리는 효율적인 게임 개발에 있어 매우 중요한 부분입니다. 이에 따라 Unity는 데이터를 단순하고 직관적으로 저장할 수 있는 방법을 제공하는데, 그것이 바로 `PlayerPrefs`입니다.

이번 포스팅에서는 `PlayerPrefs`의 **기초 개념부터 활용법 및 사용 용도**까지 자세히 다루어 보겠습니다.

---
## Step 1. PlayerPrefs란 무엇인가?

`PlayerPrefs`는 Unity3D에서 제공하는 **클래스** 중 하나로, **게임 데이터를 <u>로컬</u>에 간단히 저장하고 불러올 수 있게 해줍니다.** 
주로 **설정값이나 간단한 게임 진행도, 사용자 데이터 등**을 저장하는 데 사용됩니다. 
PlayerPrefs는 **키-값 쌍(Key-Value pairs) 형태**로 데이터를 저장하며, 세 가지 타입의 데이터를 지원합니다: `int`, `float`, `string`.

### 1.1 기초 메서드

- **저장하기**
   ```csharp
   PlayerPrefs.SetInt("PlayerScore", 100); // 정수형 데이터 저장
   PlayerPrefs.SetFloat("PlayerHealth", 95.5f); // 실수형 데이터 저장
   PlayerPrefs.SetString("PlayerName", "UnityPlayer"); // 문자열 데이터 저장
   ```

- **불러오기**
   ```csharp
   int score = PlayerPrefs.GetInt("PlayerScore");
   float health = PlayerPrefs.GetFloat("PlayerHealth");
   string playerName = PlayerPrefs.GetString("PlayerName");
   ```

- **데이터 삭제**
   ```csharp
   PlayerPrefs.DeleteKey("PlayerScore"); // 특정 키 데이터 삭제
   PlayerPrefs.DeleteAll(); // 모든 데이터 삭제
   ```

---
## Step 2. 게임에서의 PlayerPrefs 활용법

PlayerPrefs는 비휘발성 데이터를 저장하는 데 매우 유용합니다. 여기 세 가지 시나리오에서의 PlayerPrefs 활용법을 소개합니다.

### 2.1 게임 설정 저장

게임 설정은 사용자가 게임을 플레이하는 데 중요한 요소이며, 이를 PlayerPrefs를 사용해 간단히 저장할 수 있습니다.

```csharp
// 게임 설정 저장 예제
void SaveGameSettings()
{
    PlayerPrefs.SetFloat("MusicVolume", 0.75f);
    PlayerPrefs.SetInt("GraphicsQuality", 3);
    PlayerPrefs.SetString("Language", "English");

    PlayerPrefs.Save(); // 현재 모든 변경 사항을 저장
}

// 게임 설정 불러오기 예제
void LoadGameSettings()
{
    float musicVolume = PlayerPrefs.GetFloat("MusicVolume", 1.0f); // 디폴트 값 설정 가능
    int graphicsQuality = PlayerPrefs.GetInt("GraphicsQuality", 2); // 디폴트 값 설정 가능
    string language = PlayerPrefs.GetString("Language", "English"); // 디폴트 값 설정 가능

    // 불러온 값을 실제 설정에 반영
    SetMusicVolume(musicVolume);
    SetGraphicsQuality(graphicsQuality);
    SetLanguage(language);
}
```

### 2.2 유저 정보 저장

PlayerPrefs를 이용해 게임 진행 상황이나 유저 정보를 저장할 수도 있습니다.

```csharp
// 유저 정보 저장 예제
void SaveUserInfo()
{
    PlayerPrefs.SetString("UserName", "Player123");
    PlayerPrefs.SetInt("UserLevel", 10);
    PlayerPrefs.SetFloat("UserExperience", 1500.0f);

    PlayerPrefs.Save();
}

// 유저 정보 불러오기 예제
void LoadUserInfo()
{
    string userName = PlayerPrefs.GetString("UserName", "Guest");
    int userLevel = PlayerPrefs.GetInt("UserLevel", 1);
    float userExperience = PlayerPrefs.GetFloat("UserExperience", 0.0f);

    // 불러온 유저 정보를 반영
    DisplayUserName(userName);
    UpdateUserLevel(userLevel);
    UpdateUserExperience(userExperience);
}
```

### 2.3 게임 진행도 저장

```csharp
// 게임 진행도 저장 예제
void SaveGameProgress()
{
    PlayerPrefs.SetInt("CurrentLevel", 5);
    PlayerPrefs.SetInt("PlayerLives", 3);
    PlayerPrefs.SetFloat("PlayerScore", 12345.67f);

    PlayerPrefs.Save();
}

// 게임 진행도 불러오기 예제
void LoadGameProgress()
{
    int currentLevel = PlayerPrefs.GetInt("CurrentLevel", 1);
    int playerLives = PlayerPrefs.GetInt("PlayerLives", 5);
    float playerScore = PlayerPrefs.GetFloat("PlayerScore", 0.0f);

    // 불러온 게임 진행도를 반영
    LoadLevel(currentLevel);
    SetPlayerLives(playerLives);
    UpdatePlayerScore(playerScore);
}
```

---
## Step 3. PlayerPrefs의 사용 용도 

PlayerPrefs는 `가벼운 데이터 저장`에 매우 적합합니다. 
하지만 **대량의 데이터**나 `민감한 데이터(현금성 아이템 등)`를 저장하는 데는 적합하지 않습니다. 
혹시나 매우 큰 데이터를 저장해야 하는 경우에는 다른 저장 방식을 고려하는 것이 좋습니다. 

예를 들어, `File`, `XML`, `JSON` 혹은 데이터베이스를 사용할 수 있습니다.

### 3.1 **활용할 수 있는 주요 시점**
- **게임 오프닝 시**: 사용자 설정을 가져오는 순간
- **게임 종료 시**: 현재 게임 상태를 저장하는 순간
- **레벨 변경 시**: 진행 상태를 저장하거나 불러올 때    

예시일뿐 꼭 이때만 활용할 수 있는 것은 아닙니다.

**너무 자주 저장할 경우 게임에 부하가 많이 올수도 있고, 너무 적은 횟수로 저장한다면 플레이어가 쌓아왔던 경험치나 아이템 등이 한번에 날아가 버릴 수 있으니 주의해야합니다.   
<u>따라서 적당한 주기와 타이밍을 찾아 저장해야합니다.</u>**

> *<u>저장 시기를 약관에 명시하여 플레이어의 동의를 받는 방법도 있습니다.</u>*


---
## Step 4. PlayerPrefs 데이터 저장 경로

PlayerPrefs로 저장된 데이터는 각 플랫폼에 따라 다른 경로에 저장됩니다. 이는 각 플랫폼에서 제공하는 로컬 저장소를 사용하기 때문입니다.

- **Windows**: `레지스트리 편집기 -> HKEY_CURRENT_USER\Software\Unity\UnityEditor\[CompanyName]\[ProductName]` **레지스트리** 경로에 저장됩니다.
- **macOS**: `~/Library/Preferences/[CompanyName]/[ProductName].plist` 경로에 저장됩니다.
- **iOS**: `~/Library/Preferences/[CompanyName]/[ProductName].plist` 경로에 저장됩니다.
- **Android**: `SharedPreferences`를 통해 **내부 저장소**에 저장됩니다.

**플랫폼별로 경로가 다르기 때문에 디버깅 시 해당 경로에서 데이터를 확인할 수 있습니다.**

**※주의※**    
**ProductName**이 같으면 **같은 PlayerPrefs 데이터**가 사용됩니다.   
예를 들어, 동일 PC에서 ProductName이 같은 프로젝트가 2개 있다면 이 둘은 같은 PlayerPrefs 데이터를 공유합니다.



---
## Step 5. 마무리 요약 
`PlayerPrefs`는 데이터를 직관적으로 저장하고 불러올 수 있는 매우 유용한 기능입니다. 
데이터의 **복잡성이나 양이 작은 경우**, 빠르고 쉽게 적용할 수 있습니다. 
**간단한 설정**부터 **사용자 정보**까지 다양한 데이터를 간편하게 저장하고 불러올 수 있기 때문에, 게임 개발 시 유용하게 활용할 수 있습니다. 
데이터를 저장하고 불러오는 기본적인 방법을 확실하게 이해하고 있는 것은 중요하며, 이를 통해 더 복잡한 데이터 관리에도 성공적으로 대응할 수 있을 것입니다.

이상으로 **PlayerPrefs를 활용한 게임 데이터 관리**에 관한 포스팅을 마치겠습니다.    
감사합니다.