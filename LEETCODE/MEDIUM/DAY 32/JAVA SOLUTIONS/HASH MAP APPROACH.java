public int singleNumber(int[] A) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int x : A) {
        int count = map.containsKey(x) ? map.get(x) : 0;
        map.put(x, count + 1);
    }
    for (int x : A) {
        if (map.get(x) == 1) return x;
    }
    throw new IllegalArgumentException("No single element");
}
