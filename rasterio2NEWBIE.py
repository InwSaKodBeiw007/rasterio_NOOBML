a = "hello world"
print(a)

import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

with rasterio.open('IMG_T2V_20241012033956_ORTHO_PMS_32.tif') as src:
    insite = src.read()
    # show(insite) # Fullscreen insite.shape มันจะใหญ่มากทั้งภาพ (4,10000,10000) (band, height, width)
    print("ชื่อไฟล์:", src.name)
    print("จำนวน band:", src.count)
    print("ขนาด (width, height):", src.width, src.height)
    print("dtype:", src.dtypes)
    print("crs (พิกัด):", src.crs)
    print("transform (affine):", src.transform)
    print("driver:", src.driver)
    print("bounds (ขอบเขต):", src.bounds)

    # src.width = [300]
    # src.height = [300]
    # show(src) we need to use code below to fix monitor

    from rasterio.windows import Window
    # กำหนด window (x_off, y_off, width, height) x,y หมายถึงตำแหน่งที่จะเริ่ม width,height ขนาด <3
    Swindow = Window(0,0,300,300)
    cropped = src.read(window=Swindow)

    # print(cropped.shape) # ณ ตรงนี้ มัน minimum ลงมาแล้ว (4,300,300)(band,height,width) ตาม window=กำหนดมาเลย 
    # print(cropped) yoo this thing ปริ้นมา arry มาหมดเลย like print(insite)
    show(cropped) # Top-left screen
