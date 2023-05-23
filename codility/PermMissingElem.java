// https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // Implement your solution here

        int res = 0;

        for(int i=0; i < A.length; i++){
            res ^= i+1;
            res ^= A[i];
        }

        res ^= A.length+1;

        return res;

    }
}
