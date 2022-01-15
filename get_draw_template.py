def get_draw_template(n):
    n_str = str(n)
    point = r"p_{"+n_str+r"}\left(t\right)=R\left["+n_str+r"\right]\left(\cos2\pi\cdot "+str(n-51)+r"\cdot t\ +\phi\left["+n_str+r"\right],\ \sin2\pi\cdot "+str(n-51)+r"\cdot t+\phi\left["+n_str+r"\right]\right)+p_{"+str(n-1)+r"}\left(t\right)"
    
    polygon = r"\operatorname{polygon}\left(p_{"+str(n-1)+r"}\left(T\right),\ p_{"+str(n)+r"}\left(T\right)\right)"
    
    return point, polygon
