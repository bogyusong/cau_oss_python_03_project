# %%
"""
?ŒŒ?¼ê³? ê´?? ¨?œ ?•¨?ˆ˜ë¥? êµ¬í˜„?•´?†“??? ëª¨ë“ˆ
"""

import chardet
import os
import sys

def print_listdir(path='./', depth=0):
    """
    path ê²½ë¡œë¶??„° ì¡´ì¬?•˜?Š” ëª¨ë“  ?•˜?œ„ ?´?”/?ŒŒ?¼?˜ ëª©ë¡?„ ì¶œë ¥?•˜?Š” ?•¨?ˆ˜
    Args:
        path  (string): ì¶œë ¥?•˜ê³ ì ?•˜?Š” ê²½ë¡œ?˜ ?‹œ?‘ ?œ„ì¹?
        depth (int)   : ?ŒŒ?¼?˜ ?‹¨ê³? (?‚¬?š©?‹œ 0?œ¼ë¡? ê³ ì •)
    Examples:
        >>> print_listdir('../') # ?ƒ?œ„ ?´?”ë¶??„° ì¡´ì¬?•˜?Š” ëª¨ë“  ?´?”/?ŒŒ?¼?˜ ëª©ë¡?„ ì¶œë ¥
    """
    # ?‹œ?‘?˜ depth?Š” 0?œ¼ë¡? ê³ ì •
    if sys._getframe(1).f_code.co_name != 'print_listdir': depth=0

    # ?ŒŒ?¼?˜ ëª©ë¡
    dirs = os.listdir(path)
    for d in dirs:
        # depthê°? 1?´?ƒ?¼ ê²½ìš° depthë§Œí¼ ?“¤?—¬?“°ê¸?
        if depth > 0 :
            for _ in range(depth):
                print('  ', end='')
            print('|-', end='')
        print(f'[{d}]')
        d = path + '/' + d
        # ?´?”?¼ ê²½ìš° ?¬ê·??˜¸ì¶œë¡œ ?•˜?œ„ ëª©ë¡ ì¶œë ¥
        if os.path.isdir(d):
            print_listdir(d, depth+1)

def read_file(path):
    """
    ?ŒŒ?¼?˜ ì²«ë²ˆì§? ì¤„ì„ ?½?–´ ?¸ì½”ë”©?„ ?™•?¸?•œ ?’¤,
    ?¸ì½”ë”©?— ë§ê²Œ ?ŒŒ?¼?„ ?½?–´ ë¦¬ìŠ¤?Š¸ë¡? ë°˜í™˜?•˜?Š” ?•¨?ˆ˜
    Args:
        path (string): ?ŒŒ?¼ ê²½ë¡œ
    Returns:
        list of string: ?¼?¸(\n)?‹¨?œ„ë¡? ë¶„ë¦¬?œ ë¬¸ì?—´
    Examples:
        >>> list_str = read_file('./input.txt')
    """
    # encoding ?™•?¸
    enc = 'utf-8'
    with open(path, 'rb') as f:
        tmp = f.readline()
        enc = chardet.detect(tmp)['encoding']

    # file ê°ì²´ ?ƒ?„±
    list_str = list()
    with open(file=path, mode='r', encoding=enc) as f:
        for line in f:
            list_str.append(line.strip())   # ê³µë°±(\n) ? œê±°í•˜?—¬ ë¦¬ìŠ¤?Š¸?— ì¶”ê??
    del list_str[0]

    return list_str


if __name__ == '__main__':
    # ê²½ë¡œ?˜ ?ŒŒ?¼/?´?” ëª©ë¡ ì¶œë ¥
    print_listdir('./')
    
    # ?ŒŒ?¼ ?—´ê¸?
    strs = read_file("./input/free_parking_spot_seoul.csv")

    # ì¶œë ¥
    for s in strs:
        print(s)