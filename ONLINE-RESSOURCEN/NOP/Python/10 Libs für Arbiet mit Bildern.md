#### scikit-image
* arbeitet mit NumPy
* Doku: https://scikit-image.org/docs/stable/user_guide.html
* Bsp: Bild filtern
```python
import matplotlib.pyplot as plt 
 %matplotlib inline

from skimage import data,filters

image = data.coins()
 # … или любой массив NumPy!
 edges = filters.sobel(image)
 plt.imshow(edges, cmap=’gray’)
```
#### NumPy
- da Bilder-Pixels in Array gespeichert werden => NumPy
* Doku: https://numpy.org/
* Bsp: Maskierung
```python
import numpy as np
from skimage import data
import matplotlib.pyplot as plt 
%matplotlib inline

image = data.camera()
 type(image)

numpy.ndarray #Изображение - это массив NumPy

mask = image < 87
 image[mask]=255
 plt.imshow(image, cmap=’gray’)
```

#### SciPy
+ vor Allem Submodul: `scipy.ndimage`
* zum Filtern, usw.
* Doku: https://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html#correlation-and-convolution
+ Bsp: Gauss Filter
```python
from scipy import misc,ndimage

face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)

#Ergebnis
plt.imshow(<image to be displayed>)
```

#### PIL/Pillow (Python Imaging Library)
+ für Format-Umwandlung
* Doku: https://pillow.readthedocs.io/en/3.1.x/index.html
* Bsp: ImageFilter - Bild verbessern
```python
from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image
im.show()

from PIL import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.enhance(1.8).show("30% more contrast")
```

#### OpenCV-Python
* Lib für Bild-analyse
* Doku:
    1. https://github.com/abidrahmank/OpenCV2-Python-Tutorials
    2. https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_intro/py_intro.html

#### SimpleCV
* Lib für Bild-Analyse
* Doku: https://simplecv.readthedocs.io/en/latest/

#### Mahotas
* Lib für Bild-Analyse
* Doku: https://mahotas.readthedocs.io/en/latest/install.html
* Bsp: findMolly-Code: https://mahotas.readthedocs.io/en/latest/install.html

#### SimpleITK
* Insight Segementation and Registration Toolkit
* Bilder analysieren
* Doku:http://www.simpleitk.org/
    * Integraton mit Jupyter Notebook: https://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/

#### pgmagick
* ~ Driver für GraphicsMagick
+ Doku:
    1. https://github.com/hhatto/pgmagick
    2. https://pgmagick.readthedocs.io/en/latest/

#### PyCairo
* ~ Driver für Lib Cairo (2D-Vektro Graphik)
+ Doku:
    1. https://github.com/pygobject/pycairo
    2. https://pycairo.readthedocs.io/en/latest/tutorial.html