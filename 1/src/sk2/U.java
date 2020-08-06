package sk2;

import java.util.ArrayList;

import sk.S;

public class U extends S{
	
	U(){
		super();
		//q=1;
		p=2;
	}
	
	public static void main(String[] args) {
		 U u=new U();
		 System.out.println(u.p);
		 ArrayList<Object> l = new ArrayList<Object>();
		 l.add(55.2);
		 l.add("sfsd");
		 System.out.println(l);

	}

}
