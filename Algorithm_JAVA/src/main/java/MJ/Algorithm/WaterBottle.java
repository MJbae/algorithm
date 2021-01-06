package MJ.Algorithm;

import java.util.LinkedList;
import java.util.Scanner;

public class WaterBottle {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        scanner.close();

        LinkedList<Integer> listOfBottles = new LinkedList<>();
        for (int i = 0; i < N; i++) listOfBottles.add(1);
    }
}
