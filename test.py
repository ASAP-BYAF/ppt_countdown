from find_grad_st import find_grad_st_func
from move_color import move_color_func

def test():
    r,g,b = 1,2,1
    place, final_point = find_grad_st_func(r,g,b)
    for i in range(10):
        print(i, r,g,b,place, final_point)
        r,g,b,place, final_point = move_color_func(r,g,b,place,final_point)

if __name__ == '__main__':
    test()