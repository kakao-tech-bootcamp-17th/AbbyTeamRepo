from konlpy.tag import Komoran, Okt
kom = Komoran()
okt = Okt()

# Lemmatization 함수 정의
def lemmatize(tag):
    if tag[1] == 'VA' or tag[1] == 'VV':
        return tag[0] + '다'

# Stemming 함수 정의

# lemma list 정의
lemmas = []
# 파일 불러오기, lemmatization
f = open('./cleaned_data.txt', 'r')
lines = f.readlines()
for line in lines:
    morphtags = kom.pos(line)
    for tag in morphtags:
        lemma = lemmatize(tag)
        if lemma:
            lemmas.append(lemma)

# stemmed list 정의
stemmed = []
# stemming
for line in lines:
    line = line.strip()
    stems = okt.morphs(line,stem=True)
    if stems:
        stemmed.append(stems)

# 정규환 된 텍스트 데이터를 normalized_data.txt 파일로 저장하기
f = open('./normalized_data.txt', 'w')
for text in stemmed:
    f.write(' '.join(text)+'\n')
f.close()