package sk;

class t{
	int q=0;
	 t() {
		q=5;
	}
}

public class S extends t{
	protected int p=0;
	 protected S() {
		super();
		q=9;
		p=10;
		
	}

	public static void main(String[] args) {
		t s = new S();
		//System.out.println(s.p);
		System.out.println(s.q);
	}

}
