class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length ==1 || nums.length ==0) return nums.length;

        int max = 1;
        Set <Integer> unique = new HashSet<>();
        for (int num: nums){
            unique.add(num);
        }
        for (int i=0; i<nums.length; i++){
            int cnt = 1;
            int num = nums[i];
            if (unique.contains(num - 1)) continue;
            while (true){
                if(unique.contains(num+1)){
                    cnt++;
                    max = Math.max(cnt,max);
                    num+=1;
                }else {
                    break;
                }
            }
        }
        return max;
    }
}