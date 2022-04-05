package day3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Positionchar {

	public static String char_Count(String s) {
		Map<Character, List<Integer>> elements = new HashMap<>();
		s = s.replaceAll(" ", "");
		for (int i = 0; i < s.length(); i++) {
			char id = s.charAt(i);
			if (elements.containsKey(id)) {
				elements.get(id).add(i);
			} else {
				elements.put(id, new ArrayList<Integer>());
				elements.get(id).add(i);
			}

		}
		return elements.toString();
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
		System.out.print("Enter String : ");
		String input = bfr.readLine();
		System.out.print(char_Count(input));

	}

}