from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin, tw, th
    size(500, 500)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
    bg_col = '#fffffa'
    strk_col = '#000000'
    fill_col = '#B22727'
    
    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)
    fill_col = tools.hex_to_hsb(fill_col)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 2
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 100
    
    # Margins between each grid cell
    grid_margin = 5
    
    # Outer size of grid cell
    tw = 25
    th = 100
        
    # Inner size of grid cell
    dw = tw - grid_margin
    dh = th - grid_margin
    
    # Number of rows and columns in grid
    rows = int(pheight // th)
    cols = int(pwidth // tw)
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 1
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenRandom(pg, fills.ScannerFill(pg))
    #pen = pens.PenBasic(pg, fills.BasicFill(pg))
    
    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    #pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    
    pg.endDraw()
    #pen.set_clean(True)
    #pen.prob = 0
    
    flag = True
    
def keyReleased():
    global flag
    
    if key == ENTER:
        flag = True


def draw2():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin
    pen.noFill()

                
    pen.fill(fill_col)
    pen.stroke(fill_col)
    r = 100
    c = PVector(pwidth/2, pheight/2)
    pen.circle(c, r)
    
    pen.rect(PVector(100, 100), 200, 100)
    for x in range(0, pwidth, 10):
        break
        d = r**2 - (x - c.x)**2
        m = 0
        if d > 0:
            y = sqrt(d) + c.y
            
            y_ = y - (y - c.y) * 2
        
            pen.line(PVector(x, 0), PVector(x, y_ - m))
            pen.line(PVector(x, y + m), PVector(x, pheight))
        elif d < 0:
            pen.line(PVector(x, 0), PVector(x, pheight))
            
        # Else d == 0
        else:
            m = 0
            pen.line(PVector(x, 0), PVector(x, c.y - m))
            pen.line(PVector(x, c.y + m), PVector(x, pheight))
    
    
    
    pen.stroke((0,0,0))
    pen.noFill()

        
def draw3():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin
    pen.noFill()

    pen.stroke((0,0,0))
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            # Coordinates, heights, and widths for the drawn grid:
            # (x                 , y                 , w , h )
            # (c * tw + (tw-dw)/2, r * th + (th-dh)/2, dw, dh)
            if random(1) < 0.05:
                pen.fill((0,0,0))
            else:
                pen.noFill()
            pg.pushMatrix()
            
            pg.translate(c*tw + grid_margin/2 + dw/2, r * th + grid_margin/2 + dh/2)
            #pg.rotate(map(dist(c * tw + (tw-dw)/2, r * th + (th-dh)/2, pwidth/2, pheight/2), 0, dist(0,0,pwidth/2,pheight/2), 0, PI))
            pg.rotate(map(dist(c*tw + grid_margin/2 + dw/2, r * th + grid_margin/2 + dh/2, pwidth/2, pheight/2), 0, 500, 0, PI))
            pen.rect(PVector(-dw/2, -dh/2), dw, dh)
            pg.popMatrix()
                
    pen.fill(fill_col)
    pen.stroke(fill_col)
    pen.circle(PVector(pwidth/2, pheight/2), 250)
    pen.noFill()


def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    if flag:
        flag = False
        pg.beginDraw()
    
        
        # Set background color
        pg.fill(0,0,80)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        pen.fill(bg_col)
        pen.noStroke()
        pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pen.noFill()
        
        
        pen.stroke(strk_col)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw3()
        
        pg.loadPixels()
        #tools.noisify_brightness(pg.pixels, pg)
        pg.updatePixels()
           
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
