# File driver.py 
from BezierCurve import BezierCurve
from util import Point
import time

# mengambil input dan validasi input
inp_nPoints = 0
while (inp_nPoints<2):
    try:
        inp_nPoints = int(input("Masukkan jumlah titik (lebih besar atau sama dengan 2): "))
    except ValueError:
        print("Masukan bukan integer")

ps = []
for i in range(inp_nPoints):
    print(f"Titik ke-{i+1}")
    inp_x = "not defined"
    inp_y = "not defined"
    while not isinstance(inp_x, float) :
        try:
            inp_x = float(input("Masukkan Koordinat x: "))
        except ValueError:
            print("Masukan bukan float")
    while not isinstance(inp_y, float) :
        try:
            inp_y = float(input("Masukkan Koordinat y: "))
        except ValueError:
            print("Masukan bukan float")
    ps.append(Point(inp_x,inp_y))

inp_iteration = 0
while not(isinstance(inp_iteration, int) and inp_iteration>=1):
    try:
        inp_iteration = int(input("Masukkan jumlah iterasi (lebih besar atau sama dengan 1): "))
    except ValueError:
        print("Masukan bukan integer")

inp_type_method = ""
while (inp_type_method != "bf" and inp_type_method != "dnc"):
    print("Pilih tipe penyelesaian:\n1.Divide and conquer\n2.Bruteforce")
    inp_temp = input()
    if(inp_temp == "1"): inp_type_method = "dnc"
    if(inp_temp == "2"): inp_type_method = "bf"

start_time = time.time()
# membangun kurva bezier
bezier_curve = BezierCurve(ps,inp_iteration,inp_type_method)
bezier_curve.create_bezier()
# menampilkan waktu eksekusi
end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000
# display hasil
bezier_curve.display_bezier(execution_time_ms)

