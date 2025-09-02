import rasterio
from rasterio.plot import show as rasplot
import matplotlib.pyplot as plt

# with rasterio.open("IMG_T2V_20241012033956_ORTHO_PMS_32.tif") as src:
#     rasplot(src)
#     plt.show()



# imgsrc = rasterio.open("IMG_T2V_20241012033956_ORTHO_PMS_32.tif")
# rasplot(imgsrc,band=1,title="World Tree")
# plt.show()

# with rasterio.open("IMG_T2V_20241012033956_ORTHO_PMS_32.tif") as srcShow:
#     # rasplot(srcShow)
#     rasplot(srcShow.read(2),transform=srcShow.transform)


# with rasterio.open("IMG_T2V_20241012033956_ORTHO_PMS_32.tif") as imgPyplot:
#     plt.imshow(imgPyplot.read(1),cmap="pink")
#     plt.show()

with rasterio.open("IMG_T2V_20241012033956_ORTHO_PMS_32.tif") as src:
    fig, ax = plt.subplots(1, figsize=(12, 12))
    rasplot((src, 1), cmap='Greys_r', interpolation='none', ax=ax)
    rasplot((src, 1), contour=True, ax=ax)
    plt.show()
