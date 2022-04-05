package day5;

import java.util.function.BiFunction;

interface MyInterface1{  
    Hello display(String say);  
}  
class Hello{  
    public Hello(String say){  
        System.out.print(say);  
    }  
}  


interface MyInterface{  
    void display();  
}  
class Multiplication{  
	   public static int multiply(int a, int b){  
		return a*b;  
	   }  
	}  
public class MethodReference {  
    public void myMethod(){  
	System.out.println("Instance Method");  
    }  
    public static void main(String[] args) {  
    	MethodReference obj = new MethodReference();   
	// Method reference using the object of the class
	MyInterface ref = obj::myMethod;  
	// Calling the method of functional interface  
	ref.display();  
	BiFunction<Integer, Integer, Integer> product = Multiplication::multiply;  
	int pr = product.apply(11, 5);  
	System.out.println("Product of given number is(Static Method): "+pr);  
	MyInterface1 one = Hello::new;  
	one.display("Hello World!(constructor)");  
    }  
}

