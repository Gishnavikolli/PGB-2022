package day4;

import day4.CustomFunctionalInterface;

interface CustomFunctionalInterface {
	   void display();
	}
public class Main {
	   public static void main(String args[]) {
	      
	      CustomFunctionalInterface test1 = new CustomFunctionalInterface() {
	         public void display() {
	            System.out.println("Display using Anonymous inner class");
	         }
	      };
	      test1.display();
	      // Using Lambda Expression
	      CustomFunctionalInterface test2 = () -> { 
	         System.out.println("Display using Lambda Expression");
	      };
	      test2.display();
	   }
	}