package day11;

import java.util.ArrayList;
import java.util.List;

//Encapsulation
class Govt {
	private int seats;
	private String govtName;
	private int budget;

	public int getGovtseats() {
		return seats;
	}

	public String getGovtName() {
		return govtName;
	}

	public int getBudget() {
		return budget;
	}

	public void setbudget(int newValue) {
		budget = newValue;
	}

	public void setgovtName(String newValue) {
		govtName = newValue;
	}

	public void setGovtseats(int newValue) {
		seats = newValue;
	}
}

//abstraction
abstract class GovtType {
	abstract void display();
}

class State extends GovtType {
	void display() {
		System.out.println("State Government");

	}
}

//inheritance
class state {
	void agriculture() {
		System.out.println("Department of Agriculture");
	}
}

class Department extends state {
	void taxesDepartment() {
		System.out.println("Department of taxes");
	}
}

//Polymorphism
class City {
	public void print() {
		System.out.println("printing pincodes of states");
	}

	public void print(String name, int pincode) {
		System.out.println("state:" + name + " pincode:" + pincode);
	}

}

//composition,Association
class CabinetMinistries {
	public String deptName;
	public String name;

	CabinetMinistries(String deptName, String name) {
		this.deptName = deptName;
		this.name = name;

	}
}

class ministers {
	private final List<CabinetMinistries> CabinetMinistries;

	ministers(List<CabinetMinistries> CabinetMinistries) {
		this.CabinetMinistries = CabinetMinistries;
	}

	public List<CabinetMinistries> getCabinetMinistries() {
		return CabinetMinistries;
	}
}

//Aggregation acknowledges that the two classes have their own life cycle (i.e. can exist without each other). Each object is instantiated separately
class CouncilMinistries {
	public String portfolio;
	public String name;

	CouncilMinistries(String portfolio, String name) {
		this.portfolio = portfolio;
		this.name = name;

	}
}

public class Government {
	public static void main(String args[]) {
		Govt obj = new Govt();
		obj.setgovtName("Central Government");
		obj.setbudget(1000000);
		obj.setGovtseats(112);
		System.out.println("Government Name: " + obj.getGovtName());
		System.out.println("seats: " + obj.getGovtseats());
		System.out.println("Budget: " + obj.getBudget());
		State obj1 = new State();
		obj1.display();
		Department d = new Department();
		d.agriculture();
		d.taxesDepartment();
		City c = new City();
		c.print();
		c.print("Hyderabad", 500055);
		CabinetMinistries m1=new CabinetMinistries("Minister of Defence", "Shri Raj Nath Singh");
		CabinetMinistries m2=new CabinetMinistries("Minister of Home Affairs", "Shri Amit Shah"); 
		CabinetMinistries m3=new CabinetMinistries("Minister of External Affairs", "Dr. Subrahmanyam"); 
        List<CabinetMinistries> ministry = new ArrayList<CabinetMinistries>();   
        ministry.add(m1);   
        ministry.add(m2);   
        ministry.add(m3); 
        ministers ministers = new ministers(ministry);   
        List<CabinetMinistries> CabinetMinistries = ministers.getCabinetMinistries();   
        for (CabinetMinistries cm : CabinetMinistries) {   
            System.out.println("Ministry : " + cm.deptName   
                               + " and "  
                               + " Minister Name : " + cm.name);
       
	}
}
}