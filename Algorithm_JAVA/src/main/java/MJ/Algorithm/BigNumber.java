package MJ.Algorithm;

import java.util.Scanner;
import java.util.Stack;

public class BigNumber {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String firstNum = scanner.next();
        String secondNum = scanner.next();
        StringBuffer firstNum2Buffer = new StringBuffer(firstNum);
        StringBuffer secondNum2Buffer = new StringBuffer(secondNum);

        // 입력 받은 수의 크기 비교
        // 작은 수의 빈칸을 0으로 채움
        boolean isFirstNumBigger = firstNum2Buffer.length() > secondNum2Buffer.length();
        int MAX_LEN = (isFirstNumBigger) ? firstNum2Buffer.length() : secondNum2Buffer.length();

        if (isFirstNumBigger) {
            for (int i = 0; MAX_LEN > (secondNum.length() + i); i++) {
                secondNum2Buffer.insert(0, "0");
            }
        } else {
            for (int i = 0; MAX_LEN > (firstNum.length() + i); i++) {
                firstNum2Buffer.insert(0, "0");
            }
        }

        // 각 입력값의 모든 자리수에 대해 연산
        // 자리수의 연산 결과는 Stack에 삽입
        int carry = 0;
        Stack<Character> result = new Stack<>();
        for (int j = MAX_LEN - 1; j >= 0; j--) {
            int firstString2Int = Character.getNumericValue(firstNum2Buffer.charAt(j));
            int secondString2Int = Character.getNumericValue(secondNum2Buffer.charAt(j));
            int numOfAddition = firstString2Int + secondString2Int + carry;
            int sum = (numOfAddition) % 10;

            result.push(Character.forDigit(sum, 10));
            carry = (numOfAddition) / 10;
        }

        if(carry == 1) result.push('1');

        // Stack의 모든 요소 출력
        while(!result.empty()){
            System.out.print(result.peek());
            result.pop();
        }
    }
}
