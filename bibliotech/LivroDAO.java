import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class LivroDAO {

    public List<Livro> listarLivros() {
        List<Livro> livros = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros ORDER BY id";

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
                livro.setCapa(resultado.getString("capa"));
                livros.add(livro);
            }

        } catch (SQLException e) {
            throw new PersistenciaException(
                "Não foi possível consultar os livros.",
                e
            );
        }

        return livros;
    }

    public Livro buscarLivroPorId(int id) {
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);

            try (ResultSet resultado = comando.executeQuery()) {
                if (resultado.next()) {
                    Livro livro = new Livro(
                        resultado.getInt("id"),
                        resultado.getString("titulo"),
                        resultado.getString("autor"),
                        resultado.getInt("ano")
                    );
                    livro.setCapa(resultado.getString("capa"));
                    return livro;
                }
            }

        } catch (SQLException e) {
            throw new PersistenciaException(
                "Não foi possível consultar o livro pelo ID.",
                e
            );
        }

        return null;
    }

    public List<Livro> buscarLivrosPorTitulo(String titulo) {
        List<Livro> livros = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa " +
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
                    livro.setCapa(resultado.getString("capa"));
                    livros.add(livro);
                }
            }

        } catch (SQLException e) {
            throw new PersistenciaException(
                "Não foi possível consultar os livros pelo título.",
                e
            );
        }

        return livros;
    }

    public boolean atualizarCapa(int id, String caminho) {
        String sql = "UPDATE livros SET capa = ? WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, caminho);
            comando.setInt(2, id);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            throw new PersistenciaException(
                "Não foi possível atualizar a capa do livro.",
                e
            );
        }
    }

    // ACRÉSCIMO DA PARTE 22: Validação de regras de negócio antes de inserir no banco
    public int inserirLivro(Livro livro) throws LivroInvalidoException {
        ValidadorLivro.validar(
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        );

        String sql = "INSERT INTO livros (titulo, autor, ano, capa) VALUES (?, ?, ?, ?)";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            comando.setString(1, livro.getTitulo());
            comando.setString(2, livro.getAutor());
            comando.setInt(3, livro.getAno());
            comando.setString(4, livro.getCapa());

            int afetadas = comando.executeUpdate();
            if (afetadas > 0) {
                try (ResultSet chaves = comando.getGeneratedKeys()) {
                    if (chaves.next()) {
                        return chaves.getInt(1);
                    }
                }
            }

        } catch (SQLException e) {
            throw new PersistenciaException(
                "Não foi possível cadastrar o livro.",
                e
            );
        }

        return -1;
    }
}