public class TesteRequisitos {

    // Dois contadores da classe: somam o resultado de todas as verificacoes.
    private static int passaram = 0;
    private static int falharam = 0;

    // Confere uma condicao. Quem compara e o programa, nao os seus olhos.
    private static void verificar(String requisito, boolean condicao) {
        if (condicao) {
            passaram = passaram + 1;
            System.out.println("OK       " + requisito);
        } else {
            falharam = falharam + 1;
            System.out.println("FALHOU   " + requisito);
        }
    }

    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();
        
        // Corrigido para cadastrarLivro (com L maiúsculo)
        biblioteca.cadastrarLivro(new Livro("Dom Casmurro", "Machado de Assis", 1899));
        biblioteca.cadastrarLivro(new Livro("Capitaes da Areia", "Jorge Amado", 1937));
        
        biblioteca.cadastrarLeitor(new Leitor("Pedro Alves", "2026010", 1));
        biblioteca.cadastrarLeitor(new Leitor("Ana Lima", "2026011", 2));

        Livro dom = biblioteca.buscarLivro("Dom Casmurro");
        Leitor pedro = biblioteca.buscarLeitor("2026010");

        // RF01 e RF02: o que foi cadastrado pode ser encontrado.
        verificar("RF01 livro cadastrado aparece na busca", dom != null);
        verificar("RF02 leitor cadastrado aparece na busca", pedro != null);

        // RF03: consultar a disponibilidade.
        verificar("RF03 livro novo esta disponivel", dom.estaDisponivel());
        verificar("RF03 titulo fora do acervo nao e encontrado", 
            biblioteca.buscarLivro("O Cortico") == null);

        // RF05: registrar o emprestimo e recusar o que nao pode.
        verificar("RF05 emprestimo de livro disponivel e aceito",
            biblioteca.emprestar("Dom Casmurro", "2026010"));
        verificar("RF05 livro emprestado fica indisponivel",
            !dom.estaDisponivel());
        verificar("RF05 leitor passa a ter 1 livro em maos",
            pedro.getLivrosEmMaos() == 1);
        verificar("RF05 livro emprestado e recusado para outro leitor",
            !biblioteca.emprestar("Dom Casmurro", "2026011"));
        verificar("RF05 leitor no limite e recusado",
            !biblioteca.emprestar("Capitaes da Areia", "2026010"));

        // RF04: registrar a devolucao de livro emprestado.
        verificar("RF04 devolucao de emprestimo ativo e aceita",
            biblioteca.devolver("Dom Casmurro"));
        verificar("RF04 livro devolvido volta a ficar disponivel",
            dom.estaDisponivel());
        verificar("RF04 segunda devolucao e recusada",
            !biblioteca.devolver("Dom Casmurro"));

        System.out.println();
        System.out.println(passaram + " passaram, " + falharam + " falharam.");
    }
}