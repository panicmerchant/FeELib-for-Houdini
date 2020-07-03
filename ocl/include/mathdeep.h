
#ifndef __MATHDEEP_H__
#define __MATHDEEP_H__

#include <mathdeep.h>


inline
float maxf(
    float a,
    float b
    ) {
    return a > b ? a : b;
}

inline
float absf(
    float arg
    ) {
    return arg < 0 ? -arg : arg;
}


inline
float lerpf(
    float val0,
    float val1,
    float bias
    ) {
    return val0 * (1-bias) + val1 * bias;
}


inline
float clampf(
    float val,
    float min,
    float max
    ) {
    return val < min ? min : (val > max ? max : val);
}


/*
    //////////////////int x0 y0 x1 y1
    //Bresenham's line algorithm
    //https://zh.wikipedia.org/zh-cn/布雷森漢姆直線演算法
    int steep = absf(y1 - y0) > absf(x1 - x0);
    int temp;
    if (steep) {
        temp = x0;
        x0 = y0;
        y0 = temp;
        //swap(x0, y0)
        temp = x1;
        x1 = y1;
        y1 = temp;
        //swap(x1, y1)
    }
    if ( x0 > x1 ) {
        temp = x0;
        x0 = x1;
        x1 = temp;
        //swap(x0, x1)
        temp = y0;
        y0 = y1;
        y1 = temp;
        //swap(y0, y1)
    }
    int deltax = x1 - x0;
    int deltay = absf(y1 - y0);
    int error = deltax / 2;
    int ystep;
    int y = y0;
    if ( y0 < y1 ) {
        ystep = 1;
    } else {
        ystep = -1;
    }
    for (int x = x0; x < x1; ++x) {
        int idx_middle;
        if (steep) {
            idx_middle = density_stride_offset
                       + y * density_stride_x
                       + x * density_stride_y;
        } else {
            idx_middle = density_stride_offset
                       + x * density_stride_x
                       + y * density_stride_y;
        }
        density[idx_middle] = 1;

        error = error - deltay;
        if ( error < 0 ) {
            y = y + ystep;
            error = error + deltax;
        }
    }
*/

/*
    //////////////////float x0 y0 x1 y1
    //Bresenham's line algorithm
    //https://zh.wikipedia.org/zh-cn/布雷森漢姆直線演算法
    float temp;
    int steep = absf(y1 - y0) > absf(x1 - x0);
    if (steep) {
        temp = x0;
        x0 = y0;
        y0 = temp;
        //swap(x0, y0)
        temp = x1;
        x1 = y1;
        y1 = temp;
        //swap(x1, y1)
    }
    if ( x0 > x1 ) {
        temp = x0;
        x0 = x1;
        x1 = temp;
        //swap(x0, x1)
        temp = y0;
        y0 = y1;
        y1 = temp;
        //swap(y0, y1)
    }
    float deltax = x1 - x0;
    float deltay = absf(y1 - y0);
    float error = deltax / 2;
    float ystep;
    float y = y0;
    if ( y0 < y1 ) {
        ystep = 1;
    } else {
        ystep = -1;
    }
    for (int x = x0; x < x1; ++x) {
        int idx_middle;
        if (steep) {
            idx_middle = density_stride_offset
                       + y * density_stride_x
                       + x * density_stride_y;
        } else {
            idx_middle = density_stride_offset
                       + x * density_stride_x
                       + y * density_stride_y;
        }
        density[idx_middle] = 1;

        error = error - deltay;
        if ( error < 0 ) {
            y = y + ystep;
            error = error + deltax;
        }
    }
*/







#endif
