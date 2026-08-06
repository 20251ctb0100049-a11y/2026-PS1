public class Principal {

    public static void main(String[] args) {
        int[] numeros = {5, 12, 8, 20, 3, 15};
        int limite = 10;

        int total = contarAcima(numeros, limite);

        System.out.println("Quantidade de números acima de " + limite + ": " + total);
    }

    static int contarAcima(int[] numeros, int limite) {
        if (numeros == null) {
            return 0;
        }

        int quantidade = 0;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] > limite) {
                quantidade++;
            }
        }
        return quantidade;
    }
}