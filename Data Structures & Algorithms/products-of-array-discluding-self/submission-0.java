class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        for (int i=0; i<nums.length; i++){
            int val = 1;
            for (int j=0; j<nums.length; j++){
                if (j==i) continue; 
                val *= nums[j];
            }
            arr[i] = val;
        }
        return arr;
    }
}  
