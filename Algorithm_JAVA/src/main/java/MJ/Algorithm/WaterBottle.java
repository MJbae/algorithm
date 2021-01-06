package MJ.Algorithm;

import java.util.ArrayList;
import java.util.Scanner;

public class WaterBottle {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        scanner.close();

        // N개 만큼의 물병에 물을 1L만큼 채워넣음
        ArrayList<Integer> bottles = new ArrayList<>();
        for (int i = 0; i < N; i++) bottles.add(1);

        int numOfBottlesBought = 0;
        // 물병의 수가 K 보다 작을 때까지 순회
        while (bottles.size() > K) {
            // 모든 물병에 대해 순차적으로 순회
            for (int j = 0; j < bottles.size() - 1; j++) {
                // 앞뒤 물병의 물의 양이 같다면
                // 하나의 물병에 담긴 물의 양을 두배로 늘리고
                // 다른 하나의 물병은 삭제
                if (bottles.get(j) == bottles.get(j + 1)) {
                    bottles.set(j, bottles.get(j) * 2);
                    bottles.remove(j + 1);
//                    System.out.println(j);
//                    for(Integer bottle : bottles) System.out.print(bottle + " ");
//                    System.out.println("");
                // 앞뒤 물병의 쿨의 양이 다르다면
                // 물의 양이 차이가 1이라면
                // 물을 사온 후, 두 물병을 하나로 합침
                } else {
                    if (Math.abs(bottles.get(j) - bottles.get(j + 1)) == 1) {
                        int biggerWater = Math.max(bottles.get(j), bottles.get(j + 1));
                        bottles.set(j, biggerWater * 2);
                        bottles.remove(j + 1);
                        numOfBottlesBought++;
                    }
                }
            }
        }
//        for(Integer bottle : bottles) System.out.print(bottle + " ");
//        System.out.println("");
        System.out.println(numOfBottlesBought);

//        for(Integer bottle : bottles) System.out.println(bottle);
    }
}
