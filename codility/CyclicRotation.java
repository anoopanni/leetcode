// https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public void reverse(int[] arr, int i, int j){
        while (i < j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i += 1;
            j -= 1;
        }
    }

    public int[] solution(int[] A, int K) {
        if (A.length == 0)
            return A;
        
        K = K % A.length;

        if (K == A.length)
            return A;
        
        // Implement your solution here
        reverse(A, 0, A.length-1);
        reverse(A, 0, K-1);
        reverse(A, K, A.length-1);
        // System.out.println(Arrays.toString(A));

        return A;

    }
}
