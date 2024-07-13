'''
과제 2: Comprehension 활용

EXAMPLE_SEQUENCE 값을 활용해보세요.

1. 리스트 컴프리헨션: 숫자 리스트의 제곱값을 구하세요.

2. 딕셔너리 컴프리헨션: 키가 숫자이고 값이 그 숫자의 제곱인 딕셔너리를 생성하세요.

3. 집합 컴프리헨션: 중복된 값을 제거한 제곱값 집합을 생성하세요.
'''

ex= [1, 4, 12, 9, 22, 5, 1, 9]

# 1. list comprehension

ex_li = [x**2 for x in ex]
print(ex_li)


# 2. dictionary comprehension

ex_dic = {x: x**2 for x in ex}
print(ex_dic)


# 3. set comprehension

ex_set = {x**2 for x in ex}
print(ex_set)