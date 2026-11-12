import java.awt.image.BufferedImage;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.UUID;
import javax.imageio.ImageIO;

public class ImagemUsuario {

    public static String salvar(Path origem, int idUsuario) throws IOException {
        BufferedImage imagem = ImageIO.read(origem.toFile());

        if (imagem == null) {
            throw new IOException("Arquivo de imagem inválido.");
        }

        if (Files.size(origem) > 5 * 1024 * 1024) {
            throw new IOException("A imagem deve ter até 5 MB.");
        }

        String nome = idUsuario + "-" + UUID.randomUUID() + ".png";
        Path pasta = Path.of("imagens", "usuarios");
        Files.createDirectories(pasta);

        Path destino = pasta.resolve(nome);

        if (!ImageIO.write(imagem, "png", destino.toFile())) {
            throw new IOException("Não foi possível salvar a fotografia.");
        }

        return destino.toString().replace('\\', '/');
    }
}