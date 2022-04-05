package day2;

import java.util.Objects;

//Question 1 - Create a class - Take a meaningful class name - e.g. Employee, Country, Student,
//				Birds, Animal and so on
public class Employee {
//Question 2 - Add attributes to class - Add Associated attribute to the class you chosen

	int eId;
	String enameString;
	String deptCode;
	String gender;

//Question 3 - Add Constructor to Class - Add default and parameterized constructor to 
//	           class
	public Employee() {
		super();

	}

	public Employee(int eId, String enameString, String deptCode, String gender) {
		super();
		this.eId = eId;
		this.enameString = enameString;
		this.deptCode = deptCode;
		this.gender = gender;
	}

//Question 4 - Add getter and setter to Class variables
	public int geteId() {
		return eId;
	}

	public void seteId(int eId) {
		this.eId = eId;
	}

	public String getEnameString() {
		return enameString;
	}

	public void setEnameString(String enameString) {
		this.enameString = enameString;
	}

	public String getDeptCode() {
		return deptCode;
	}

	public void setDeptCode(String deptCode) {
		this.deptCode = deptCode;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	// Question 5 - Override equals and hashCode method from object class

	@Override
	public int hashCode() {
		return Objects.hash(deptCode, eId, enameString, gender);
	}
//    Question 6 - Add method in class for equality check of class Objects

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Employee other = (Employee) obj;
		return Objects.equals(deptCode, other.deptCode) && eId == other.eId
				&& Objects.equals(enameString, other.enameString) && Objects.equals(gender, other.gender);
	}

//	Overloading
//	Question - 8 Show case method overloading by creating the methods for the
//				class created at step 1

	void emp(int id) {
		System.out.println("Overloading Id: " + id);
	}

	void emp(int id, String empName) {
		System.out.println("Overloading Id: " + id + " Name: " + empName);
	}

	public static void main(String[] args) {

//		Question 7 - Create two objects of class and do equality check with above method.

		Employee emp1 = new Employee();
		emp1.seteId(1);
		emp1.setEnameString("Gishnavi");
		emp1.setDeptCode("CSE");
		emp1.setGender("female");
		System.out.println("Emp ID: " + emp1.geteId() + "\nEmp Name is: " + emp1.getEnameString() + "\nEmpDept is: "
				+ emp1.getDeptCode() + "\nEmp Gender is: " + emp1.getGender());
		System.out.println("Hascode of " + emp1.geteId() + " is " + emp1.hashCode());
		System.out.println();

		Employee emp2 = new Employee(2, "Supriya", "It", "Female");

		System.out.println("Emp ID: " + emp2.geteId() + "\nEmp Name is: " + emp2.getEnameString() + "\nEmpDept is: "
				+ emp2.getDeptCode() + " \nEmp Gender is: " + emp2.getGender());
		System.out.println("Hascode of " + emp2.geteId() + " is " + emp2.hashCode());
		System.out.println();
		System.out.println("Both Equal? " + emp1.equals(emp2));
		System.out.println();
		emp1.emp(3);
		emp1.emp(4, "Jim");

	}

}