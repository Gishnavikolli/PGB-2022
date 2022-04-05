package day4;

import java.util.Scanner;

class AgeNotSufficientException extends Exception {
	public AgeNotSufficientException(String str) {
		super(str);
	}
}

public class Employee {
	static void validate(int age) throws AgeNotSufficientException {
		if (age < 22) {

			throw new AgeNotSufficientException("Employee age is not valid");
		} else {
			System.out.println("Employee age is valid");
		}
	}

	static String name = null;

	public int addition(int empId1, int empId2) {
		return (empId1 + empId2);

	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("enter empId1 and empId2:\n" + "	");
		int empId1 = sc.nextInt();
		int empId2 = sc.nextInt();
		System.out.println("Addition is:" + (empId1 + empId2));
		sc.nextLine();
		System.out.println("enter name:");
		String nme = sc.nextLine();
		try {//null pointer exception
			System.out.println(name.equals(nme));
		} catch (NullPointerException e) {
			System.out.println("NullPointerException");
		}
		try {//custom exception
			System.out.println("enter Age:");
			int age = sc.nextInt();
			validate(age);
		} catch (AgeNotSufficientException e) {

			System.out.println("AgeNotSufficientException");

		}

		int empId3;//NumberFormatException
		while (true) {
			System.out.println("Enter any valid Integer: ");
			try {
				empId3 = Integer.parseInt(sc.next());
				System.out.println("You entered: " + empId3);
				break;
			} catch (NumberFormatException e) {
				System.out.println("NumberFormatException occurred");

			}

		}

		try {
			int a = 30, b = 0;
			int c = a / b; // cannot divide by zero
			System.out.println("Result = " + c);
		} catch (ArithmeticException e) {
			System.out.println("Can't divide a number by 0");
		}
		try {
			Class temp = Class.forName("jim"); // calling the jim class
		} catch (ClassNotFoundException e) {
			System.out.println("ClassNotFoundException");
		}
		new Thread(() -> {
			System.out.println("Thread Functional  Interface");//Built in Functional interface with lambda expression 
		}).start();
	}

}
