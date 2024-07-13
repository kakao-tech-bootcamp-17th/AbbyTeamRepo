'''
과제 1: Collections 모듈 활용

EXAMPLE_SEQUENCE 값을 활용해보세요.

Deque: Deque를 생성하고, 요소를 추가하고 제거하는 작업을 해보세요.

Namedtuple: Namedtuple을 정의하고 인스턴스를 생성해보세요.

Defaultdict: Defaultdict를 사용해보세요. 키가 없을 때 기본값을 설정하세요.

Counter: Counter를 사용해 리스트에서 각 요소의 빈도를 세어보세요.
'''

EXAMPLE_SEQUENCE = ['dog', 'cat', 'mouse', 'parrot', 'frog']

# 1. Deque

from collections import deque
animalDQ = deque(EXAMPLE_SEQUENCE)

print(animalDQ)

animalDQ.append('abby')
print(animalDQ)

animalDQ.popleft()
print(animalDQ)


# 2. Namedtuple

from collections import namedtuple

Animal = namedtuple('Animal',['species','name'])
cat = Animal('animal','cat')
print(cat)


# 3. Defaultdict

from collections import defaultdict

dd = defaultdict(int)
dd['cat'] = 1
dd['mouse'] = 2
dd['parrot'] = 3
dd['frog'] = 4

print(dd['cat'])
print(dd['mouse'])
print(dd['parrot'])
print(dd['frog'])
print(dd['abby'])


# 4. Counter

from collections import Counter

Counter(EXAMPLE_SEQUENCE)

