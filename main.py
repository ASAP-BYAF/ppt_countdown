import os
import pptx
import pathlib
from pptx.dml.color import RGBColor
import sys
import time

from add_new_slide import add_new_slide_func 
from add_count import add_count_func
from calc_delta_days import calc_delta_days_func
from add_box import add_box_func
from add_date import add_date_func
from add_days import add_days_func
from color_code_to_RGB import color_code_to_RGB_func

### Input
date_st = '2023-08-09'
date_ed = '2024-03-31'
bg_color = '#00ff00'
text_color = '#00ffff'

prs = pptx.Presentation()
delta_days = calc_delta_days_func(date_st, date_ed)
date_now = date_st

# カラーコードを RGBColor オブジェクトに変換
bg_rgb = color_code_to_RGB_func(bg_color)
text_rgb = color_code_to_RGB_func(text_color)

for i in range(delta_days, -1, -1):
    # 新しいスライドを末尾に追加
    add_new_slide_func(prs) 
    last_sld = prs.slides[-1]

    # 背景色を設定
    # (直接背景色の設定は難しそうなので大きめの色付きテキストボックスを配置
    #　そのせいで少しスライドが大きく見える。スライドショーにすれば文字は真ん中に来る。)
    add_box_func(last_sld, bg_RGB=RGBColor(bg_rgb['r'], bg_rgb['g'], bg_rgb['b']))

    # 最後のスライドに残り日数を追加
    add_count_func(last_sld, str(i), text_RGB=RGBColor(text_rgb['r'], text_rgb['g'], text_rgb['b']))
    
    # 最後のスライドに日付を追加
    add_date_func(last_sld, date_now, text_RGB=RGBColor(text_rgb['r'], text_rgb['g'], text_rgb['b']))

    # 日付を更新
    date_now = add_days_func(date_now) 

outputdir = 'random'
if not os.path.isdir(outputdir):
    pathlib.Path(outputdir).mkdir()

ppt_outputfile = os.path.join(outputdir, str(time.time())+'.pptx')
prs.save(ppt_outputfile)