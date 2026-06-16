class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int left = 0;
        int right = heights.length-1;
        int l = heights.length -1;

        while (left < right){
            int min = Math.min(heights[left], heights[right]);
            int area = min * l;
            max = Math.max(max, area);
            if (heights[left]<=heights[right]){
                left ++;
            }else {
                right --;
            }
            l--;
        }
        return max;
    }
}
