package abc;

import java.util.ArrayList;
import java.util.Arrays;

public class WeightesUniformString {
	
	static String[] weightedUniformStrings(String s, int[] queries) {
		//(int)'z' - 96
		//s=s+"0";
		ArrayList<Integer> list = new ArrayList<Integer>();
		int count=1;
		char c=s.charAt(0);
		list.add(((int)c - 96)*count);
		for(int i=1; i<s.length();i++) {
			
			if(s.charAt(i)==c) {
				count+=1;
				list.add(((int)c - 96)*count);
			}else {
				
				c=s.charAt(i);
				count=1;
				list.add(((int)c - 96)*count);
			}
		}
		System.out.println(list);
		String[] list1 = new String[queries.length];
		for(int i=0; i<queries.length; i++) {
			
			if(list.contains(queries[i])) {
				list1[i]="Yes";
			}else {
				list1[i]="No ";
			}
		}
		return list1;
	}


	public static void main(String[] args) {
		int[] a = {9,7,8,12,5};
		String[] b = weightedUniformStrings("aaabbbbcccddd",a);
		for(int i=0; i<b.length; i++) {
			
			System.out.println(b[i]);
		}

	}

}
