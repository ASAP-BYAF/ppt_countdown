def find_grad_st_func(r,g,b):
    """r,g,b の整数値を受け取り、置換する場所、終点の値を返します。
        
    Args:
        r (int): RGB の R の値
        g (int): RGB の G の値
        b (int): RGB の B の値
    
    Returns:
        str, str, List[int]: 置換する場所は rg(R と G の値を交換) or gb or br, 
            終点の値は ２つの整数の組
        
    """

    # 最初の2を満たさないとき r == g かつ g == b ⇔ r == g == bで交換できない。
    # ゆえに b != r という分岐は必要ない。
    if r != g:
        place, final_point = 'rg', [g,r]
    elif g != b:
        place, final_point = 'gb', [b,g]
    else:
        place, final_point = None, None
    
    return place, final_point

if __name__ == '__main__':
    place, final_point = func(1,1,1)
    print(place, final_point)
    place, final_point = func(1,1,2)
    print(place, final_point)
    place, final_point = func(1,1,0)
    print(place, final_point)
    place, final_point = func(1,4,2)
    print(place, final_point)
    place, final_point = func(2,1,1)
    print(place, final_point)