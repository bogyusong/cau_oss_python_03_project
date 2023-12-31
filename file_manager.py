# %%
"""
??Όκ³? κ΄?? ¨? ?¨?λ₯? κ΅¬ν?΄???? λͺ¨λ
"""

import chardet
import os
import sys

def print_listdir(path='./', depth=0):
    """
    path κ²½λ‘λΆ??° μ‘΄μ¬?? λͺ¨λ  ?? ?΄?/??Ό? λͺ©λ‘? μΆλ ₯?? ?¨?
    Args:
        path  (string): μΆλ ₯?κ³ μ ?? κ²½λ‘? ?? ?μΉ?
        depth (int)   : ??Ό? ?¨κ³? (?¬?©? 0?Όλ‘? κ³ μ )
    Examples:
        >>> print_listdir('../') # ?? ?΄?λΆ??° μ‘΄μ¬?? λͺ¨λ  ?΄?/??Ό? λͺ©λ‘? μΆλ ₯
    """
    # ??? depth? 0?Όλ‘? κ³ μ 
    if sys._getframe(1).f_code.co_name != 'print_listdir': depth=0

    # ??Ό? λͺ©λ‘
    dirs = os.listdir(path)
    for d in dirs:
        # depthκ°? 1?΄??Ό κ²½μ° depthλ§νΌ ?€?¬?°κΈ?
        if depth > 0 :
            for _ in range(depth):
                print('  ', end='')
            print('|-', end='')
        print(f'[{d}]')
        d = path + '/' + d
        # ?΄??Ό κ²½μ° ?¬κ·??ΈμΆλ‘ ?? λͺ©λ‘ μΆλ ₯
        if os.path.isdir(d):
            print_listdir(d, depth+1)

def read_file(path):
    """
    ??Ό? μ²«λ²μ§? μ€μ ?½?΄ ?Έμ½λ©? ??Έ? ?€,
    ?Έμ½λ©? λ§κ² ??Ό? ?½?΄ λ¦¬μ€?Έλ‘? λ°ν?? ?¨?
    Args:
        path (string): ??Ό κ²½λ‘
    Returns:
        list of string: ?Ό?Έ(\n)?¨?λ‘? λΆλ¦¬? λ¬Έμ?΄
    Examples:
        >>> list_str = read_file('./input.txt')
    """
    # encoding ??Έ
    enc = 'utf-8'
    with open(path, 'rb') as f:
        tmp = f.readline()
        enc = chardet.detect(tmp)['encoding']

    # file κ°μ²΄ ??±
    list_str = list()
    with open(file=path, mode='r', encoding=enc) as f:
        for line in f:
            list_str.append(line.strip())   # κ³΅λ°±(\n) ? κ±°ν?¬ λ¦¬μ€?Έ? μΆκ??
    del list_str[0]

    return list_str


if __name__ == '__main__':
    # κ²½λ‘? ??Ό/?΄? λͺ©λ‘ μΆλ ₯
    print_listdir('./')
    
    # ??Ό ?΄κΈ?
    strs = read_file("./input/free_parking_spot_seoul.csv")

    # μΆλ ₯
    for s in strs:
        print(s)