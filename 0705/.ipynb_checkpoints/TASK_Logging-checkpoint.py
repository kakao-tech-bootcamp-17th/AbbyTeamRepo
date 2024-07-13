'''
## 과제 3: Logging 활용
1. 기본 로깅 설정: 로깅을 설정하고 정보를 로깅하세요. 로그의 형태는 '시간 - 에러레벨 - 메시지' 입니다.

2. 예외 로깅: 예외가 발생했을 때 에러를 로깅하세요.
'''

# 1. 기본 로깅 설정

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

logger = logging.getLogger(__name__)


# 2. 예외 로깅

def divide(a,b):
    try:
        result = a/b
        logger.info("SUCCESS!")
        return result
    except ZeroDivisionError:
        logger.error("You cannot divide by zero.")
        return None

print(divide(10,2))
print(divide(10,0))

