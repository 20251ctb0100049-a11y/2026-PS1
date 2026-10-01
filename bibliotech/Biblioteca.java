import java.util.ArrayList;

public class Biblioteca {

    private ArrayList<Livro> livros;
    private ArrayList<Leitor> leitores;
    private ArrayList<Emprestimo> emprestimos;

    // Construtor que inicializa as listas para evitar NullPointerException
    public Biblioteca() {
        this.livros = new ArrayList<>();
        this.leitores = new ArrayList<>();
        this.emprestimos = new ArrayList<>();
    }

    public void cadastrarLivro(Livro livro) {
        livros.add(livro);
    }

    public void cadastrarLeitor(Leitor leitor) {
        leitores.add(leitor);
    }

    public void listarAcervo() {
        for (int i = 0; i < livros.size(); i++) {
            System.out.println(livros.get(i));
        }
    }

    // Devolve o livro achado, ou null se o titulo nao esta no acervo.
    public Livro buscarLivro(String titulo) {
        for (int i = 0; i < livros.size(); i++) {
            Livro l = livros.get(i);
            if (l.getTitulo().equals(titulo)) {
                return l;
            }
        }
        return null;
    }

    public Leitor buscarLeitor(String matricula) {
        for (Leitor leitor : leitores) {
            if (leitor.getMatricula().equals(matricula)) {
                return leitor;
            }
        }
        return null;
    }

    public boolean emprestar(String titulo, String matricula) {
        Livro livro = buscarLivro(titulo);
        Leitor leitor = buscarLeitor(matricula);
        if (livro == null || leitor == null) {
            return false;
        }

        Emprestimo novo = new Emprestimo(livro, leitor);

        if (!novo.realizarEmprestimo()) {
            return false;
        }

        emprestimos.add(novo);
        return true;
    }

    // Procura o emprestimo ATIVO daquele titulo. O registro continua na lista
    public boolean devolver(String titulo) {
        for (int i = 0; i < emprestimos.size(); i++) {
            Emprestimo e = emprestimos.get(i);
            if (e.estaAtivo() && e.getLivro().getTitulo().equals(titulo)) {
                return e.registrarDevolucao();
            }
        }
        return false;
    }

    public void listarEmprestimos() {
        for (int i = 0; i < emprestimos.size(); i++) {
            System.out.println(emprestimos.get(i));
        }
    }
}
