# File BezierCurve.py
from util import Point,create_mid_point,display_2sets_dots_and_line
from collections import deque

class BezierCurve():
    def __init__(self,inp_points, inp_iteration,inp_method) -> None:
        self.points = inp_points
        self.nPoints = len(self.points)
        self.iteration = inp_iteration
        self.method = inp_method
        self.bezier_points = []
        self.power_of_2 = 1
        self.pascal_triangle = []

    # membuat bezier curve dengan divide and conquer
    def dnc_populate_bezier_points(self, cur_points, iteration_count):
        if (iteration_count>0):
            left_points = [cur_points[0]]
            right_points = deque([cur_points[len(cur_points)-1]])

            # generate all mid points in 1 iteration
            n = self.nPoints
            while(n>1):
                new_points = []
                for i in range(n-1):
                    new_point = create_mid_point(cur_points[i],cur_points[i+1])
                    new_points.append(new_point)
                    if(i==0):
                        left_points.append(new_point)
                    if(i == n-2):
                        right_points.appendleft(new_point)
                cur_points = new_points
                n-=1
            # rekursi bagian kiri dan kanan
            self.dnc_populate_bezier_points(left_points, iteration_count-1)
            self.tambah_point(left_points[len(left_points)-1])
            self.dnc_populate_bezier_points(right_points, iteration_count-1)
    
    # membuat bezier curve dengan bruteforce
    def bf_populate_bezier_points(self):
        dist_per_point = 0.5/self.power_of_2
        cur_dist = dist_per_point

        # mengisi setiap titik sesuai jumlah iterasi dan jumlah titik
        while(cur_dist<1):
            tempx = 0
            tempy =0
            for i in range(self.nPoints):
                # print(f"(1-t):{(1-cur_dist)**(self.nPoints-i)}\nt:{(cur_dist)**(i)}")
                tempx += self.pascal_triangle[self.nPoints][i+1]*self.points[i].x*((1-cur_dist)**(self.nPoints-i-1))*((cur_dist)**(i))
                tempy += self.pascal_triangle[self.nPoints][i+1]*self.points[i].y*((1-cur_dist)**(self.nPoints-i-1))*((cur_dist)**(i))
            tempp = Point(tempx,tempy)
            self.tambah_point(tempp)
            cur_dist+=dist_per_point

    # fungsi untuk menyiapkan nilai-nilai yang diperlukan dalam metode dnc atau bf
    def create_bezier(self):
        self.bezier_points = []
        self.bezier_points = []
        self.tambah_point(self.points[0])
        if(self.method == "dnc"):
            self.dnc_populate_bezier_points(self.points,self.iteration)
        else:
            for i in range(self.iteration-1):
                self.power_of_2=self.power_of_2*2
            self.pascal_triangle.append([0,0])
            self.pascal_triangle.append([0,1,0])
            # print(self.pascal_triangle)
            for i in range(2,self.nPoints+1):
                temp = []
                for j in range (i+2):
                    if(j == 0 or j == i +1):
                        temp.append(0) 
                    else:
                        temp.append(self.pascal_triangle[i-1][j-1]+self.pascal_triangle[i-1][j])
                        # print(self.pascal_triangle[i-1][j-1]+self.pascal_triangle[i-1][j])
                self.pascal_triangle.append(temp)
            # print(self.pascal_triangle)
            self.bf_populate_bezier_points()
        self.tambah_point(self.points[len(self.points)-1])
    

    def display_bezier(self,exec_time):
        display_2sets_dots_and_line(self.points,self.bezier_points,exec_time)
    

    def tambah_point(self, point):
        self.bezier_points.append(Point(point.x,point.y))