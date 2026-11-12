import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;

public class TelaPerfil extends JFrame {

    private final UsuarioDAO usuarioDAO = new UsuarioDAO();
    private final int idUsuario = 1;

    private final JLabel lblAvatar = new JLabel("👤", SwingConstants.CENTER);
    private final JLabel lblNome = new JLabel("Ana Silva", SwingConstants.CENTER);
    private final JLabel lblPerfil = new JLabel("Leitora cadastrada", SwingConstants.CENTER);
    private final JLabel lblEmprestimos = new JLabel("Livros emprestados: 2", SwingConstants.CENTER);

    private final Color COR_PRIMARIA = new Color(30, 58, 138);
    private final Color COR_DESTAQUE = new Color(15, 118, 110);
    private final Color COR_FUNDO = new Color(248, 250, 252);
    private final Color COR_TEXTO = new Color(30, 41, 59);

    public TelaPerfil() {
        setTitle("BiblioTech | Meu Perfil");
        setSize(420, 480);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        getContentPane().setBackground(COR_FUNDO);
        setLayout(new BorderLayout(10, 10));

        // Cabeçalho
        JLabel banner = new JLabel("  👤 BiblioTech | Meu Perfil");
        banner.setFont(new Font("SansSerif", Font.BOLD, 18));
        banner.setForeground(Color.WHITE);
        banner.setOpaque(true);
        banner.setBackground(COR_PRIMARIA);
        banner.setBorder(new EmptyBorder(12, 10, 12, 10));
        add(banner, BorderLayout.NORTH);

        // Cartão Central
        JPanel cartao = new JPanel();
        cartao.setLayout(new BoxLayout(cartao, BoxLayout.Y_AXIS));
        cartao.setBackground(Color.WHITE);
        cartao.setBorder(BorderFactory.createCompoundBorder(
            new EmptyBorder(20, 30, 20, 30),
            new LineBorder(new Color(226, 232, 240), 1, true)
        ));

        lblAvatar.setPreferredSize(new Dimension(130, 130));
        lblAvatar.setMaximumSize(new Dimension(130, 130));
        lblAvatar.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblAvatar.setFont(new Font("SansSerif", Font.PLAIN, 48));
        lblAvatar.setOpaque(true);
        lblAvatar.setBackground(new Color(241, 245, 249));
        lblAvatar.setBorder(new LineBorder(new Color(203, 213, 225), 2));

        lblNome.setFont(new Font("SansSerif", Font.BOLD, 20));
        lblNome.setForeground(COR_TEXTO);
        lblNome.setAlignmentX(Component.CENTER_ALIGNMENT);

        lblPerfil.setFont(new Font("SansSerif", Font.PLAIN, 14));
        lblPerfil.setForeground(new Color(100, 116, 139));
        lblPerfil.setAlignmentX(Component.CENTER_ALIGNMENT);

        lblEmprestimos.setFont(new Font("SansSerif", Font.BOLD, 14));
        lblEmprestimos.setForeground(COR_DESTAQUE);
        lblEmprestimos.setAlignmentX(Component.CENTER_ALIGNMENT);

        JButton btnAlterarFoto = new JButton("Alterar fotografia");
        btnAlterarFoto.setFont(new Font("SansSerif", Font.BOLD, 14));
        btnAlterarFoto.setBackground(COR_PRIMARIA);
        btnAlterarFoto.setForeground(Color.WHITE);
        btnAlterarFoto.setFocusPainted(false);
        btnAlterarFoto.setAlignmentX(Component.CENTER_ALIGNMENT);
        btnAlterarFoto.setCursor(new Cursor(Cursor.HAND_CURSOR));

        cartao.add(Box.createVerticalStrut(20));
        cartao.add(lblAvatar);
        cartao.add(Box.createVerticalStrut(16));
        cartao.add(lblNome);
        cartao.add(Box.createVerticalStrut(6));
        cartao.add(lblPerfil);
        cartao.add(Box.createVerticalStrut(12));
        cartao.add(lblEmprestimos);
        cartao.add(Box.createVerticalStrut(22));
        cartao.add(btnAlterarFoto);
        cartao.add(Box.createVerticalStrut(20));

        add(cartao, BorderLayout.CENTER);

        btnAlterarFoto.addActionListener(e -> alterarFotografia());

        carregarDadosUsuario();
    }

    private void carregarDadosUsuario() {
        String[] dados = usuarioDAO.buscarUsuario(idUsuario);
        if (dados != null) {
            lblNome.setText(dados[0]);
            lblPerfil.setText(dados[1]);
            exibirFoto(dados[2]);
        }
    }

    private void exibirFoto(String caminho) {
        if (caminho == null || caminho.isBlank()) return;
        File arquivo = new File(caminho);
        if (!arquivo.isFile()) return;

        try {
            BufferedImage img = ImageIO.read(arquivo);
            if (img != null) {
                Image reduzida = img.getScaledInstance(130, 130, Image.SCALE_SMOOTH);
                lblAvatar.setIcon(new ImageIcon(reduzida));
                lblAvatar.setText("");
            }
        } catch (Exception ignored) {
        }
    }

    private void alterarFotografia() {
        JFileChooser seletor = new JFileChooser();
        seletor.setDialogTitle("Selecione a fotografia do perfil");
        seletor.setFileFilter(new FileNameExtensionFilter("Imagens JPG e PNG", "jpg", "jpeg", "png"));

        if (seletor.showOpenDialog(this) != JFileChooser.APPROVE_OPTION) return;

        File arquivoSelecionado = seletor.getSelectedFile();

        // Desafio adicional: Prévia da imagem antes de salvar
        try {
            BufferedImage imgPrevia = ImageIO.read(arquivoSelecionado);
            if (imgPrevia == null) {
                JOptionPane.showMessageDialog(this, "Arquivo inválido.");
                return;
            }
            JLabel previa = new JLabel(new ImageIcon(imgPrevia.getScaledInstance(120, 120, Image.SCALE_SMOOTH)));
            int confirma = JOptionPane.showConfirmDialog(
                this,
                previa,
                "Confirmar nova fotografia?",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.PLAIN_MESSAGE
            );
            if (confirma != JOptionPane.YES_OPTION) return;
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Erro ao carregar prévia.");
            return;
        }

        Path destino = null;
        try {
            destino = Path.of(ImagemUsuario.salvar(arquivoSelecionado.toPath(), idUsuario));
            if (usuarioDAO.atualizarFotoUsuario(idUsuario, destino.toString().replace('\\', '/'))) {
                exibirFoto(destino.toString());
                JOptionPane.showMessageDialog(this, "Fotografia atualizada com sucesso!");
            } else {
                Files.deleteIfExists(destino);
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Erro: " + ex.getMessage());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaPerfil().setVisible(true));
    }
}