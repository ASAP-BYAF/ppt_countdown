from pptx.util import Pt

from add_box import add_box_func 

def add_count_func(sld, count):

    sld = add_box_func(sld, fontsize=Pt(200), text=count, lm=Pt(100), tm=Pt(200), h=Pt(50), w=Pt(500) )
    sld = add_box_func(sld, fontsize=Pt(50), text="卒業まであと", lm=Pt(10), tm=Pt(100), h=Pt(50), w=Pt(300) )
    sld = add_box_func(sld, fontsize=Pt(100), text="日", lm=Pt(300), tm=Pt(250), h=Pt(50), w=Pt(500) )
