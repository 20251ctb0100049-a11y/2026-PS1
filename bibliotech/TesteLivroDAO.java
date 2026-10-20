public class TesteLivroDAO {
    public static void main(String[] args) {
        LivroDAO dao = new LivroDAO();

        System.out.println("--- 1 e 2. Cadastrando os Livros ---");
        boolean livro1 = dao.adicionarLivro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943);
        System.out.println("Livro 1 cadastrado: " + livro1);

        boolean livro2 = dao.adicionarLivro("Dom Casmurro", "Machado de Assis", 1899);
        System.out.println("Livro 2 cadastrado: " + livro2);

        System.out.println("\n--- 4. Atualizando o título do primeiro livro ---");
        int idLivro1 = 1; 
        boolean atualizado = dao.atualizarLivro(
            idLivro1,
            "O Pequeno Príncipe - Edição Revisada",
            "Antoine de Saint-Exupéry",
            1943
        );
        System.out.println("Livro atualizado: " + atualizado);

        System.out.println("\n--- 5. Excluindo o segundo livro ---");
        int idLivro2 = 2; 
        boolean excluido = dao.excluirLivro(idLivro2);
        System.out.println("Livro excluído: " + excluido);
    }
}