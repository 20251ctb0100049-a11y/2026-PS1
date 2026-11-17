import java.sql.Connection;
import java.sql.SQLException;

public class TesteConfiguracaoBanco {

    public static void main(String[] args) {

        ConfiguracaoBanco a = ConfiguracaoBanco.getInstancia();
        ConfiguracaoBanco b = ConfiguracaoBanco.getInstancia();

        System.out.println("Mesma instância: " + (a == b));
        System.out.println("URL: " + a.getUrl());

        try (Connection conexao = Conexao.conectar()) {
            System.out.println("Conexão realizada com sucesso!");

        } catch (SQLException e) {
            System.out.println("Falha na conexão: " + e.getMessage());
        }
    }
}