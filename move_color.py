import sys
from typing import Tuple, List

def inc_dec_func(left, right):
    if left > right:
        left -= 1
        right += 1
    else:
        left += 1
        right -= 1
    return left, right
            
def move_color_func(r: int,g: int,b: int,place: str,final_point: str) \
    -> Tuple[int,int,int,str,List[int]]:
    """RGB の各値と交換する場所の値を終点に向かって1ずつずらします。

    Args:
        r (int): RGB の R の値
        g (int): RGB の G の値
        b (int): RGB の B の値
    
    Returns:
        str, str, List[int]: 置換する場所は rg(R と G の値を交換) or gb or br, 
            終点の値は ２つの整数の組
    """
    # 指定された場所の値を 1 ずつずらす
    if place == 'rg':
        r,g = inc_dec_func(r,g)
        if r == final_point[0] and g == final_point[1]:
            # 終点の値と交換個所を更新
            if g != b:
                place = 'gb'
                final_point = [b,g]
            else:
                place = 'br'
                final_point = [r,b]
    elif place == 'gb':
        g,b = inc_dec_func(g,b)
        if g == final_point[0] and b == final_point[1]:
            # 終点の値と交換個所を更新
            if b != r:
                place = 'br'
                final_point = [r,b]
            else:
                place = 'rg'
                final_point = [g,b]
    elif place == 'br':
        b,r = inc_dec_func(b,r)
        if b == final_point[0] and r == final_point[1]:
            # 終点の値と交換個所を更新
            if r != g:
                place = 'rg'
                final_point = [g,r]
            else:
                place = 'gb'
                final_point = [b,g]
    else:
        print('Place is incorrect')
        sys.exit()
    return r,g,b,place,final_point
    
if __name__ == '__main__':
    # move_color_func(1,2,3,'rg', [2,1])
    # r,g,b = 1,3,2
    # place, final_point = 'rg', [3,1]
    # for i in range(10):
    #     print(i, r,g,b,place, final_point)
    #     r,g,b,place, final_point = move_color_func(r,g,b,place,final_point)
    r,g,b = 1,2,1
    place, final_point = 'rg', [2,1]
    for i in range(10):
        print(i, r,g,b,place, final_point)
        r,g,b,place, final_point = move_color_func(r,g,b,place,final_point)