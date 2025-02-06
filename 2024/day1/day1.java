import java.util.Arrays;
import java.util.Scanner;
import java.io.File;

public class day1{


  public static void main (String[] args) {

    int N = 1000;
    int i = 0;
    int[] n1 = new int[N];
    int[] n2 = new int[N];      
 

    try (Scanner scan = new Scanner(new File("input.txt"))) {
      while (scan.hasNextLine()) {
        String[] a = scan.nextLine().split("\\s+");
        n1[i] = Integer.parseInt(a[0]);
        n2[i] = Integer.parseInt(a[1]);
        i++;
     }
    } catch (Exception e) {
      System.out.println("file not found");
    }

    int output = 0;
    Arrays.sort(n1);
    Arrays.sort(n2);
    for (int j=0; j < N; j++) {
      output += Math.abs(n1[j] - n2[j]);
    }                
    System.out.println(output);
 
  }
}
