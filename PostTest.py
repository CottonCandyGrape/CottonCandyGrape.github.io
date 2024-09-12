import os
from openai import OpenAI

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_completion(prompt, model="gpt-4o-mini"):
#def get_completion(prompt, model="gpt-3.5-turbo"):
    messages=[
        #{"role": "system", "content": "You are a Unity3D master game programmer and tech blogger"},
        {"role": "system", "content": "너는 건강 및 식품영양 전문가야."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1,
    )
    return response.choices[0].message.content

def generatePostFile(prompt, postDate, postTitle):
    postPath = "C:/Users/jeongho/Documents/GitHub/CottonCandyGrape.github.io/_posts/"
    response = get_completion(prompt)
    
    postDate += "-"
    postTitle += ".md"
    
    fileName = postPath + postDate + postTitle
    
    file = open(fileName, 'w')
    file.write(response)
    file.close()

print(get_completion("'배로 만든 건강 음료의 효능.'을 제목으로 포스팅해줘. 글은 [글 소개 - (소제목-설명)*반복]의 구조로 작성해줘. 대략 3000자 정도 써줘. 중요한 부분은 볼드체 처리해줘."))
