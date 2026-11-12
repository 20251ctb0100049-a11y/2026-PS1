import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    private final DefaultTableModel modelo;
    private final JTable tabela;

    private final JTextField campoId = new JTextField(5);
    private final JTextField campoTitulo = new JTextField(14);
    private final JLabel status = new JLabel("Pronto.");

    // Componentes do Painel de Detalhes (Etapa 3)
    private final JLabel lblCapaGrande = new JLabel("Sem capa", SwingConstants.CENTER);
    private final JLabel lblDetalheTitulo = new JLabel("Selecione um livro");
    private final JLabel lblDetalheAutor = new JLabel("-");
    private final JLabel lblDetalheAno = new JLabel("-");

    // Paleta de cores (Modelo 1)
    private final Color COR_PRIMARIA = new Color(30, 58, 138);
    private final Color COR_DESTAQUE = new Color(15, 118, 110);
    private final Color COR_FUNDO = new Color(248, 250, 252);
    private final Color COR_LINHA_PAR = Color.WHITE;
    private final Color COR_LINHA_IMPAR = new Color(241, 245, 249);
    private final Color COR_SELECAO = new Color(191, 219, 254);
    private final Color COR_TEXTO = new Color(30, 41, 59);

    public TelaLivros() {
        setTitle("BiblioTech | Gerenciamento de Livros");
        setSize(1160, 600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        getContentPane().setBackground(COR_FUNDO);
        setLayout(new BorderLayout(10, 10));

        // 1. Cabeçalho Superior + Barra de Pesquisa
        JPanel painelSuperior = new JPanel(new BorderLayout());
        painelSuperior.setBackground(COR_FUNDO);

        JLabel tituloBanner = new JLabel("  📚 BiblioTech | Gerenciamento de Livros");
        tituloBanner.setFont(new Font("SansSerif", Font.BOLD, 18));
        tituloBanner.setForeground(Color.WHITE);
        tituloBanner.setOpaque(true);
        tituloBanner.setBackground(COR_PRIMARIA);
        tituloBanner.setBorder(new EmptyBorder(12, 10, 12, 10));
        painelSuperior.add(tituloBanner, BorderLayout.NORTH);

        JPanel controles = new JPanel(new FlowLayout(FlowLayout.LEFT, 8, 10));
        controles.setBackground(COR_FUNDO);
        controles.setBorder(new EmptyBorder(4, 8, 4, 8));

        JButton buscarId = criarBotao("Buscar ID", COR_PRIMARIA, Color.WHITE);
        JButton buscarTitulo = criarBotao("Buscar Título", COR_PRIMARIA, Color.WHITE);
        JButton limparCampos = criarBotao("Limpar", new Color(226, 232, 240), COR_TEXTO);
        JButton mostrarTodos = criarBotao("Mostrar Todos", new Color(226, 232, 240), COR_TEXTO);
        JButton botaoCapa = criarBotao("Selecionar capa", COR_DESTAQUE, Color.WHITE);
        JButton botaoPerfil = criarBotao("👤 Meu Perfil", new Color(71, 85, 105), Color.WHITE);

        Font fonteCampo = new Font("SansSerif", Font.PLAIN, 14);
        campoId.setFont(fonteCampo);
        campoTitulo.setFont(fonteCampo);

        controles.add(criarLabel("ID:"));
        controles.add(campoId);
        controles.add(buscarId);
        controles.add(Box.createHorizontalStrut(4));
        controles.add(criarLabel("Título:"));
        controles.add(campoTitulo);
        controles.add(buscarTitulo);
        controles.add(Box.createHorizontalStrut(4));
        controles.add(limparCampos);
        controles.add(mostrarTodos);
        controles.add(Box.createHorizontalStrut(4));
        controles.add(botaoCapa);
        controles.add(botaoPerfil);

        painelSuperior.add(controles, BorderLayout.CENTER);
        add(painelSuperior, BorderLayout.NORTH);

        // 2. Tabela Central
        modelo = new DefaultTableModel(
            new Object[]{"ID", "Capa", "Título", "Autor", "Ano"}, 0
        ) {
            @Override
            public boolean isCellEditable(int linha, int coluna) {
                return false;
            }
        };

        tabela = new JTable(modelo);
        tabela.setRowHeight(85);
        tabela.setFont(new Font("SansSerif", Font.PLAIN, 14));
        tabela.setForeground(COR_TEXTO);
        tabela.setSelectionBackground(COR_SELECAO);
        tabela.setSelectionForeground(COR_TEXTO);
        tabela.setGridColor(new Color(226, 232, 240));
        tabela.setShowVerticalLines(false);
        tabela.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        JTableHeader header = tabela.getTableHeader();
        header.setFont(new Font("SansSerif", Font.BOLD, 14));
        header.setBackground(new Color(226, 232, 240));
        header.setForeground(COR_TEXTO);
        header.setPreferredSize(new Dimension(header.getWidth(), 36));

        tabela.getColumnModel().getColumn(0).setPreferredWidth(45);
        tabela.getColumnModel().getColumn(1).setPreferredWidth(85);
        tabela.getColumnModel().getColumn(2).setPreferredWidth(300);
        tabela.getColumnModel().getColumn(3).setPreferredWidth(220);
        tabela.getColumnModel().getColumn(4).setPreferredWidth(70);

        DefaultTableCellRenderer renderizadorTexto = new DefaultTableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(
                    JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
                Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                if (!isSelected) {
                    c.setBackground(row % 2 == 0 ? COR_LINHA_PAR : COR_LINHA_IMPAR);
                }
                setHorizontalAlignment((column == 0 || column == 4) ? SwingConstants.CENTER : SwingConstants.LEFT);
                setFont(new Font("SansSerif", column == 2 ? Font.BOLD : Font.PLAIN, 14));
                setForeground(COR_TEXTO);
                setBorder(new EmptyBorder(0, 8, 0, 8));
                return c;
            }
        };

        for (int i = 0; i < tabela.getColumnCount(); i++) {
            if (i != 1) {
                tabela.getColumnModel().getColumn(i).setCellRenderer(renderizadorTexto);
            }
        }

        tabela.getColumnModel().getColumn(1).setCellRenderer(
            new DefaultTableCellRenderer() {
                @Override
                public Component getTableCellRendererComponent(
                        JTable tabela, Object valor, boolean selecionada, boolean foco, int linha, int coluna) {
                    JLabel label = new JLabel();
                    label.setHorizontalAlignment(JLabel.CENTER);
                    label.setOpaque(true);
                    label.setBackground(selecionada ? tabela.getSelectionBackground() : (linha % 2 == 0 ? COR_LINHA_PAR : COR_LINHA_IMPAR));

                    if (valor instanceof ImageIcon) {
                        label.setIcon((ImageIcon) valor);
                    } else {
                        label.setText("Sem capa");
                        label.setFont(new Font("SansSerif", Font.ITALIC, 12));
                        label.setForeground(new Color(100, 116, 139));
                    }
                    return label;
                }
            }
        );

        JScrollPane scrollPane = new JScrollPane(tabela);
        scrollPane.setBorder(new EmptyBorder(0, 12, 0, 6));
        scrollPane.getViewport().setBackground(Color.WHITE);
        add(scrollPane, BorderLayout.CENTER);

        // 3. Painel Lateral de Detalhes do Livro Selecionado (Etapa 3)
        JPanel painelDetalhes = new JPanel();
        painelDetalhes.setLayout(new BoxLayout(painelDetalhes, BoxLayout.Y_AXIS));
        painelDetalhes.setPreferredSize(new Dimension(240, 0));
        painelDetalhes.setBackground(Color.WHITE);
        painelDetalhes.setBorder(BorderFactory.createCompoundBorder(
            new EmptyBorder(0, 6, 0, 12),
            new LineBorder(new Color(226, 232, 240), 1, true)
        ));

        JLabel tituloPainel = new JLabel("Detalhes do Livro");
        tituloPainel.setFont(new Font("SansSerif", Font.BOLD, 15));
        tituloPainel.setForeground(COR_PRIMARIA);
        tituloPainel.setAlignmentX(Component.CENTER_ALIGNMENT);

        lblCapaGrande.setPreferredSize(new Dimension(120, 160));
        lblCapaGrande.setMaximumSize(new Dimension(120, 160));
        lblCapaGrande.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblCapaGrande.setOpaque(true);
        lblCapaGrande.setBackground(new Color(241, 245, 249));
        lblCapaGrande.setForeground(new Color(100, 116, 139));
        lblCapaGrande.setBorder(new LineBorder(new Color(203, 213, 225), 1));

        lblDetalheTitulo.setFont(new Font("SansSerif", Font.BOLD, 14));
        lblDetalheTitulo.setForeground(COR_TEXTO);
        lblDetalheTitulo.setAlignmentX(Component.CENTER_ALIGNMENT);

        lblDetalheAutor.setFont(new Font("SansSerif", Font.PLAIN, 13));
        lblDetalheAutor.setForeground(new Color(71, 85, 105));
        lblDetalheAutor.setAlignmentX(Component.CENTER_ALIGNMENT);

        lblDetalheAno.setFont(new Font("SansSerif", Font.BOLD, 13));
        lblDetalheAno.setForeground(COR_DESTAQUE);
        lblDetalheAno.setAlignmentX(Component.CENTER_ALIGNMENT);

        painelDetalhes.add(Box.createVerticalStrut(18));
        painelDetalhes.add(tituloPainel);
        painelDetalhes.add(Box.createVerticalStrut(16));
        painelDetalhes.add(lblCapaGrande);
        painelDetalhes.add(Box.createVerticalStrut(16));
        painelDetalhes.add(lblDetalheTitulo);
        painelDetalhes.add(Box.createVerticalStrut(6));
        painelDetalhes.add(lblDetalheAutor);
        painelDetalhes.add(Box.createVerticalStrut(6));
        painelDetalhes.add(lblDetalheAno);

        add(painelDetalhes, BorderLayout.EAST);

        // 4. Barra de Status Inferior
        status.setFont(new Font("SansSerif", Font.PLAIN, 13));
        status.setForeground(COR_TEXTO);
        status.setBorder(new EmptyBorder(6, 14, 10, 14));
        add(status, BorderLayout.SOUTH);

        // 5. Eventos
        tabela.getSelectionModel().addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                atualizarPainelDetalhes();
            }
        });

        buscarId.addActionListener(e -> buscarLivroPorId());
        campoId.addActionListener(e -> buscarLivroPorId());
        buscarTitulo.addActionListener(e -> buscarPorTitulo());
        campoTitulo.addActionListener(e -> buscarPorTitulo());
        limparCampos.addActionListener(e -> limparPesquisa());
        mostrarTodos.addActionListener(e -> carregarLivros());
        botaoCapa.addActionListener(e -> selecionarCapa());
        botaoPerfil.addActionListener(e -> new TelaPerfil().setVisible(true));

        carregarLivros();
    }

    private void atualizarPainelDetalhes() {
        int linha = tabela.getSelectedRow();
        if (linha == -1) {
            lblCapaGrande.setIcon(null);
            lblCapaGrande.setText("Sem capa");
            lblDetalheTitulo.setText("Selecione um livro");
            lblDetalheAutor.setText("-");
            lblDetalheAno.setText("-");
            return;
        }

        int linhaModelo = tabela.convertRowIndexToModel(linha);
        int id = (int) modelo.getValueAt(linhaModelo, 0);
        Livro livro = dao.buscarLivroPorId(id);

        if (livro != null) {
            lblDetalheTitulo.setText("<html><center>" + livro.getTitulo() + "</center></html>");
            lblDetalheAutor.setText(livro.getAutor());
            lblDetalheAno.setText("Ano: " + livro.getAno());

            ImageIcon grande = carregarImagemRedimensionada(livro.getCapa(), 120, 160);
            if (grande != null) {
                lblCapaGrande.setIcon(grande);
                lblCapaGrande.setText("");
            } else {
                lblCapaGrande.setIcon(null);
                lblCapaGrande.setText("Sem capa");
            }
        }
    }

    private JLabel criarLabel(String texto) {
        JLabel label = new JLabel(texto);
        label.setFont(new Font("SansSerif", Font.BOLD, 14));
        label.setForeground(COR_TEXTO);
        return label;
    }

    private JButton criarBotao(String texto, Color fundo, Color textoCor) {
        JButton botao = new JButton(texto);
        botao.setFont(new Font("SansSerif", Font.BOLD, 13));
        botao.setBackground(fundo);
        botao.setForeground(textoCor);
        botao.setFocusPainted(false);
        botao.setCursor(new Cursor(Cursor.HAND_CURSOR));
        return botao;
    }

    private ImageIcon carregarImagemRedimensionada(String caminho, int largura, int altura) {
        if (caminho == null || caminho.isBlank()) return null;
        File arquivo = new File(caminho);
        if (!arquivo.isFile()) return null;

        try {
            BufferedImage imagem = ImageIO.read(arquivo);
            if (imagem == null) return null;
            return new ImageIcon(imagem.getScaledInstance(largura, altura, Image.SCALE_SMOOTH));
        } catch (IOException e) {
            return null;
        }
    }

    private void carregarLivros() {
        modelo.setRowCount(0);
        List<Livro> livros = dao.listarLivros();
        for (Livro livro : livros) {
            adicionarLinha(livro);
        }
        status.setText("Livros apresentados: " + livros.size());
    }

    private void adicionarLinha(Livro livro) {
        modelo.addRow(new Object[]{
            livro.getId(),
            carregarImagemRedimensionada(livro.getCapa(), 55, 75),
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        });
    }

    private void selecionarCapa() {
        int linha = tabela.getSelectedRow();
        if (linha == -1) {
            JOptionPane.showMessageDialog(this, "Selecione um livro na tabela.");
            return;
        }

        int linhaModelo = tabela.convertRowIndexToModel(linha);
        int id = (int) modelo.getValueAt(linhaModelo, 0);

        JFileChooser seletor = new JFileChooser();
        seletor.setDialogTitle("Selecione a capa do livro");
        seletor.setFileFilter(new FileNameExtensionFilter("Imagens JPG e PNG", "jpg", "jpeg", "png"));

        if (seletor.showOpenDialog(this) != JFileChooser.APPROVE_OPTION) return;

        File arquivoSelecionado = seletor.getSelectedFile();

        // Desafio adicional: Prévia da imagem selecionada antes de salvá-la
        ImageIcon iconePrevia = carregarImagemRedimensionada(arquivoSelecionado.getAbsolutePath(), 120, 160);
        if (iconePrevia != null) {
            JLabel previa = new JLabel(iconePrevia);
            int resposta = JOptionPane.showConfirmDialog(
                this,
                previa,
                "Prévia da capa — Deseja salvar?",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.PLAIN_MESSAGE
            );
            if (resposta != JOptionPane.YES_OPTION) return;
        }

        Path destino = null;
        try {
            destino = Path.of(ImagemLivro.salvar(arquivoSelecionado.toPath(), id));
            boolean atualizado = dao.atualizarCapa(id, destino.toString().replace('\\', '/'));

            if (!atualizado) {
                Files.deleteIfExists(destino);
                JOptionPane.showMessageDialog(this, "Não foi possível atualizar o livro.");
                return;
            }

            carregarLivros();
            JOptionPane.showMessageDialog(this, "Capa salva com sucesso!");

        } catch (Exception ex) {
            if (destino != null) {
                try {
                    Files.deleteIfExists(destino);
                } catch (IOException ignorado) {
                }
            }
            JOptionPane.showMessageDialog(this, "Erro ao salvar capa: " + ex.getMessage());
        }
    }

    private void buscarLivroPorId() {
        String texto = campoId.getText().trim();
        int id;
        try {
            id = Integer.parseInt(texto);
            if (id <= 0) throw new NumberFormatException();
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Informe um ID inteiro positivo.", "Entrada inválida", JOptionPane.WARNING_MESSAGE);
            return;
        }

        Livro livro = dao.buscarLivroPorId(id);
        modelo.setRowCount(0);

        if (livro == null) {
            status.setText("Nenhum livro encontrado para o ID " + id);
            JOptionPane.showMessageDialog(this, "Livro não encontrado.");
        } else {
            adicionarLinha(livro);
            status.setText("Livro encontrado: " + livro.getTitulo());
        }
    }

    private void buscarPorTitulo() {
        String titulo = campoTitulo.getText().trim();
        if (titulo.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Informe o título do livro.", "Campo obrigatório", JOptionPane.WARNING_MESSAGE);
            return;
        }

        List<Livro> livros = dao.buscarLivrosPorTitulo(titulo);
        modelo.setRowCount(0);
        for (Livro livro : livros) {
            adicionarLinha(livro);
        }
        status.setText("Livros encontrados: " + livros.size());

        if (livros.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Nenhum livro encontrado.", "Resultado da Pesquisa", JOptionPane.INFORMATION_MESSAGE);
        }
    }

    private void limparPesquisa() {
        campoId.setText("");
        campoTitulo.setText("");
        carregarLivros();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaLivros().setVisible(true));
    }
}