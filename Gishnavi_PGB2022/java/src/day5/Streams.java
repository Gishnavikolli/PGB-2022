package day5;

import java.util.*;
import java.util.stream.Collectors;

public class Streams {

	static int[] ints = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 29 };
	// array is converted to list
	static List<Integer> list = Arrays.stream(ints).boxed().collect(Collectors.toList());

	public static void main(String[] args) {
		// to get prime numbers from the list
		list.stream().map(primenumber -> Main.prime(primenumber))
				// to get prime numbers below 25
				.filter(primenumber -> (primenumber < 25 && primenumber > 0))
				// to sort the elements in the list in descending order
				.sorted(Comparator.reverseOrder())
				// to store the sorted list into a list
				.collect(Collectors.toList())
				// to print the prime numbers less than 25
				.forEach(System.out::println);
		// to get the sum of the elements in the list
		System.out.println("Sum : " + list.stream().reduce(0, (a, b) -> a + b, Integer::sum));
	}

}

// check Prime number 
class Main {
	static int prime(int n) {
		int i, m = 0, flag = 0;
		m = n / 2;
		if (n == 0 || n == 1) {
			return 0;
		} else {
			for (i = 2; i <= m; i++) {
				if (n % i == 0) {
					return 0;
				}
			}
			return n;
		}
	}
}
