package Recursive;

public class MyPow {
    // stack overflow
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }

        if(n == Integer.MIN_VALUE){
            x = x * x;
            n = n/2;
        }

        if(n<0){
            n = -n;
            x = 1/x;
        }

        return x * myPow(x, n - 1);
    }

    public double myPow2(double x, int n) {
        if(n == 0) return 1;
        if(n == Integer.MIN_VALUE){
            x = x * x;
            n = n/2;
        }
        if(n < 0) {
            n = -n;
            x = 1/x;
        }

        return (n%2 == 0) ? myPow(x * x, n/2) : x *  myPow(x * x, n/2);
    }

    public static void main(String[] args) {
        MyPow my = new MyPow();
        System.out.println("The result: " + my.myPow(-2, -4));
        System.out.println("The result: " + my.myPow2(-2, -4));
    }
}
