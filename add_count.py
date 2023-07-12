from pptx.util import Pt

from add_box import add_box_func 

def add_count_func(sld, count):

    sld = add_box_func(sld, fontsize=Pt(300), text=count, text_color='#FFFFFF', lm=Pt(100), tm=Pt(250), h=Pt(50), w=Pt(500) )
    sld = add_box_func(sld, fontsize=Pt(50), text="卒業まであと", text_color='#FFFFFF', lm=Pt(10), tm=Pt(100), h=Pt(50), w=Pt(300) )
    sld = add_box_func(sld, fontsize=Pt(100), text="日", text_color='#FFFFFF', lm=Pt(380), tm=Pt(310), h=Pt(50), w=Pt(500) )
