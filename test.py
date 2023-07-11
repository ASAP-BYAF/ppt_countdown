import os
import pptx
import pathlib
import time

from add_new_slide import add_new_slide_func 
from add_count import add_count_func

# date_st = #カウントダウン開始日時(yyyy/mm/dd)
# date_ed = #カウントダウン終了日時(yyyy/mm/dd)
# num_of_day = calc_num_of_day_func(date_st, date_ed) # カウントダウン終了までの日数

ppt_inputfile = os.path.join('sample020.pptx')

prs = pptx.Presentation(ppt_inputfile)
for i in range(3, -1, -1):
    # date = calc_date_func() # 日付の始点と経過日数から日付を計算
    add_new_slide_func(prs)
    last_sld = prs.slides[-1]
    add_count_func(last_sld, str(i))

outputdir = 'random'
if not os.path.isdir(outputdir):
    pathlib.Path(outputdir).mkdir()

ppt_outputfile = os.path.join(outputdir, str(time.time())+'.pptx')
prs.save(ppt_outputfile)