package ch.unibas.kpw;

public class Program {static long factor = 10;static long max(long a,
long b){/* 3 */if (a > b)return a;else return b;}static long compute(long x){/* 2 */long y=factor*max(x, 0);return y;}public static void main(String[] args){/* 1 */long n=0;java.util.Scanner sc=new java.util.Scanner(System.in);System.out.println("Bitte Zahl eingeben");n = sc.nextLong()
;System.out.println(compute(n));sc.close();}}