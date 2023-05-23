// https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

// you can also use imports, for example:
// import java.util.*;
import java.lang.Math;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int X, int Y, int D) {

        if (X == Y || D == 0)
            return 0;

        int res = Y - X;

        double temp;

        temp = Math.ceil((double) res / D);
        res = (int)temp;

        return res;
    }
}
