import math, sys, os, re
from pathlib import Path

from coldtype.text import *
from coldtype.text.reader import Font
from coldtype.pens.datpen import DATPen, DATPenSet, DATPenLikeObject, DATText
from coldtype.geometry import *
from coldtype.color import *
from coldtype.renderable import *
from coldtype.helpers import *
from coldtype.animation import *
#from coldtype.renderer.state import RendererState, Keylayer

name = "coldtype"
__version__ = "0.1.4"