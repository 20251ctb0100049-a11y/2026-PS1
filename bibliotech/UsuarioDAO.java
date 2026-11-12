import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UsuarioDAO {

    public boolean atualizarFotoUsuario(int id, String caminho) {
        String sql = "UPDATE usuarios SET foto = ? WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, caminho);
            comando.setInt(2, id);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar foto: " + e.getMessage());
            return false;
        }
    }

    public String[] buscarUsuario(int id) {
        String sql = "SELECT nome, perfil, foto FROM usuarios WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);

            try (ResultSet rs = comando.executeQuery()) {
                if (rs.next()) {
                    return new String[]{
                        rs.getString("nome"),
                        rs.getString("perfil"),
                        rs.getString("foto")
                    };
                }
            }
        } catch (SQLException e) {
            System.out.println("Erro ao buscar usuário: " + e.getMessage());
        }
        return null;
    }
}