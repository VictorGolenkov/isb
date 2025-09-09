import java.util.Random;

public class Main {
    /**
     * Generates a 128-bit random binary sequence
     *
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        Random random = new Random();
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < 128; i++) {
            sb.append(random.nextBoolean() ? '1' : '0');
        }
        
        System.out.println(sb.toString());
    }
}