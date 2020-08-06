package linked;

public class Runner {

	public static void main(String[] args) {
		
		LinkedList l=new LinkedList();
		
		l.add(11);
		l.add(12);
		l.add(8);
		l.add(18);
		l.add(16);
		l.add(5);
		l.add(18);
		
		l.show();
		
		l.del_node(l.head, 0);

	}

}
