import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Scanner;

public class AES {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        String key = "1234567890abcdef"; // 16 bytes
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");

        System.out.print("Enter plaintext: ");
        String plaintext = sc.nextLine();

        // Encrypt
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] encrypted = cipher.doFinal(plaintext.getBytes());

        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(encrypted));

        // Decrypt
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        byte[] decrypted = cipher.doFinal(encrypted);

        System.out.println("Decrypted: " + new String(decrypted));
    }
}
