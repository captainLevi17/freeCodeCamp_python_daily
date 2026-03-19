'''
Element Size
Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.

"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.

"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.


'''

def get_element_size(window_size, element_vw, element_vh):
    w = int(window_size.split(' x ')[0])
    h = int(window_size.split(' x ')[1])
    vw = int(element_vw[:-2])
    vh = int(element_vh[:-2])
    viewport_width = (vw * w) /100
    viewport_height =(vh * h) /100

    return f"{int(viewport_width)} x {int(viewport_height)}"