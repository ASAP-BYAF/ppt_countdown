from pptx.util import Pt
from pptx.dml.color import RGBColor

from add_box import add_box_func 

def add_count_func(sld, count, text_RGB):

    sld = add_box_func(sld, fontsize=Pt(300), text=count, text_RGB=text_RGB, lm=Pt(100), tm=Pt(250), h=Pt(50), w=Pt(500) )
    sld = add_box_func(sld, fontsize=Pt(50), text="卒業まであと", text_RGB=text_RGB, lm=Pt(10), tm=Pt(100), h=Pt(50), w=Pt(300) )
    sld = add_box_func(sld, fontsize=Pt(100), text="日", text_RGB=text_RGB, lm=Pt(380), tm=Pt(310), h=Pt(50), w=Pt(500) )
