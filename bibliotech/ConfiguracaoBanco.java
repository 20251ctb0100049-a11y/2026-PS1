public final class ConfiguracaoBanco {

    private static final ConfiguracaoBanco INSTANCIA = new ConfiguracaoBanco();

    private final String url;
    private final String usuario;
    private final String senha;

    private ConfiguracaoBanco() {
        url = "jdbc:mariadb://localhost:3306/bibliotech";
        usuario = System.getenv("DB_USER");
        senha = System.getenv("DB_PASSWORD");
    }

    public static ConfiguracaoBanco getInstancia() {
        return INSTANCIA;
    }

    public String getUrl() {
        return url;
    }

    public String getUsuario() {
        return usuario;
    }

    public String getSenha() {
        return senha;
    }
}