import os
import pptx
import pathlib
import time

from add_new_slide import add_new_slide_func 
from add_count import add_count_func
from calc_delta_days import calc_delta_days_func

### Input
date_st = '2023-07-12'
date_ed = '2024-03-31'
ppt_inputfile = os.path.join('blank.pptx')

delta_days = calc_delta_days_func(date_st, date_ed)

prs = pptx.Presentation(ppt_inputfile)
for i in range(delta_days, -1, -1):
    # date = calc_date_func() # 日付の始点と経過日数から日付を計算
    add_new_slide_func(prs)
    last_sld = prs.slides[-1]
    add_count_func(last_sld, str(i))

outputdir = 'random'
if not os.path.isdir(outputdir):
    pathlib.Path(outputdir).mkdir()

ppt_outputfile = os.path.join(outputdir, str(time.time())+'.pptx')
prs.save(ppt_outputfile)