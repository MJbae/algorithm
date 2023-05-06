package MJ.Algorithm;

import java.util.*;

public class DistributedProcessing {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int a, b;

        int[] results = new int[T];

        for(int i = 0; i < T; i++){
            a = sc.nextInt();
            b = sc.nextInt();
            int base = a % 10;
            int exponent = (b % 4 == 0) ? 4 : b % 4;
            double nthOfData = (int)Math.pow(base, exponent);
//            System.out.println(nthOfData);
            results[i] = (nthOfData % 10 == 0) ? 10 : (int)(nthOfData % 10);
        }

        sc.close();

        for (int result : results) System.out.println(result);
    }
}
