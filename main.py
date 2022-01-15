from c_sub_n import get_constant
from get_draw_template import get_draw_template
from utils import get_template
def main():
    coeffs = []
    for i in range(-50, 51):
        coeffs.append(get_constant(i))
    print(coeffs)
    
if __name__ == "__main__":
    main()