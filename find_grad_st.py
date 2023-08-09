def find_grad_st_func(r,g,b):
    """r,g,b の整数値を受け取り、置換する場所、向き、終点の値を返します。
        
    Args:
        r (int): RGB の R の値
        g (int): RGB の G の値
        b (int): RGB の B の値
    
    Returns:
        str, str, List[int]: 置換する場所は rg(R と G の値を交換) or gb or br, 
            向きは ud(左側の数字を up、右側の数字を down) or du
            終点の値は ２つの整数の組
        
    """

    # 最初の2を満たさないとき r == g かつ g == b ⇔ r == g == bで交換できない。
    # ゆえに b != r という分岐は必要ない。
    if r != g:
        place, direction, final_point = 'rg', 'du' if  r>g else 'ud', [g,r]
    elif g != b:
        place, direction, final_point = 'gb', 'du' if  g>b else 'ud', [b,g]
    else:
        place, direction, final_point = None, None, None
    
    return place, direction, final_point

if __name__ == '__main__':
    place, dirction, final_point = find_grad_st_func(1,1,1)
    print(place, dirction, final_point)
    place, dirction, final_point = find_grad_st_func(1,1,2)
    print(place, dirction, final_point)
    place, dirction, final_point = find_grad_st_func(1,1,0)
    print(place, dirction, final_point)
    place, dirction, final_point = find_grad_st_func(1,4,2)
    print(place, dirction, final_point)
    place, dirction, final_point = find_grad_st_func(2,1,1)
    print(place, dirction, final_point)