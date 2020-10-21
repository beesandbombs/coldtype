Text
====

To run any of these examples, you'll want to save a bit of code in a python file, with any name, e.g. ``text.py``, and then run that file by navigating to it on the command line and constructing a call like, ``coldtype shape.py``

Basic Text
----------

Let’s start with a simple Hello World, except in this case, let’s just say COLDTYPE, because the coldtype repository has a special version of Obviously in it that just has those letters.

.. code:: python

    from coldtype import *

    @renderable((1000, 200))
    def basic(r):
        return (StyledString("COLDTYPE",
            Style("assets/ColdtypeObviously-VF.ttf", 150))
            .pens()
            .align(r))

Which should get you this:

.. image:: /_static/renders/text_basic.png
    :width: 500

You might be wondering why the text is blue — that’s the default fill color for any text in coldtype. Let’s mess w/ the color and set some variable font axis values:

.. code:: python

    @renderable((1000, 200))
    def lessbasic(r):
        return (StyledString("COLDTYPE",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=150))
            .pens()
            .align(r)
            .f(hsl(0.8, s=0.75)))

.. image:: /_static/renders/text_lessbasic.png
    :width: 500

What’s interesting (and different) about setting text with Coldtype is that you are telling the computer to draw text, you're asking for information about the individual glyphs and where they sit, given the parameters you’re passing into the combination of ``StyledString`` and ``Style``.

Put another way, what you get back from calling ``(StyledString, Style(...)).pens()`` is a rich set of data that can be inspected and manipulated.

.. code:: python

    @renderable((1000, 200))
    def print_tree(r):
        pens = (StyledString("COLDTYPE",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=150))
            .pens()
            .align(r)
            .f(Gradient.Vertical(r, hsl(0.5, s=0.8), hsl(0.8, s=0.75))))
        
        pens.print_tree()
        pens[0].rotate(180)
        pens[-1].rotate(180)
        pens[-2].rotate(10)
        return pens

Because of the line ``pens.print_tree()``, you should see something like this in your terminal when you run that example:

.. code:: text

    <DPS:pens:8:tag(?)>
        <DP(typo:int(True)(C))/tag:(Unknown)>
        <DP(typo:int(True)(O))/tag:(Unknown)>
        <DP(typo:int(True)(L))/tag:(Unknown)>
        <DP(typo:int(True)(D))/tag:(Unknown)>
        <DP(typo:int(True)(T))/tag:(Unknown)>
        <DP(typo:int(True)(Y))/tag:(Unknown)>
        <DP(typo:int(True)(P))/tag:(Unknown)>
        <DP(typo:int(True)(E))/tag:(Unknown)>
    </DPS>

And because of the lines with calls to `rotate`, you should see this on your screen:

.. image:: /_static/renders/text_print_tree.png
    :width: 500

Less Basic Text
---------------

Usually, glyph-wise hierarchical representation of text is not a feature of software or software libraries, because when programmers sit down to implement support for text, they do it with the understanding that if you want text, you usually want a `lot` of text, set in large blocks, like this paragraph that you’re reading now.

But for lots of graphic design, what you actually want is very precise control over only a few glyphs, maybe a line or two. That was the magic of technologies like moveable type, or especially Letraset; those technologies gave designers direct control over letterforms. A lot like when you hit "Convert to Outlines" in Illustrator today.

Of course, there’s a big downside to having direct control: it is excruciatingly slow. And more than that, even when you’re working with just a few letters, you might need to change those letters at the last minute, right before a project is due.

Which is where code really shines. All the manipulations I’ve done so far are not "destructive," like Convert to Outlines. As far as we’re concerned, the "textbox" (so to speak) is still intact, ``StyledString("COLDTYPE"...``

To illustrate that point, let’s change the text:

.. code:: python

    @renderable((1000, 200))
    def typecold(r):
        pens = (StyledString("TYPECOLD",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=150))
            .pens()
            .align(r)
            .f(Gradient.Vertical(r, hsl(0.5, s=0.8), hsl(0.8, s=0.75))))
        
        pens[0].rotate(180)
        pens[-1].rotate(180)
        pens[-2].rotate(10)
        return pens

.. image:: /_static/renders/text_typecold.png
    :width: 500

The last two examples also illustrate something important about Coldtype — (almost) everything is self-mutating by default. So a line like ``pens[0].rotate(180)`` changes ``pens[0]`` directly, meaning you don’t need to assign it to a new variable. This makes it very easy to directly manipulate nested structures without needing to reassign variables.

This also means that sometimes it is very necessary to ``copy`` pens in order to double them. For instance:

.. code:: python

    @renderable((1000, 200))
    def simpledrop(r):
        pens = (StyledString("TYPECOLD",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=250))
            .pens()
            .align(r)
            .f(1))
        return DATPenSet([
            pens.copy().translate(10, -10).f(0),
            pens.s(hsl(0.9)).sw(3)
        ])

.. image:: /_static/renders/text_simpledrop.png
    :width: 500

I’ll admit the impact of the interesting dropshadow here is lessened somewhat by the appearance of the strange pink lines in the top layer of text. When I added the code stroking the pens (``.s(hsl(0.9)).sw(3)``), I thought it would look like a standard stroked shape. But if you’re familiar with how variable fonts are constructed, those lines might not seem all that strange to you — they indicate that the letters are constructed in order to interpolate cleanly. That said, we probably don’t want to see them! So there’s a special ``ro=1`` flag that you can pass to any ``Style`` constructor, and that’ll ``(r)emove (o)verlaps`` on all the glyphs before they come back to you in their correct positions.

.. code:: python

    @renderable((1000, 200))
    def ro(r):
        pens = (StyledString("TYPECOLD",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=100, ro=1))
            .pens()
            .align(r)
            .f(1))
        return DATPenSet([
            pens.copy().pen().castshadow(-45, 50).f(0),
            pens.s(hsl(0.9)).sw(3)
        ]).align(r, th=1, tv=1)

.. image:: /_static/renders/text_ro.png
    :width: 500

Fixed! Also I did some completely unrelated things there.

* Instead of simply offsetting the main text to get a shadow, this example collapses the set of pens to a single pen (via ``.pen()``), and then uses a built-in method called ``castshadow(<angle>, <distance>)`` to cast a shadow.

* When you cast a shadow like that, your text might look a little un-centered, so to fix that we’ve added an additional ``align`` call at the end, passing ``th=1`` and ``tv=1`` to indicate that we want the whole thing centered perfectly (true-horizontal and true-vertical) within the bounding rectangle ``r``. (Those flags are useful for a type-centric graphics engine, because up until now we’ve relied on the pre-set cap-height of the letters to vertically align glyphs, rather than their "true height" which varies from letter to letter.)

One additional refinement you may want to make in an example like this is that you'd want to individually cast shadows based on a glyph + a little bit of stroke set around it, in the style of the 19th-century type designers. So let’s do that:

.. code:: python

    @renderable((1000, 200))
    def stroke_shadow(r):
        pens = (StyledString("COLDTYPE",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=100, ro=1))
            .pens()
            .align(r)
            .f(1))
        return DATPenSet([
            (pens.copy()
                .pmap(lambda i, p: (p
                    .outline(10)
                    .removeOverlap()
                    .castshadow(-45, 50)
                    .f(None)
                    .s(hsl(0.6, s=1, l=0.4))
                    .sw(4)))),
            pens.s(hsl(0.9)).sw(4)
        ]).align(r, th=1, tv=1)

.. image:: /_static/renders/text_stroke_shadow.png
    :width: 500

Dang, you know I thought that example would just work, but it looks like there are some tiny little dots present, which I think are artifacts of the ``castshadow`` call. I didn’t write the guts of that (Loïc Sander wrote something called a ``TranslationPen`` which is used by coldtype internally), so I don’t understand it completely, but it shouldn’t be difficult to devise a way to clean up those tiny specks by testing the ``bounds`` of each of the contours created by the ``TranslationPen``. We can do that by iterating over the individual contours with the ``filter_contours`` method provided by the ``DATPen`` class. We can also use the opportunity demonstrate some debugging techniques, like isolating a single letter and blowing it up.

.. code:: python

    @renderable((1000, 500))
    def stroke_shadow_cleanup(r):
        pens = (StyledString("O",
            Style("assets/ColdtypeObviously-VF.ttf",
                500, wdth=0.5, rotate=10, tu=100, ro=1))
            .pens()
            .align(r)
            .f(1))
        
        return DATPenSet([
            (pens
                .copy()
                .pmap(lambda i, p:
                    (p.outline(10)
                        .reverse()
                        .removeOverlap()
                        .castshadow(-5, 500)
                        .filter_contours(lambda j, c: c.bounds().w > 50)
                        .f(None)
                        .s(hsl(0.6, s=1, l=0.4))
                        .sw(4)))),
            pens.s(hsl(0.9)).sw(4)
        ]).align(r, th=1, tv=1)

.. image:: /_static/renders/text_stroke_shadow_cleanup.png
    :width: 500

Got it! If you comment out the ``.filter_contours`` line, you should see the little speck show up again.

Two suggestions to help you better understand code or find weird looks: try commenting out various stuff and using random colors.

.. code:: python

    @renderable((1000, 200))
    def stroke_shadow_random(r):
        pens = (StyledString("COLDTYPE",
            Style("assets/ColdtypeObviously-VF.ttf",
                150, wdth=0.5, rotate=10, tu=100, ro=1))
            .pens()
            .align(r)
            .f(1))
        return DATPenSet([
            (pens.copy()
                .pmap(lambda i, p: (p
                    .outline(10)
                    #.removeOverlap() # commented out
                    .castshadow(-45, 50)
                    .f(hsl(random(), s=1, a=0.1))
                    .s(hsl(random(), s=1, l=0.4))
                    .sw(4)))),
            pens.pmap(lambda i, p: p.s(hsl(random())).sw(4))
        ]).align(r, th=1, tv=1)

.. image:: /_static/renders/text_stroke_shadow_random.png
    :width: 500