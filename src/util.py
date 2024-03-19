# File util.py
from collections import namedtuple
import matplotlib.pyplot as plt

Point = namedtuple('Point', ['x', 'y'])

# mengembalikan titik tengah dari dua buah titik
def create_mid_point(point1, point2):
    createdPoint = Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)
    return createdPoint

# menampilkan 2 set titik dengan setiap titik yang bersebalahan dihubungkan dengan garis
def display_2sets_dots_and_line(points_1, points_2,exec_time):
    # variable for centering text
    max_x = "sapi"
    min_x = "sapi"
    max_y = "sapi"

    for i in range(len(points_1)-1) :
        plt.plot(points_1[i].x,points_1[i].y,'ro',markersize = 4, alpha=0.8)
        plt.plot([points_1[i].x, points_1[i+1].x],[points_1[i].y, points_1[i+1].y],color = 'black',linewidth=1)
        if (max_x == "sapi" or max_x<points_1[i].x):
            max_x = points_1[i].x
        if (min_x == "sapi" or min_x>points_1[i].x):
            min_x = points_1[i].x
        if(max_y == "sapi" or max_y<points_1[i].y):
            max_y = points_1[i].y
    plt.plot(points_1[len(points_1)-1].x,points_1[len(points_1)-1].y,'ro',markersize = 4, alpha=0.8)
    if (max_x == "sapi" or max_x<points_1[len(points_1)-1].x):
        max_x = points_1[len(points_1)-1].x
    if (min_x == "sapi" or min_x>points_1[len(points_1)-1].x):
        min_x = points_1[len(points_1)-1].x
    if(max_y == "sapi" or max_y<points_1[len(points_1)-1].y):
        max_y = points_1[len(points_1)-1].y

    for i in range(len(points_2)-1) :
        plt.plot(points_2[i].x,points_2[i].y,'bo',markersize = 4, alpha=0.8)
        plt.plot([points_2[i].x, points_2[i+1].x],[points_2[i].y, points_2[i+1].y],color = 'blue',linewidth=1)
        if (max_x == "sapi" or max_x<points_2[i].x):
            max_x = points_2[i].x
        if (min_x == "sapi" or min_x>points_2[i].x):
            min_x = points_2[i].x
        if(max_y == "sapi" or max_y<points_2[i].y):
            max_y = points_2[i].y
    plt.plot(points_2[len(points_2)-1].x,points_2[len(points_2)-1].y,'bo',markersize = 4, alpha=0.8)
    if (max_x == "sapi" or max_x<points_2[len(points_2)-1].x):
        max_x = points_2[len(points_2)-1].x
    if (min_x == "sapi" or min_x>points_2[len(points_2)-1].x):
        min_x = points_2[len(points_2)-1].x
    if(max_y == "sapi" or max_y<points_2[len(points_2)-1].y):
        max_y = points_2[len(points_2)-1].y
    mid_x = (max_x + min_x) / 2
    plt.text(mid_x, max_y*1.01, f'Execution Time {exec_time} millisecond(s)', ha='center')
    plt.show()