%matplotlib inline

import contextily as cx
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm
import rasterio
from rasterio.plot import show as rioshow
import matplotlib.image as img


def mapCode(Column, mapColour, edgeColour, mapTitle):
    ax = merged_gdf.plot(
    Column
    ,figsize=(10,10)
    ,edgecolor=edgeColour
    ,linewidth=0.5
    ,vmax=50
    ,vmin=0
    ,legend=True
    ,legend_kwds= {'shrink':0.7}
    ,cmap=mapColour
    )

    ax.annotate(
    mapTitle,
    (0.5,1)
    ,xycoords = 'axes fraction'
    ,horizontalalignment='center'
    ,verticalalignment='bottom'
    ,fontsize = 20
    ,color='#000'
    ,fontstyle='normal'
    )


    # Link to add basemap
    data_url = "https://ndownloader.figshare.com/files/20232174"
    db = gpd.read_file(data_url)

    # Adding the basemap
    background = db.query("city_id == 'ci122'")
    cx.add_basemap(ax,
               crs=background.crs.to_string(),
               source=cx.providers.CartoDB.Voyager
                  )



    # Adding the scale bar
    ax.add_artist(ScaleBar(1, dimension= "si-length", units="m", location= 'lower right'))




    # Adding the north arrow
    x, y, arrow_length = 0.03, 0.98, 0.1
    ax.annotate('N', xy=(x, y), xytext=(x, y-arrow_length),
            arrowprops=dict(facecolor='black', width=5, headwidth=15),
            ha='center', va='center', fontsize=20,
            xycoords=ax.transAxes)
    
plt.savefig('lab5Map.png', dpi=300)