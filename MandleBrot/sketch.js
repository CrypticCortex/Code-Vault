function setup() {
    createCanvas(300,400);
    background(220);
    text("my ps5 tst.", 10, 15);
}

function draw() {
    //making madelbrot set with rgb values
    loadPixels();
    for (let x = 0; x < width; x++) { //width = 400
        for (let y = 0; y < height; y++) { //height = 300
            let a = map(x, 0, width, -1.5, 1); //we use map to map the x value from 0 to 400 to -1.5 to 1
            let b = map(y, 0, height, -1, 1);// maps the y value from 0 to 300 to -1 to 1
            let ca = -0.70176; //ca is a constant and is set to a
            let cb = -0.85464;
            let n = 0;
            let z = 0;
            while (n < 100) { //100 is the max number of iterations
                let aa = a * a - b * b; //aa is a squared - b squared
                let bb = 2 * a * b; //bb is 2ab
                a = aa + ca; //a is aa + ca
                b = bb + cb; //b is bb + cb
                if (abs(a + b) > 16) { //if the absolute value of a + b is greater than 16 then, 16 is the max value of the magnitude of a complex number
                    break;
                }
                n++;
            }
            //rgb values
            let r = map(n, 0, 50, 0, 255); //maps the number of iterations to a value between 0 and 255
            let g = map(n, 0, 50, 0, 255); //maps the number of iterations to a value between 0 and 255
            let B = map(n, 0, 50, 0, 255); //maps the number of iterations to a value between 0 and 255
            if (n === 100) { //if the number of iterations is 100 then the pixel is black
                r = 100;
                g = 60;
                B = 160;
            }
            let pix = (x + y * width) * 4; //pix is the pixel location
            pixels[pix + 0] = r; //sets the pixel to the value of r
            pixels[pix + 1] = g; //sets the pixel to the value of g
            pixels[pix + 2] = B; //sets the pixel to the value of b
            pixels[pix + 3] = 1000; //sets the alpha value of the pixel to 255 which is opaque
        }
    }
    updatePixels();
}