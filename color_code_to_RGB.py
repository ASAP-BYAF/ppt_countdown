from pptx.dml.color import RGBColor
    
def color_code_to_RGB_func(color):

    #
    R = int(color[1:3], 16)
    G = int(color[3:5], 16)
    B = int(color[5:7], 16)
    # return RGBColor(R, G, B)
    return {'r': R, 'g': G, 'b': B}
