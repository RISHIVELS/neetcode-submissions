class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int num: nums){
            int count = map.getOrDefault(num,0);
            map.put(num,count+1);
        }
        for (int num: map.keySet()){
            int count = map.get(num);
            if (count>1) return true; 
        }
        return false; 
    }
}