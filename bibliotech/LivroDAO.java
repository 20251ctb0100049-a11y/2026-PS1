import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class LivroDAO {

    public boolean adicionarLivro(
            String titulo, String autor, int ano) {

        String sql =
            "INSERT INTO livros (titulo, autor, ano) " +
            "VALUES (?, ?, ?)";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando =
                 conexao.prepareStatement(sql)) {

            comando.setString(1, titulo);
            comando.setString(2, autor);
            comando.setInt(3, ano);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            System.out.println(
                "Erro ao adicionar: " + e.getMessage()
            );
            return false;
        }
    }

    public boolean atualizarLivro(
            int id, String titulo,
            String autor, int ano) {

        String sql =
            "UPDATE livros " +
            "SET titulo = ?, autor = ?, ano = ? " +
            "WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando =
                 conexao.prepareStatement(sql)) {

            comando.setString(1, titulo);
            comando.setString(2, autor);
            comando.setInt(3, ano);
            comando.setInt(4, id);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            System.out.println(
                "Erro ao atualizar: " + e.getMessage()
            );
            return false;
        }
    }

    public boolean excluirLivro(int id) {

        String sql =
            "DELETE FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando =
                 conexao.prepareStatement(sql)) {

            comando.setInt(1, id);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            System.out.println(
                "Erro ao excluir: " + e.getMessage()
            );
            return false;
        }
    }
}