package abc;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

public class Ab {

	public static void main(String[] args) {
		BigInteger i = new BigInteger("99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999");
		BigDecimal  b =new BigDecimal(i);
		System.out.println(i.add(i));
		System.out.println(b.toString());
		System.out.println((int)'a'+" "+(int)'Z');
		int[] arr = new int[5];
		System.out.println(arr);
		Hashtable<String,Integer> map= new Hashtable<String,Integer>();
		map.put("s", 1);
		map.put("u", 2);
		map.put("m", 3);
		map.put("i", 4);
		map.put("t", 5);
		
		Iterator<Entry<String, Integer>> s = map.entrySet().iterator();
		
		while (s.hasNext()){
			
			System.out.println(s.next());
			
		}
		int j=0;
		for(int k=65; k<91; k++) {
			System.out.print(k+"-->"+(char)k +" ");
			j++;
		}
		double a = 0.02;
	   double c = 0.03;
	   double d = c - a;
	   System.out.println(d);
	   Object[] names = new String[3];
	   names[0] = new Integer(0);
	   System.out.println(names[0]);

	}

}
