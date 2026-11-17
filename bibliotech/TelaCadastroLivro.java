import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.nio.file.Path;

public class TelaCadastroLivro extends JFrame {

    private final LivroDAO dao = new LivroDAO();
    private final Runnable aoSalvarCallback;

    private final JTextField campoTitulo = new JTextField(20);
    private final JTextField campoAutor = new JTextField(20);
    private final JTextField campoAno = new JTextField(8);
    private final JLabel lblPrevia = new JLabel("Sem capa", SwingConstants.CENTER);

    private File arquivoCapaSelecionado = null;

    private final Color COR_PRIMARIA = new Color(30, 58, 138);
    private final Color COR_DESTAQUE = new Color(15, 118, 110);
    private final Color COR_FUNDO = new Color(248, 250, 252);
    private final Color COR_TEXTO = new Color(30, 41, 59);

    public TelaCadastroLivro(Runnable aoSalvarCallback) {
        this.aoSalvarCallback = aoSalvarCallback;

        setTitle("BiblioTech | Cadastro de Livro");
        setSize(560, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        getContentPane().setBackground(COR_FUNDO);
        setLayout(new BorderLayout(10, 10));

        // Cabeçalho
        JLabel banner = new JLabel("  📖 BiblioTech | Novo Livro");
        banner.setFont(new Font("SansSerif", Font.BOLD, 18));
        banner.setForeground(Color.WHITE);
        banner.setOpaque(true);
        banner.setBackground(COR_PRIMARIA);
        banner.setBorder(new EmptyBorder(12, 10, 12, 10));
        add(banner, BorderLayout.NORTH);

        // Painel Central (Formulário + Prévia)
        JPanel centro = new JPanel(new BorderLayout(16, 10));
        centro.setBackground(COR_FUNDO);
        centro.setBorder(new EmptyBorder(16, 20, 10, 20));

        // Campos à esquerda
        JPanel form = new JPanel(new GridLayout(6, 1, 4, 4));
        form.setBackground(COR_FUNDO);

        Font fonteLabel = new Font("SansSerif", Font.BOLD, 14);
        Font fonteCampo = new Font("SansSerif", Font.PLAIN, 14);

        JLabel lblTitulo = new JLabel("Título do Livro:");
        lblTitulo.setFont(fonteLabel);
        lblTitulo.setForeground(COR_TEXTO);
        campoTitulo.setFont(fonteCampo);

        JLabel lblAutor = new JLabel("Autor:");
        lblAutor.setFont(fonteLabel);
        lblAutor.setForeground(COR_TEXTO);
        campoAutor.setFont(fonteCampo);

        JLabel lblAno = new JLabel("Ano de Publicação:");
        lblAno.setFont(fonteLabel);
        lblAno.setForeground(COR_TEXTO);
        campoAno.setFont(fonteCampo);

        form.add(lblTitulo);
        form.add(campoTitulo);
        form.add(lblAutor);
        form.add(campoAutor);
        form.add(lblAno);
        form.add(campoAno);

        centro.add(form, BorderLayout.CENTER);

        // Prévia da capa à direita
        JPanel painelCapa = new JPanel();
        painelCapa.setLayout(new BoxLayout(painelCapa, BoxLayout.Y_AXIS));
        painelCapa.setBackground(COR_FUNDO);

        lblPrevia.setPreferredSize(new Dimension(120, 160));
        lblPrevia.setMaximumSize(new Dimension(120, 160));
        lblPrevia.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblPrevia.setOpaque(true);
        lblPrevia.setBackground(Color.WHITE);
        lblPrevia.setForeground(new Color(100, 116, 139));
        lblPrevia.setBorder(new LineBorder(new Color(203, 213, 225), 1));

        JButton btnEscolherCapa = new JButton("Escolher Capa");
        btnEscolherCapa.setFont(new Font("SansSerif", Font.BOLD, 12));
        btnEscolherCapa.setBackground(new Color(226, 232, 240));
        btnEscolherCapa.setForeground(COR_TEXTO);
        btnEscolherCapa.setFocusPainted(false);
        btnEscolherCapa.setAlignmentX(Component.CENTER_ALIGNMENT);

        painelCapa.add(lblPrevia);
        painelCapa.add(Box.createVerticalStrut(10));
        painelCapa.add(btnEscolherCapa);

        centro.add(painelCapa, BorderLayout.EAST);
        add(centro, BorderLayout.CENTER);

        // Rodapé com botões
        JPanel rodape = new JPanel(new FlowLayout(FlowLayout.RIGHT, 12, 12));
        rodape.setBackground(COR_FUNDO);

        JButton btnCancelar = new JButton("Cancelar");
        btnCancelar.setFont(new Font("SansSerif", Font.BOLD, 13));
        btnCancelar.setBackground(new Color(226, 232, 240));
        btnCancelar.setForeground(COR_TEXTO);

        JButton btnSalvar = new JButton("Salvar Livro");
        btnSalvar.setFont(new Font("SansSerif", Font.BOLD, 13));
        btnSalvar.setBackground(COR_DESTAQUE);
        btnSalvar.setForeground(Color.WHITE);

        rodape.add(btnCancelar);
        rodape.add(btnSalvar);
        add(rodape, BorderLayout.SOUTH);

        // Eventos
        btnEscolherCapa.addActionListener(e -> escolherCapa());
        btnCancelar.addActionListener(e -> dispose());
        btnSalvar.addActionListener(e -> salvarLivro());
    }

    private void escolherCapa() {
        JFileChooser seletor = new JFileChooser();
        seletor.setDialogTitle("Selecione a capa do livro");
        seletor.setFileFilter(new FileNameExtensionFilter("Imagens JPG e PNG", "jpg", "jpeg", "png"));

        if (seletor.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
            arquivoCapaSelecionado = seletor.getSelectedFile();
            try {
                BufferedImage img = ImageIO.read(arquivoCapaSelecionado);
                if (img != null) {
                    lblPrevia.setIcon(new ImageIcon(img.getScaledInstance(120, 160, Image.SCALE_SMOOTH)));
                    lblPrevia.setText("");
                }
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Erro ao carregar prévia.");
            }
        }
    }

    private void salvarLivro() {
        String titulo = campoTitulo.getText().trim();
        String autor = campoAutor.getText().trim();
        String anoTexto = campoAno.getText().trim();

        if (titulo.isEmpty() || autor.isEmpty() || anoTexto.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Preencha título, autor e ano.");
            return;
        }

        int ano;
        try {
            ano = Integer.parseInt(anoTexto);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Informe um ano válido.");
            return;
        }

        Livro novo = new Livro(0, titulo, autor, ano);
        int idGerado = dao.inserirLivro(novo);

        if (idGerado <= 0) {
            JOptionPane.showMessageDialog(this, "Erro ao gravar livro no MariaDB.");
            return;
        }

        if (arquivoCapaSelecionado != null) {
            try {
                String caminho = ImagemLivro.salvar(Path.of(arquivoCapaSelecionado.getAbsolutePath()), idGerado);
                dao.atualizarCapa(idGerado, caminho);
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Livro salvo, mas houve erro na capa: " + ex.getMessage());
            }
        }

        if (aoSalvarCallback != null) {
            aoSalvarCallback.run();
        }

        JOptionPane.showMessageDialog(this, "Livro cadastrado com sucesso!");
        dispose();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaCadastroLivro(null).setVisible(true));
    }
}