package abc;

public class love_letter {
	
	public static int loverLetter(String s) {
		int count=0;
		int j=s.length()-1;
		for(int i=0; i<s.length()-1; i++) {
			
			if(s.charAt(i)>s.charAt(j)) {
				
				int r = (int)s.charAt(i)- (int)s.charAt(j);
				count+=r;
			}else if(s.charAt(i)<s.charAt(j)) {
				int r = (int)s.charAt(j)- (int)s.charAt(i);
				count+=r;
			}
			j--;
			if(i>j || i==j) {
				break;
			}
		}
		return count;
		
		
	}

	public static void main(String[] args) {
		System.out.println((int)'z' - 96);
		loverLetter("cba");
	}

}
