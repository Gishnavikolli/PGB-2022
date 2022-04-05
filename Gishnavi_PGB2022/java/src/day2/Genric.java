package day2;

public class Genric<A> {
	public A getElement() {
		return element;
	}

	public void setElement(A element) {
		this.element = element;
	}

	A element;

	public static void main(String[] args) {
		Genric<Integer> empId = new Genric<Integer>();
		empId.setElement(1);
		System.out.println("Emp Id is :" + empId.getElement());
		Genric<String> empName = new Genric<String>();
		empName.setElement("Gishnavi");
		System.out.println("Emp Name is :" + empName.getElement());
	}

}
