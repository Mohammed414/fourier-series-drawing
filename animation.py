
import matplotlib.pyplot as plt # for plotting and creating figures
import numpy as np # for easy and fast number calculation
from math import tau # tau is constant number = 2*PI
from scipy.integrate import quad_vec # for calculating definite integral 
from tqdm import tqdm # for progress bar
import matplotlib.animation as animation # for compiling animation and exporting video 
coeffs = np.array([(-0.0219+0.1375j), (0.137-0.1312j), (-0.0642+0.0069j), (-0.0742+0.0116j), (0.1529+0.0971j), (-0.1433-0.1234j), (-0.0532-0.0756j), (0.0197+0.043j), (0.1503-0.2345j), (-0.0209+0.0712j), (-0.0607+0.0778j), (0.1221-0.0306j), (-0.1777-0.1244j), (0.0192-0.082j), (0.0438+0.0595j), (-0.021-0.1805j), (-0.0262-0.0134j), (-0.0943-0.0843j), (0.1801-0.1151j), (-0.0928-0.0811j), (-0.0613-0.1081j), (0.0265+0.0124j), (0.0227-0.279j), (0.0888-0.0625j), (-0.1079+0.0416j), (-0.0016-0.0763j), (-0.2166-0.213j), (-0.1768-0.3879j), (0.2598-0.087j), (0.2458-0.3806j), (-0.0698-0.0655j), (-0.0894+0.2427j), (0.1584-0.3942j), (-0.3616-0.1259j), (-0.0029+0.0722j), (0.0799-0.5091j), (-0.5653-0.628j), (0.3805-0.2802j), (0.5891-0.3947j), (0.2242+0.3023j), (0.4302+0.8067j), (-0.2179-0.674j), (-1.1604-0.772j), (-0.2624+1.5987j), (3.0189+3.3374j), (0.7004-0.0446j), (-10.1098-1.6177j), (-9.4655+6.1871j), (10.7287+8.3098j), (22.6236+9.0628j), (6.796+22.4139j), (25.6427+43.1874j), (-28.3797+21.4504j), (15.4239+4.5984j), (-7.2867+6.807j), (-1.5612+3.7944j), (-0.0007-2.5851j), (-0.7067-0.1317j), (2.1045+1.4815j), (1.1706+1.1701j), (-0.5368+1.8912j), (-0.2344+1.1133j), (-0.5948-0.0014j), (-0.0411+0.2129j), (0.1823+0.4076j), (-0.1252+0.3101j), (0.0615+0.3878j), (-0.0208-0.0086j), (0.0954+0.1809j), (-0.0033+0.3713j), (0.0324+0.1315j), (-0.0783+0.1733j), (-0.0818+0.0052j), (0.2097+0.2065j), (-0.0174+0.0695j), (-0.1607+0.0938j), (-0.1142+0.2291j), (0.1163-0.282j), (0.0108-0.0262j), (0.0525+0.1667j), (0.2541+0.0777j), (-0.2161+0.0379j), (-0.035+0.0581j), (0.0612+0.1017j), (-0.0188-0.1685j), (-0.0213+0.0501j), (-0.0736+0.0112j), (0.2002-0.0758j), (-0.0199+0.0032j), (0.0107+0.0294j), (0.0618+0.1728j), (-0.0877-0.1597j), (-0.0003-0.0235j), (-0.0224+0.0534j), (0.1961-0.061j), (-0.0821+0.0481j), (-0.093-0.036j), (0.0978+0.0695j), (-0.0238-0.174j), (0.0382-0.0106j), (-0.0219+0.1375j)])
#coeffs = np.array([(-0.5171+0.197j), (-0.2278-0.249j), (-0.0524-0.6483j), (0.5952+0.1051j), (0.5139+0.1426j), (0.2265+0.303j), (-0.1425+0.5682j), (0.1286+0.3182j), (0.0487+0.4801j), (-0.6758-0.0649j), (-0.6782-0.0024j), (-0.1807-0.4019j), (0.3698-0.5563j), (0.4508-0.0069j), (0.2783+0.3323j), (0.053+0.3476j), (-0.2326+0.5213j), (-0.109+0.711j), (-0.4553+0.6555j), (-0.8893+0.0776j), (-0.6486+0.2377j), (-0.2774+0.1362j), (0.8516+0.0934j), (0.3798+0.2634j), (-0.5825+0.6837j), (0.6644+1.0778j), (-1.0382+1.3043j), (-0.8274+0.6746j), (-0.4915+0.7715j), (-1.7829-1.2381j), (0.2755-0.852j), (0.126-0.2327j), (0.8708+0.3634j), (0.4279-0.1971j), (-0.9471+1.7205j), (0.1686+2.3398j), (-0.854+1.7353j), (-1.2941+2.4496j), (-2.0745-1.4796j), (0.6703-1.9697j), (2.3567+6.3588j), (0.0937+3.6946j), (-2.2568+9.135j), (-7.9611-1.2046j), (-2.4338+0.4509j), (3.3343+4.0874j), (-5.7688+14.4389j), (-27.4007-3.7234j), (17.4915-4.0425j), (-13.5136+7.1581j), (-47.8868+21.0996j), (-22.5774-3.5523j), (-33.0298+16.6604j), (17.4105+16.2347j), (12.0961-10.1511j), (5.3224+1.2689j), (10.0583-2.5945j), (7.7793-0.5138j), (1.5261+2.2844j), (-1.3256+1.1916j), (3.5641+1.9894j), (-1.7821+1.5946j), (3.1157-1.0937j), (-3.5088-1.2487j), (-0.0597-0.1603j), (2.7985-1.1304j), (2.5713+0.3701j), (2.8612-1.3797j), (-0.3135+0.3139j), (0.1401+0.7139j), (1.2492+0.1038j), (-0.0109-0.0166j), (0.647-0.5965j), (-0.0553-1.1501j), (0.8486-1.1618j), (1.2204-1.1234j), (0.5745-0.0991j), (0.628+0.5199j), (0.0641+0.1417j), (-0.0668+0.362j), (0.1781+0.3063j), (-0.3006-0.51j), (-0.3547-0.2335j), (0.178-0.7527j), (0.9937-0.5942j), (0.5132-0.058j), (0.6281+0.4125j), (0.5567+0.5681j), (0.2699-0.1621j), (-0.0776+0.305j), (-0.1356+0.2288j), (-0.1562-0.6076j), (-0.454-0.5359j), (0.5795-0.461j), (0.7488-0.2851j), (0.2058+0.0125j), (0.2091+0.507j), (0.0163+0.2742j), (0.2143+0.248j), (-0.5038+0.2107j), (-0.5171+0.197j)])
#coeffs = np.array([(-1.0296+1.0038j), (-0.7521-0.411j), (-0.1357-0.3383j), (1.2128-0.6023j), (0.4503+1.2252j), (-1.5087+0.7122j), (-0.6606+0.5446j), (-0.8355+0.5716j), (-1.2151-0.6553j), (-0.5624+0.6825j), (-2.0157-0.3293j), (-0.3574-0.5677j), (-0.9421-0.8764j), (-0.5147-1.6187j), (-0.0328-1.8278j), (0.1175-0.5146j), (1.4579-0.2472j), (0.9495+0.5968j), (0.996+1.0956j), (-1.2561+2.5458j), (-1.5834+1.1691j), (-3.4783-2.1816j), (-1.0691-4.299j), (1.4007-0.3448j), (0.0629+0.5826j), (0.2777-0.1119j), (-0.1555+0.4935j), (1.4929-0.2457j), (1.2206+1.9919j), (-4.131+2.5818j), (-1.5561+1.3117j), (-2.5545+1.734j), (-6.7847-0.0576j), (-4.1046-1.0888j), (0.0983+1.2506j), (0.5327-3.013j), (-2.0685+3.1095j), (-1.0567-9.7294j), (4.1996+2.2239j), (-0.0834+4.858j), (-6.4892+4.5395j), (-1.2912+10.7863j), (1.4042-1.6719j), (-5.0201+0.6089j), (2.0729-6.1076j), (-5.1689-6.4642j), (-13.6472+20.9034j), (-5.4569+4.6714j), (-11.1761+3.991j), (11.8603-14.5113j), (-35.0374+16.4351j), (-19.1673-6.3105j), (2.7963+8.5157j), (4.1485-2.576j), (-1.0152-12.128j), (0.1348+17.5515j), (16.6979+7.7559j), (6.2132+1.2135j), (6.1503-5.0002j), (3.3843+2.6388j), (4.8019-10.7661j), (2.4741-4.5542j), (7.7665-3.2081j), (3.5013+0.4403j), (-0.2278+4.6172j), (-0.3848+3.7355j), (-1.8069-1.2118j), (-1.0785-0.27j), (0.0905-0.1831j), (1.9587-2.2953j), (-0.5821-1.4802j), (0.2882-0.1362j), (2.5231-2.7216j), (4.5985+0.8816j), (-0.0169-1.0256j), (1.5879+1.0486j), (1.5497+0.7355j), (2.7677+1.0307j), (-0.3069+1.8846j), (-1.5476+0.9069j), (-1.5299-2.3962j), (-0.138-2.6775j), (2.768-0.6709j), (1.9736-1.2234j), (0.8311-0.756j), (1.0249+0.4171j), (1.5736+1.3783j), (1.1262+0.1332j), (1.1486+0.9915j), (-0.087+1.1528j), (-0.6943+1.6779j), (-1.2131+0.3296j), (-0.6798+0.1011j), (-0.8476-0.392j), (0.3884-1.2371j), (-0.1326-0.6488j), (0.7807-0.0125j), (1.9921+0.7874j), (-0.0425+0.6957j), (-0.793+0.3715j), (-1.0296+1.0038j)])
# later we will need these data to fix the size of figure
xlim_data = (-2, 2) 
ylim_data = (-2, 2)

plt.show()

# Now find forier coefficient from -n to n circles
# ..., c-3, c-2, c-1, c0, c1, c2, c3, ...
order = 50 # -order to order i.e -100 to 100
# you can change the order to get proper figure
# too much is also not good, and too less will not produce good result


# converting list into numpy array
c = np.array(coeffs)

# save the coefficients for later use
np.save("coeff.npy", c)

## -- now to make animation with epicycle -- ##

# this is to store the points of last circle of epicycle which draws the required figure
draw_x, draw_y = [], []

# make figure for animation
fig, ax = plt.subplots()
ax.set_facecolor('xkcd:salmon')
ax.set_facecolor((1.0, 0.47, 0.42))

# different plots to make epicycle
# there are -order to order numbers of circles
circles = [ax.plot([], [], 'w-')[0] for i in range(-order, order+1)]

# circle_lines are radius of each circles
circle_lines = [ax.plot([], [], 'b-')[0] for i in range(-order, order+1)]
# drawing is plot of final drawing
drawing, = ax.plot([], [], 'k-', linewidth=2)

# original drawing
orig_drawing, = ax.plot([], [], 'g-', linewidth=0.5)

# to fix the size of figure so that the figure does not get cropped/trimmed
ax.set_xlim(xlim_data[0]-150, xlim_data[1]+150)
ax.set_ylim(ylim_data[0]-150, ylim_data[1]+150)

# hide axes
ax.set_axis_off()

# to have symmetric axes
ax.set_aspect('equal')

# Set up formatting for the video file
Writer = animation.writers['ffmpeg']

fps_num = 60

writer = Writer(fps=fps_num, metadata=dict(artist='Amrit Aryal'), bitrate=1800)

print("compiling animation ...")
# set number of frames
frames = 600
pbar = tqdm(total=frames)

# save the coefficients in order 0, 1, -1, 2, -2, ...
# it is necessary to make epicycles
def sort_coeff(coeffs):
    new_coeffs = []
    new_coeffs.append(coeffs[order])
    for i in range(1, order+1):
        new_coeffs.extend([coeffs[order+i],coeffs[order-i]])
    return np.array(new_coeffs)

# make frame at time t
# t goes from 0 to 2*PI for complete cycle
def make_frame(i, time, coeffs):
    global pbar
    # get t from time
    t = time[i]

    # exponential term to be multiplied with coefficient 
    # this is responsible for making rotation of circle
    exp_term = np.array([np.exp(n*t*1j) for n in range(-order, order+1)])

    # sort the terms of fourier expression
    coeffs = sort_coeff(coeffs*exp_term) # coeffs*exp_term makes the circle rotate. 
    # coeffs itself gives only direction and size of circle

    # split into x and y coefficients
    x_coeffs = np.real(coeffs)
    y_coeffs = np.imag(coeffs)

    # center points for fisrt circle
    center_x, center_y = 0, 0

    # make all circles i.e epicycle
    for i, (x_coeff, y_coeff) in enumerate(zip(x_coeffs, y_coeffs)):
        # calculate radius of current circle
        r = np.linalg.norm([x_coeff, y_coeff]) # similar to magnitude: sqrt(x^2+y^2)

        # draw circle with given radius at given center points of circle
        # circumference points: x = center_x + r * cos(theta), y = center_y + r * sin(theta)
        theta = np.linspace(0, tau, num=50) # theta should go from 0 to 2*PI to get all points of circle
        x, y = center_x + r * np.cos(theta), center_y + r * np.sin(theta)
        circles[i].set_data(x, y)

        # draw a line to indicate the direction of circle
        x, y = [center_x, center_x + x_coeff], [center_y, center_y + y_coeff]
        circle_lines[i].set_data(x, y)

        # calculate center for next circle
        center_x, center_y = center_x + x_coeff, center_y + y_coeff
    
    # center points now are points from last circle
    # these points are used as drawing points
    draw_x.append(center_x)
    draw_y.append(center_y)

    # draw the curve from last point
    drawing.set_data(draw_x, draw_y)

    # # draw the real curve
    # orig_drawing.set_data([*range(-10, 10)], [*range(-10, 10)])

    # update progress bar
    pbar.update(1)

# make animation
# time is array from 0 to tau 
time = np.linspace(0, tau, num=frames)
anim = animation.FuncAnimation(fig, make_frame, frames=frames, fargs=(time, c),interval=5)
anim.save('epicycle'+str(fps_num)+'fps.mp4', writer=writer, dpi=300)
pbar.close()
print("completed: epicycle.mp4")