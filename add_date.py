from pptx.util import Pt
from pptx.dml.color import RGBColor

from add_box import add_box_func 

def add_date_func(sld, date, text_RGB):

    y, m, d = map(int, date.split('-'))
    sld = add_box_func(sld, fontsize=Pt(50), text=f'{y}年{m}月{d}日', text_RGB=text_RGB, lm=Pt(250), tm=Pt(450), h=Pt(50), w=Pt(500) )
