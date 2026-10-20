public class TesteLivroDAO {
    public static void main(String[] args) {
        LivroDAO dao = new LivroDAO();


        dao.atualizarLivro(1, "1984 - Edição Especial", "George Orwell", 1949);

        dao.excluirLivro(2);
    }
}