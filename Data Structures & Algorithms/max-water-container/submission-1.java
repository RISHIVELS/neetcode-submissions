class Solution {
    public int maxArea(int[] heights) {
        //  keep track of the max area 
        int max = 0;
        // pointers
        int left = 0;
        int right = heights.length-1;
        // length to multiply
        int l = heights.length -1;

        while (left < right){
            // take the minimum bar height
            int min = Math.min(heights[left], heights[right]);
            // calc the area
            int area = min * l;
            // calc the max
            max = Math.max(max, area);
            // if bar height is low then move that pointer
            if (heights[left]<=heights[right]){
                left ++;
            }else {
                right --;
            }
            // reduce the length
            l--;
        }
        return max;
    }
}
