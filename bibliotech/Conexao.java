import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexao {

    public static Connection conectar() throws SQLException {
        ConfiguracaoBanco config = ConfiguracaoBanco.getInstancia();

        if (config.getUsuario() == null ||
                config.getUsuario().isBlank() ||
                config.getSenha() == null) {

            throw new SQLException("Configure DB_USER e DB_PASSWORD.");
        }

        return DriverManager.getConnection(
            config.getUrl(),
            config.getUsuario(),
            config.getSenha()
        );
    }
}