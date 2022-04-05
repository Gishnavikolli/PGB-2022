package day5;

public class Synchronization implements Runnable {

	int books = 3;
	static int i = 1, j = 2, k = 3;

	synchronized void buybooks(String name, int RequiredBooks) {
		if (RequiredBooks <= books) {
			System.out.println(RequiredBooks + " bought by " + name);
			books = books - RequiredBooks;
		} else {
			System.out.println("Books Not Available");
		}
	}

	public void run() {
		String name = Thread.currentThread().getName();
		if (name.equals("t1")) {
			buybooks(name, i);
		} else if (name.equals("t2")) {
			buybooks(name, j);
		} else {
			buybooks(name, k);
		}
	}

	public static void main(String[] args) {
		Synchronization s = new Synchronization();
		Thread t1 = new Thread(s);
		Thread t2 = new Thread(s);
		Thread t3 = new Thread(s);
		t1.setName("t1");
		t2.setName("t2");
		t3.setName("t3");
		t1.start();
		t2.start();
		t3.start();
	}

}
