package day2.util;

public class CallTask2 {

	public static void main(String[] args) {
		Task2 task = new Task2();

		System.out.println("Factorial With Recursion: " + task.factWithRecursion(5));
		System.out.println("Addition Without Recursion: " + Task2.addWithoutRecursion(5));
	}

}
