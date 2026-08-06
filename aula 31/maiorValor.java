public class Principal {

    public static void main(String[] args) {
        int[] numeros = {15, 42, 8, 99, 23};

        int maior = maiorValor(numeros);

        System.out.println("O maior valor é: " + maior);
    }

    static int maiorValor(int[] numeros) {
        if (numeros == null || numeros.length == 0) {
            return 0; 
        }

        int maior = numeros[0];
        for (int n : numeros) {
            if (n > maior) {
                maior = n;
            }
        }
        return maior;
    }
}