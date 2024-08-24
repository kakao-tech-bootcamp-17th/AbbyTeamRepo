'''
1. 소문자 변환
2. re 문장부호 제거
3. spellchecker 철자오류 교정
4. konlpy 불용어 제거
'''
import re
from hanspell import spell_checker
from konlpy.tag import Okt
okt = Okt()

# 파일 불러오기
text_li = []
f = open('./raw_data.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()   # 줄바꿈(\n) 문자를 제거
    text_li.append(line)
f.close()

# 불용어 리스트 만들기
stop_words = []
f = open('./stopwords.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()   # 줄바꿈(\n) 문자를 제거
    stop_words.append(line)
f.close()

# 클리닝 과정 순차적으로 진행하고 새로운 리스트에 넣기
text_cleaned = []
for text in text_li:
    # 1. 소문자 변환
    text = text.lower()
    # 2. re 문장부호 제거
    text = re.sub(r'[^\w\s]', '', text)
    # 3. spellchecker 철자오류 교정
    result = spell_checker.check(text)
    if result.checked:
        text = result.checked
    else:
        text = result.original
    # 4. konlpy 불용어 제거
    word_tokens = okt.morphs(text)
    text = [word for word in word_tokens if not word in stop_words]
    text = ' '.join(text)
    text_cleaned.append(text)

# 클리닝 된 텍스트 데이터를 cleaned_data.txt 파일로 저장하기
f = open('./cleaned_data.txt', 'w')
for text in text_cleaned:
    f.write(text+'\n')
f.close()