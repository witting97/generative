PImage image;

void setup() {
  image = loadImage("DSC_2518.jpg");
  image.resize(750,0);
  image.loadPixels();
  size(750, 750);
}

// Convert color to gray
int gray(int c) {
  int r=(c&0x00FF0000)>>16; // red part
  int g=(c&0x0000FF00)>>8; // green part
  int b=(c&0x000000FF); // blue part
  return (r+b+g)/3; 
}

int avgColor(int[] pixels, int px, int py, int stepSize, int w) {
  int x = px - stepSize / 2;
  int y = py - stepSize / 2;
  int sum = 0;
  
  for (; x < px + stepSize / 2; x++) {
    for (; y < py + stepSize / 2; y++) {
      try {
        sum += gray(pixels[x + y * w]);
      } catch (ArrayIndexOutOfBoundsException e) {
        continue;
      }
    }
  }
  return sum / (stepSize * stepSize);
}


void draw() {
  int w = image.width;
  int h = image.height;
  int stepSize = 6;
  
  float x1, x2, y1, y2, cpx1, cpy1, cpx2, cpy2;
  
  x1 = 0;
  y1 = 0;
  background(255);
  stroke(200);
  
  for (int y = 0, yc = 0; y < h; y += stepSize, yc++) {
    float[] ys = new float[w / stepSize + 1];
    for (int x = 0, xc = 0; x < w; x += stepSize, xc++) {
      int c = avgColor(image.pixels, x, y, stepSize, image.width);
      ys[xc] = c;
    }
    
    for (int x = 0, xc = 3; xc < w / stepSize; x += stepSize * 3, xc += 3) {
      strokeWeight(map(ys[xc], 0, 150, 0, 10));
      x1 = x;
      y1 = y - ys[xc - 3];
      cpx1 = x1 + stepSize;
      cpy1 = y - ys[xc - 2];
      cpx2 = cpx1 + stepSize;
      cpy2 = y - ys[xc - 1];
      x2 = cpx2 + stepSize;
      y2 = y - ys[xc];
      bezier(x1, y1, cpx1, cpy1, cpx2, cpy2, x2, y2);
    }
  }
  noLoop();
}
