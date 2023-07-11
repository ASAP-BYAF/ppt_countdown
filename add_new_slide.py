import pptx

def add_new_slide_func(prs):
    """presentation オブジェクトを受け取り、白紙のスライドを末尾に追加します。

       Args:
           prs (pptx.Presentation): pptx ファイルオブジェクト

        Returns:
            pptx.Presentatin: 受け取った pptx ファイルオブジェクトの末尾に白紙のスライドを追加したもの
    """

    new_slide = prs.slide_layouts[6]
    prs.slides.add_slide(new_slide)
