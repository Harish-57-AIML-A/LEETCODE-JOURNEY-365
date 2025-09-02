class TwoSum {
    private Map<Integer, Integer> table = new HashMap<>();
    
    // Add number to the data structure
    public void add(int number) {
        int count = table.getOrDefault(number, 0);
        table.put(number, count + 1);
    }
    
    // Find if there exists a pair with given sum
    public boolean find(int value) {
        for (Map.Entry<Integer, Integer> entry : table.entrySet()) {
            int num = entry.getKey();
            int y = value - num;
            if (y == num) {
                if (entry.getValue() >= 2) return true;
            } else if (table.containsKey(y)) {
                return true;
            }
        }
        return false;
    }
}
