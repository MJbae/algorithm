package MJ.Algorithm;

import java.util.HashMap;
import java.util.Scanner;

public class Resistor {
    public static void main(String args[]) {
        HashMap<String, Long[]> registersMap = new HashMap<>();
        registersMap.put("black", new Long[]{0L, 1L});
        registersMap.put("brown", new Long[]{1L, 10L});
        registersMap.put("red", new Long[]{2L, 100L});
        registersMap.put("orange", new Long[]{3L, 1000L});
        registersMap.put("yellow", new Long[]{4L, 10000L});
        registersMap.put("green", new Long[]{5L, 100000L});
        registersMap.put("blue", new Long[]{6L, 1000000L});
        registersMap.put("violet", new Long[]{7L, 10000000L});
        registersMap.put("grey", new Long[]{8L, 100000000L});
        registersMap.put("white", new Long[]{9L, 1000000000L});

        Scanner scan = new Scanner(System.in);
        String firstColor = scan.next();
        String secondColor = scan.next();
        String thirdColor = scan.next();

        long result = (registersMap.get(firstColor)[0]*10
                + registersMap.get(secondColor)[0])
                * registersMap.get(thirdColor)[1];
        System.out.println(result);
    }
}
