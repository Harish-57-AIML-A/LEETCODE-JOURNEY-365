import java.util.*;

public class PlusOne {
    public List<Integer> plusOne(List<Integer> digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            int digit = digits.get(i);

            if (digit < 9) {
                digits.set(i, digit + 1);
                return digits;
            } else {
                digits.set(i, 0);
            }
        }

        // If all digits were 9
        digits.add(0);  
        digits.set(0, 1);
        return digits;
    }

    public static void main(String[] args) {
        PlusOne sol = new PlusOne();
        System.out.println(sol.plusOne(new ArrayList<>(Arrays.asList(1,2,3)))); // [1,2,4]
        System.out.println(sol.plusOne(new ArrayList<>(Arrays.asList(9,9,9)))); // [1,0,0,0]
    }
}
