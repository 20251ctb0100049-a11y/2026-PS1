public class TesteEmprestimo {
    public static void main(String[] args) {
        Livro livro = new Livro(
            "Dom Casmurro", "Machado de Assis", 1899
        );
        Livro outroLivro = new Livro(
            "Capitaes da Areia", "Jorge Amado", 1937
        );

        Leitor pedro = new Leitor("Pedro Alves", "2026010", 1);
        Leitor ana = new Leitor("Ana Lima", "2026011", 2);

        Emprestimo primeiro = new Emprestimo(livro, pedro);
        System.out.println(
            "Primeiro emprestimo: "
            + primeiro.realizarEmprestimo()
        );
        System.out.println(primeiro);
        System.out.println(
            "Livro disponivel? " + livro.estaDisponivel()
        );
        System.out.println(
            "Livros com Pedro: " + pedro.getLivrosEmMaos()
        );

        Emprestimo tentativaAna = new Emprestimo(livro, ana);
        System.out.println(
            "Mesmo livro para Ana: "
            + tentativaAna.realizarEmprestimo()
        );

        Emprestimo tentativaPedro =
            new Emprestimo(outroLivro, pedro);
        System.out.println(
            "Pedro acima do limite: "
            + tentativaPedro.realizarEmprestimo()
        );
        System.out.println(
            "Outro livro ainda disponivel? "
            + outroLivro.estaDisponivel()
        );

        System.out.println(
            "Devolucao: " + primeiro.registrarDevolucao()
        );
        System.out.println(
            "Segunda devolucao: "
            + primeiro.registrarDevolucao()
        );

        System.out.println(
            "Outro livro para Pedro: "
            + tentativaPedro.realizarEmprestimo()
        );
        System.out.println(
            "Livros com Pedro: " + pedro.getLivrosEmMaos()
        );
    }
}