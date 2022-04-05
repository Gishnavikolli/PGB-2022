package day3;

//Interface Add
interface Person {
//	Declare 2 methods in interface
	String getName(String pName);

	int getId(int pid);
}

// Add a Abstract Class
abstract class Department {
//	method with definition
	public String dName(String dName) {
		System.out.println("Dept Name is" + dName);
		return dName;
	}

	public int dId(int did) {
		return did;
	}
}

public class Employee extends Department implements Person {
	int eId;
	String eNameString;

	// Implement methods of interface
	@Override
	public String getName(String pName) {

		return pName;
	}

	@Override
	public int getId(int pid) {

		return pid;
	}

	public Employee() {
		super();

	}

	public Employee(int eId, String eNameString) {
		super();
		this.eId = eId;
		this.eNameString = eNameString;
	}

	public int geteId() {
		return eId;
	}

	public void seteId(int eId) {
		this.eId = eId;
	}

	public String geteNameString() {
		return eNameString;
	}

	public void seteNameString(String eNameString) {
		this.eNameString = eNameString;
	}

//Override Abstract class
	public String dName(String dName) {
//		System.out.println("Dept Name is: " + dName);
		return dName;
	}

	public int dId(int did) {
		return did;
	}

	// main method
	public static void main(String[] args) {
//		Objects Of concrete class
		Employee e1 = new Employee(1, "Gishnavi");
		Employee e2 = new Employee();
		e2.seteId(2);
		e2.seteNameString("Supriya");
		System.out.println("Emp ID: " + e1.geteId() + " Emp Name is: " + e1.geteNameString());
		System.out.println("Emp ID: " + e2.geteId() + " Emp Name is: " + e2.geteNameString());
//		Access the abstract methods
		System.out.println("Dept ID (Abstract): " + e1.dId(987));
		System.out.println("Dept Name (Abstract): " + e1.dName("CSE"));
//	Access the concrete class methods
		System.out.println("Dept Name (Concrete): " + e2.dName("IT"));
	}

}