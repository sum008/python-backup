package linked;

import java.util.ArrayList;

public class String_man {
	
	public static void str(int n,String s) {
		ArrayList<String> list = new ArrayList<String>();
		int count=0;
		String temp="";
		for(int i=0; i<s.length(); i++) {
			
			if(s.charAt(i)!=' ') {
				temp+=s.charAt(i);
			}else {
				list.add(temp);
				temp="";
			}
		}
		list.add(temp);
		temp="";
			
		for(int i=0; i<list.size() ;i++) {
			
			for (int j=0; j<n ;j++) {
				temp=temp+list.get(i);
				count++;
			}
			list.set(i, temp);
			temp="";
		}
		
		System.out.println(list+" "+count);
	}
	
	public static void str1(int n,String s) {
		ArrayList<String> list = new ArrayList<String>();
		int t=0;
		String temp="";
		for(int i=0; i<s.length(); i++) {
			
			if(s.charAt(i)!=' ') {
				temp+=s.charAt(i);
			}else {
				list.add(temp);
				temp="";
			}
		}
		list.add(temp);
		temp="";
		int count=1;
		int pos=0;
		int i=0;	
		for(; i<=list.size()*n+3 ;i++) {
			
			if(count<=n) {
				temp+=list.get(pos);
			}else {
				list.set(pos, temp);
				temp ="";
				count=0;
				pos+=1;
			}
			count++;
			t++;
		}
		
		System.out.println(list+" "+t);
	}
	
	public static void str3(int n,String s) {
		ArrayList<String> list = new ArrayList<String>();
		int t=0;
		String temp="";
		for(int i=0; i<s.length(); i++) {
			
			if(s.charAt(i)!=' ') {
				temp+=s.charAt(i);
			}else {
				list.add(temp);
				temp="";
			}
		}
		list.add(temp);
		temp="";
		int till=list.size()*n;
		int i=0;
		for(; i<till; i++) {
			temp=list.get(i);
			for(int j=0; j<n-1; j++) {
				t++;
				list.add(i,temp);
				
			}
			i=i+n-1;
		}
		
		System.out.println(list+" "+t);
	}
	
	
	public static void lis(ArrayList<Integer> arr) {
		
		ArrayList<Integer> list = new ArrayList<Integer>();
		int min = arr.get(0);
		list.add(arr.get(0));
		for(int i=1; i<arr.size(); i++) {
			if(arr.get(i)<min) {
				min=arr.get(i);
				
			}else {
				list.add(arr.get(i));
			}
		}
		if(list.get(0)!=min) {
			list.add(0, min);
		}
		System.out.println(list);
	}
	
	public static void lis1(ArrayList<Integer> arr) {
		
		ArrayList<Integer> list = new ArrayList<Integer>();
		int min = arr.get(0);
		list.add(arr.get(0));
		int pos=0;
		for(int i=1; i<arr.size(); i++) {
			if(arr.get(i)<min) {
				min=arr.get(i);
				pos=i;
			}else {
				list.add(arr.get(i));
			}
		}
		if(list.get(0)!=min) {
			
			list.add(pos, list.get(0));
			list.set(0, min);
		}
		System.out.println(list);
	}

	public static void main(String[] args) {
		
		str(5,"my name is sumit");
		str1(5,"my name is sumit");
		str3(5,"my name is sumit");
		
		ArrayList<Integer> list = new ArrayList<Integer>();
		list.add(4);
		list.add(5);
		list.add(1);
		list.add(2);
		list.add(3);
		
		lis1(list);
		lis(list);

	}

}
