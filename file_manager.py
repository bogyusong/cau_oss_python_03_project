# %%
"""
?��?���? �??��?�� ?��?���? 구현?��?��??? 모듈
"""

import chardet
import os
import sys

def print_listdir(path='./', depth=0):
    """
    path 경로�??�� 존재?��?�� 모든 ?��?�� ?��?��/?��?��?�� 목록?�� 출력?��?�� ?��?��
    Args:
        path  (string): 출력?��고자 ?��?�� 경로?�� ?��?�� ?���?
        depth (int)   : ?��?��?�� ?���? (?��?��?�� 0?���? 고정)
    Examples:
        >>> print_listdir('../') # ?��?�� ?��?���??�� 존재?��?�� 모든 ?��?��/?��?��?�� 목록?�� 출력
    """
    # ?��?��?�� depth?�� 0?���? 고정
    if sys._getframe(1).f_code.co_name != 'print_listdir': depth=0

    # ?��?��?�� 목록
    dirs = os.listdir(path)
    for d in dirs:
        # depth�? 1?��?��?�� 경우 depth만큼 ?��?��?���?
        if depth > 0 :
            for _ in range(depth):
                print('  ', end='')
            print('|-', end='')
        print(f'[{d}]')
        d = path + '/' + d
        # ?��?��?�� 경우 ?���??��출로 ?��?�� 목록 출력
        if os.path.isdir(d):
            print_listdir(d, depth+1)

def read_file(path):
    """
    ?��?��?�� 첫번�? 줄을 ?��?�� ?��코딩?�� ?��?��?�� ?��,
    ?��코딩?�� 맞게 ?��?��?�� ?��?�� 리스?���? 반환?��?�� ?��?��
    Args:
        path (string): ?��?�� 경로
    Returns:
        list of string: ?��?��(\n)?��?���? 분리?�� 문자?��
    Examples:
        >>> list_str = read_file('./input.txt')
    """
    # encoding ?��?��
    enc = 'utf-8'
    with open(path, 'rb') as f:
        tmp = f.readline()
        enc = chardet.detect(tmp)['encoding']

    # file 객체 ?��?��
    list_str = list()
    with open(file=path, mode='r', encoding=enc) as f:
        for line in f:
            list_str.append(line.strip())   # 공백(\n) ?��거하?�� 리스?��?�� 추�??
    del list_str[0]

    return list_str


if __name__ == '__main__':
    # 경로?�� ?��?��/?��?�� 목록 출력
    print_listdir('./')
    
    # ?��?�� ?���?
    strs = read_file("./input/free_parking_spot_seoul.csv")

    # 출력
    for s in strs:
        print(s)