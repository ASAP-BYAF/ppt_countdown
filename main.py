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

### Input
date_st = '2023-07-12'
date_ed = '2024-03-31'

prs = pptx.Presentation()
delta_days = calc_delta_days_func(date_st, date_ed)
date_now = date_st
for i in range(delta_days, -1, -1):
    # 新しいスライドを末尾に追加
    add_new_slide_func(prs) 
    last_sld = prs.slides[-1]

    # 背景色を設定(直接背景色の設定は難しそうなので大きめの色付きテキストボックスを配置)
    add_box_func(last_sld, bg_RGB=RGBColor(0, 0, 0))
    add_count_func(last_sld, str(i))
    
    # 日付を更新
    date_now = add_days_func(date_now) 
    add_date_func(last_sld, date_now)

outputdir = 'random'
if not os.path.isdir(outputdir):
    pathlib.Path(outputdir).mkdir()

ppt_outputfile = os.path.join(outputdir, str(time.time())+'.pptx')
prs.save(ppt_outputfile)