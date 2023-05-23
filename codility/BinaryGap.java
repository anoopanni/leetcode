// https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N) {
        // Implement your solution here
        String bin = Integer.toBinaryString(N);
        int res = 0;
        int idx = 0;

        for(int i=0; i < bin.length(); i++){
            if(bin.charAt(i) == '1'){
                int cur = i - idx;
                if(res < cur){
                    res = cur;
                }
                idx = i;
            }
        }
        if(res >= 1)
        return res-1;
        else
        return res;
    }
}
