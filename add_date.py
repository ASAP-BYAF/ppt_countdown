from pptx.util import Pt

from add_box import add_box_func 

def add_date_func(sld, date):

    y, m, d = map(int, date.split('-'))
    sld = add_box_func(sld, fontsize=Pt(50), text=f'{y}年{m}月{d}日', lm=Pt(250), tm=Pt(450), h=Pt(50), w=Pt(500) )
