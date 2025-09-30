public int singleNumber(int[] A) {
    Set<Integer> set = new HashSet<>();
    for (int x : A) {
        if (set.contains(x)) set.remove(x);
        else set.add(x);
    }
    return set.iterator().next();
}
