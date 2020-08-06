package abc;

import java.util.Scanner;

public class Solution1 {
    public static void main(String args[] ) throws Exception {

        Scanner s = new Scanner(System.in);
        int[] a = new int[4];
        // for(int i=0; i<4; i++){
        //     a[i]=
        // }
        String x = s.nextLine();
       // System.out.print(x);
        Point p1 = new Point(Integer.parseInt(String.valueOf(x.charAt(0))),Integer.parseInt(String.valueOf(x.charAt(2))));
        Point p2 = new Point(Integer.parseInt(String.valueOf(x.charAt(4))),Integer.parseInt(String.valueOf(x.charAt(6))));
    

    double r = findDistance( p1,  p2);
    String p = String.valueOf(r);
    String[] t=p.split("\\.");
    if(t[1].contains("2") ||t[1].contains("3") ||t[1].contains("4") ||t[1].contains("5") ||t[1].contains("1") ||t[1].contains("6") ||t[1].contains("7") ||t[1].contains("8") ||t[1].contains("9")) {
//    	System.out.println(p);
    	p=t[0]+t[1];
    	System.out.println(p+".000");
    }else {
//    	System.out.println(p);
    	System.out.println(t[0]+".000");	
    }

    }
    public static double findDistance(Point p1, Point p2)
    {
        return Math.sqrt((p2.getX()-p1.getX())*(p2.getX()-p1.getX())+(p2.getY()-p1.getY())*(p2.getY()-p1.getY()));

    }
}

class Point
{
    private int x=0;
    private int y=0;

    public Point(int x,int y){
        this.x=x;
        this.y=y;

    }
    public void setX(int x){
        this.x=x;
    }
    public void setY(int y){
        this.y=y;
    }

    public int getX(){
        return this.x;
    }
    public int getY(){
        return this.y;
    }
    
}