package linked;

class x{
	
	static public void funPar() {
		System.out.println("parent1");
	}
	
	public void funPar2() {
		System.out.println("parent2");
	}
	
	public final void xyz() {
		System.out.println("final method");
	}
	
}

class child extends x{
	
	static public void funPar() {
		System.out.println("parentchild");
	}
	
	public void funchild() {
		System.out.println("child1");
	}
	
	public void funPar2() {
		System.out.println("child2");
	}
}



public class Par {

	public static void main(String[] args) {
		
//		int[] arr = {-4 ,3 ,-9, 0 ,4 ,1};
//		int pos=0,nev=0,zer=0;
//        for (int i=0; i<arr.length; i++){
//            if(arr[i]<0){
//                nev+=1;
//            }else if(arr[i]>0){
//                pos+=1;
//            }else{
//                zer+=1;
//            }
//        }
//        System.out.println(1/2);
//        double x=(float)pos/arr.length;
//        double y=nev/arr.length;
//        double z=zer/arr.length;
//        System.out.println(x);
//        System.out.println(y);
//        System.out.println(z);
		
		
		
		x.funPar();
		child.funPar();
		x b = new x();
		x a = new child();
		//child c = new child();
		a.funPar();
		a.funPar2();
		//a.funchild();
//		a.funPar();
//		a.funPar2();
		System.out.println(a);
		System.out.println(b);
		//a.funchild();

	}

}
