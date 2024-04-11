import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;

public class QuiltingBee{
    // arraylist of scale
    private static ArrayList<Double> scale = new ArrayList<Double>();
    // arraylist of colour values
    private static ArrayList<Integer> rVal = new ArrayList<Integer>();
    private static ArrayList<Integer> gVal = new ArrayList<Integer>();
    private static ArrayList<Integer> bVal = new ArrayList<Integer>();

    private static ArrayList<Integer> xCorner = new ArrayList<Integer>();
    private static ArrayList<Integer> yCorner = new ArrayList<Integer>();
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String temp = "";
        System.out.println("Syntax: 'scale r g b'\nUse ctrl+c or 'exit' to close input.");
        System.out.print("Input Quilting Values: ");
            // error handling
            while (in.hasNextLine()) {
                temp = in.nextLine();
                // allow exit
                if (temp.equalsIgnoreCase("exit")) {
                    System.out.println("Exiting...");
                    break;
                }
                if (inputSyntaxHandler(temp)) {
                    inputHandler(temp);
                    System.out.println("Added!");
                } else {
                    System.out.print("--------\nLine(s) Had Invalid Syntax, Correct Syntax: 'scale r g b'\nInput More Values: ");
                }
            }
        in.close();
    // now run quilting logic!
    }
    // main logic for controlling where the squares are drawn
    public static void quiltMaster(){
        JFrame jframe = new JFrame("QuiltingBee");
        
        for(int i=0; i<scale.size(); i++){
            int toDraw = (int)Math.pow(i+1, 2);
            if(i==0){
                squareLogic(i, 0, 0);
            }

        }
    }
    public static void squareLogic(int index, int x, int y){
        int size = scale * 500;
        xCorner.add()
    }


/* Methods Related to Input Handling */
    // method to check that inputted numbers are formatted correctly
    public static boolean inputSyntaxHandler(String input){
        String parts[] = input.split(" ");
        // check there are enough values given
        if(parts.length!=4){
            return false;
        }
        // try for parsing values
        try{
            double scale = Double.parseDouble(parts[0]);
            int r = Integer.parseInt(parts[1]);
            int g = Integer.parseInt(parts[2]);
            int b = Integer.parseInt(parts[3]);
            // check that rgb & scale numbers are valid.
            if(scale<0 || r<0 || r>255 || b<0 || b>255 || g<0 || g>255){
                return false;
            }
        } catch(NumberFormatException e){
            return false;
        }
        return true;
    }
    // adds correct input to the arraylists
    public static void inputHandler(String input){
        String parts[] = input.split(" ");
        scale.add(Double.parseDouble(parts[0]));
        rVal.add(Integer.parseInt(parts[1]));
        gVal.add(Integer.parseInt(parts[2]));
        bVal.add(Integer.parseInt(parts[3]));
    }
}