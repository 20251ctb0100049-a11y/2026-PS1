public class Principal {

    public static void main(String[] args) {
        int[] numeros = {15, 42, 8, 99, 23};

        int menor = menorValor(numeros);

        System.out.println("O menor valor é: " + menor);
    }

    static int menorValor(int[] numeros) {
        if (numeros == null || numeros.length == 0) {
            return 0;
        }

        int menor = numeros[0];
        int it = 1;
        while (it < numeros.length) {
            if (numeros[it] < menor) {
                menor = numeros[it];
            }
            it++;
        }
        return menor;
    }
}