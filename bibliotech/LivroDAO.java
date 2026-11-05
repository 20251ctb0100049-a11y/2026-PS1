import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class LivroDAO {

    public List<Livro> listarLivros() {
        List<Livro> livros = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano FROM livros ORDER BY id";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql);
             ResultSet resultado = comando.executeQuery()) {

            while (resultado.next()) {
                Livro livro = new Livro(
                    resultado.getInt("id"),
                    resultado.getString("titulo"),
                    resultado.getString("autor"),
                    resultado.getInt("ano")
                );
                livros.add(livro);
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar livros: " + e.getMessage());
        }

        return livros;
    }

    public Livro buscarLivroPorId(int id) {
        String sql = "SELECT id, titulo, autor, ano FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);

            try (ResultSet resultado = comando.executeQuery()) {
                if (resultado.next()) {
                    return new Livro(
                        resultado.getInt("id"),
                        resultado.getString("titulo"),
                        resultado.getString("autor"),
                        resultado.getInt("ano")
                    );
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar livro por ID: " + e.getMessage());
        }

        return null;
    }

    // === NOVO MÉTODOS DA AULA 44 (PARTE 18) ===
    public List<Livro> buscarLivrosPorTitulo(String titulo) {
        List<Livro> livros = new ArrayList<>();

        String sql = "SELECT id, titulo, autor, ano " +
                     "FROM livros " +
                     "WHERE titulo LIKE ? " +
                     "ORDER BY titulo";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, "%" + titulo + "%");

            try (ResultSet resultado = comando.executeQuery()) {
                while (resultado.next()) {
                    Livro livro = new Livro(
                        resultado.getInt("id"),
                        resultado.getString("titulo"),
                        resultado.getString("autor"),
                        resultado.getInt("ano")
                    );
                    livros.add(livro);
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar livros por título: " + e.getMessage());
        }

        return livros;
    }
}