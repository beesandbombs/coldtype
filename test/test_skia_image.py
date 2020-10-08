from coldtype import *

co = Font("assets/ColdtypeObviously.designspace")

img = Path("test/renders/test_skia_image_is_image.png")

@renderable(rect=(1000, 1000))
def uses_image(r):
    return DATPenSet([
        DATPen().oval(r.inset(10)).f(hsl(0.5, l=0.2)),
        (DATPen()
            .oval(r.inset(20))
            .f(None)
            .attr(image=dict(src=img, opacity=0.35, rect=Rect(0, 0, 125, 125))))])

#@renderable(rect=(250, 250))
def is_image(r):
    return DATPenSet([
        DATPen().oval(r.inset(5)).f(hsl(random())),
        (StyledString("COLDTYPE",
            Style(co, 100, tu=50, ro=1, r=1, rotate=15, wdth=0))
            .pens()
            .align(r)
            .rotate(-45)
            .translate(0, 10)
            .f(1))])

#@renderable(rect=(500, 500))
def uses_shadow(r):
    return DATPenSet([
        (DATPen()
            .rect(r.inset(100))
            .rotate(45)
            .attr(shadow=dict(clip=r.inset(100), alpha=0.75, radius=30))
            .f(hsl(0.75))),
        (DATPen()
            .rect(r.take(20, "mdx"))
            .f(hsl(0.5))
            .rotate(-45)
            .attr(shadow=dict(alpha=1, radius=30))),
        (DATPen()
            .rect(r.take(20, "mdy"))
            .f(hsl(0.1, s=0.6, l=0.6))
            .attr(shadow=dict(alpha=1, radius=30)))
    ])