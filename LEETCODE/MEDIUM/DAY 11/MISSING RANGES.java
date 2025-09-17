import java.util.*;

class Solution {
    public List<String> findMissingRanges(int[] nums, int start, int end) {
        List<String> ranges = new ArrayList<>();
        int prev = start - 1;

        for (int i = 0; i <= nums.length; i++) {
            int curr = (i == nums.length) ? end + 1 : nums[i];
            if (curr - prev >= 2) {
                ranges.add(getRange(prev + 1, curr - 1));
            }
            prev = curr;
        }
        return ranges;
    }

    private String getRange(int low, int high) {
        return (low == high) ? String.valueOf(low) : low + "->" + high;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findMissingRanges(new int[]{0, 1, 3, 50, 75}, 0, 99));
        // Output: [2, 4->49, 51->74, 76->99]
    }
}

