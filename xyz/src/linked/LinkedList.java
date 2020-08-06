package linked;

public class LinkedList {
	
	Node head;//Point to front element i.e first object of Node class
	Node tail;//Point to last element i.e last object of Node class
	
	public void add(int data){
		Node node=new Node(data);
		
		if(tail==null){
			head=node;
			tail=node; //tail at line 16 is this tail, thats why node at line 16 is entering at tail of previous node
			//System.out.println(head.data);
		}else{
			tail.nextnode=node;
			//tail=node;//TO make sure that tail is not null i.e it has been initialized(Working just like queue)
			tail=tail.nextnode;
			
		}
	}
	
	public void show(){
		
		while(head.nextnode!=null){
			System.out.println(head.data);
			head=head.nextnode;
		}
		System.out.println(head.data);
	}
	
	public void del_node(Node head,int position) {
		
		Node head1 = null;
		Node    current=null;
			  int  count=0;
			    while( count != position) {

			        if (head1==null){
			            Node x = new Node(head.data);
			            current=x;
			            head1=x;
			        } else {
			            current.nextnode = new Node(head.data);
			            current=current.nextnode;
			        }
			        count+=1;
			        head=head.nextnode;
			    }
			   current.nextnode=head.nextnode;
			   
			   while(head1.nextnode!=null){
					System.out.println(head.data);
					head1=head1.nextnode;
				}
				System.out.println(head1.data);
		
	}
	
	

}
