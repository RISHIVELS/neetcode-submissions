class Solution {

    public static class Pair {
        int value;
        int count;
        Pair(int value, int count){
            this.value = value;
            this.count = count;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map <Integer,Integer> map = new HashMap<>();
        List<Pair> pairArr = new ArrayList<>();
        for (int num: nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        for (int key: map.keySet()){
            int count = map.get(key);
            Pair obj = new Pair(key,count);
            pairArr.add(obj);
        }
        // sort the list 
      Collections.sort(pairArr, ( obj1, obj2) -> {
            return obj2.count - obj1.count;
        });
        int[] result = new int[k];
        int index = 0;
        for(Pair obj: pairArr){
            if (index == k) break;
            result[index++] = obj.value;
        }
        return result;

    }
}
