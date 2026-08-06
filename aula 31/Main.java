public class Main {
    public static void main(String[] args) {
        int[] valores = {8, 3, 10, 5, 12};
        System.out.println(calculaSoma(valores));
        System.out.println(calculaMedia(valores));
        System.out.println(menorValor(valores));
        System.out.println(maiorValor(valores));
        System.out.println(contarAcima(valores, 6));
    }

    // Insira aqui os cinco métodos.
    public static int calculaSoma(int[] array) {
        int soma = 0;
        for (int v : array) {
            soma += v;
        }
        return soma;
    }

    public static double calculaMedia(int[] array) {
        if (array.length == 0) return 0.0;
        return (double) calculaSoma(array) / array.length;
    }

    public static int menorValor(int[] array) {
        int menor = array[0];
        for (int v : array) {
            if (v < menor) {
                menor = v;
            }
        }
        return menor;
    }

    public static int maiorValor(int[] array) {
        int maior = array[0];
        for (int v : array) {
            if (v > maior) {
                maior = v;
            }
        }
        return maior;
    }

    public static int contarAcima(int[] array, int limite) {
        int contador = 0;
        for (int v : array) {
            if (v > limite) {
                contador++;
            }
        }
        return contador;
    }
}