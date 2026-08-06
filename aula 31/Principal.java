public class Principal {

    public static void main(String[] args) {
        int[] numeros = {10, 20, 30, 40};

        int resultado = calculaSoma(numeros);

        System.out.println("A soma é: " + resultado);
    }

    static int calculaSoma(int[] numeros) {
        if (numeros == null) {
            return 0;
        }

        int soma = 0;
        for (int n : numeros) {
            soma += n;
        }
        return soma;
    }
}