// 371. Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/description/

class Solution {
    public int getSum(int a, int b) {

        while(b != 0){
            int temp = a ^ b; // addition without carry
            b = (a & b) << 1; // caluclating carry 
            a = temp;
        }
        return a;
    }
}
