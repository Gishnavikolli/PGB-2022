package day2.util;

public class Task2 {
	static int factWithRecursion(int n) {
		if (n == 0) {
			return 1;
		} else {
			return n * factWithRecursion(n - 1);
		}

	}

	static int addWithoutRecursion(int n) {
		return n + n;

	}

	public static void main(String[] args) {
		System.out.println("Factorial With Recursion: " + factWithRecursion(5));
		System.out.println("Addition Without Recursion: " + addWithoutRecursion(5));
	}

}
