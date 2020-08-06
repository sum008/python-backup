package abc;


import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String args[] ) throws Exception {
    	
        Scanner s = new Scanner(System.in);
        int id=s.nextInt();
        double balance=s.nextDouble();
        double interestRate=s.nextDouble();//s.nextLine();
        Account a=new Account(id,balance,interestRate);
        int noOfYears=s.nextInt();

        double result=calculateInterest(a, noOfYears);
        
//        String p = String.valueOf(result);
//        String[] t=p.split("\\.");
//        if(t[1].contains("2") ||t[1].contains("3") ||t[1].contains("4") ||t[1].contains("5") ||t[1].contains("1") ||t[1].contains("6") ||t[1].contains("7") ||t[1].contains("8") ||t[1].contains("9")) {
//        	
//        	p=t[0]+t[1];
//        	p=p+".000";
//        	System.out.println(Double.parseDouble(p));
//        }else {
//        	p=t[0]+".000";
//        	System.out.println(Double.parseDouble(p));	
//        }
        System.out.println(result);
        System.out.format("%.3f",result);
      }
    
    
    public static double calculateInterest(Account account, int noOfYear) {
        double temp = noOfYear * account.getInterestRate() / 100;
        System.out.println("temp "+temp);
        return (account.getBalance() * (account.getInterestRate()+temp) / 100);
    }
}

class Account
{
    private int id=0;
    private double balance=0;
    private double interestRate=0;

    public Account(int id,double balance,double interestRate){
        this.id=id;
        this.balance=balance;
        this.interestRate=interestRate;

    }
    public void setId(int id){
        this.id=id;
    }
    public void setBalance(double balance){
        this.balance=balance;
    }
    public void setinterestRate(double interestRate){
        this.interestRate=interestRate;
    }

    public int getId(){
        return this.id;
    }
    public double getBalance(){
        return this.balance;
    }
    public double getInterestRate(){
        return this.interestRate;
    }

}