package day5;

import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.Executors;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class ThreadPool {
	public static void main(String[] args) {
		ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(4);

		for (int i = 1; i <= 7; i++) {
			Task task = new Task("TaskId " + i);
			System.out.println("Created : " + task.getName());

			executor.execute(task);
		}
		executor.shutdown();
	}
}

class Task implements Runnable {
	private String name;

	public Task(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void run() {
		try {
			Long duration = (long) (Math.random() * 10);
			System.out.println("Executing : " + name);
			TimeUnit.SECONDS.sleep(duration);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
