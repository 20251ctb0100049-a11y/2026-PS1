import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import java.awt.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    private final DefaultTableModel modelo;
    private final JTable tabela;

    private final JTextField campoId = new JTextField(6);
    private final JTextField campoTitulo = new JTextField(16);
    private final JLabel status = new JLabel("Pronto.");

    // Paleta de cores (Modelo 1 - Clássico Administrativo)
    private final Color COR_PRIMARIA = new Color(30, 58, 138);
    private final Color COR_DESTAQUE = new Color(15, 118, 110);
    private final Color COR_FUNDO = new Color(248, 250, 252);
    private final Color COR_LINHA_PAR = Color.WHITE;
    private final Color COR_LINHA_IMPAR = new Color(241, 245, 249);
    private final Color COR_SELECAO = new Color(191, 219, 254);
    private final Color COR_TEXTO = new Color(30, 41, 59);

    public TelaLivros() {
        setTitle("BiblioTech | Gerenciamento de Livros");
        setSize(1080, 580);
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

        // Painel de controles
        JPanel controles = new JPanel(new FlowLayout(FlowLayout.LEFT, 8, 10));
        controles.setBackground(COR_FUNDO);
        controles.setBorder(new EmptyBorder(4, 8, 4, 8));

        JButton buscarId = criarBotao("Buscar ID", COR_PRIMARIA, Color.WHITE);
        JButton buscarTitulo = criarBotao("Buscar Título", COR_PRIMARIA, Color.WHITE);
        JButton limparCampos = criarBotao("Limpar", new Color(226, 232, 240), COR_TEXTO);
        JButton mostrarTodos = criarBotao("Mostrar Todos", new Color(226, 232, 240), COR_TEXTO);
        JButton botaoCapa = criarBotao("Selecionar capa", COR_DESTAQUE, Color.WHITE);

        Font fonteCampo = new Font("SansSerif", Font.PLAIN, 14);
        campoId.setFont(fonteCampo);
        campoTitulo.setFont(fonteCampo);

        controles.add(criarLabel("ID:"));
        controles.add(campoId);
        controles.add(buscarId);

        controles.add(Box.createHorizontalStrut(6));

        controles.add(criarLabel("Título:"));
        controles.add(campoTitulo);
        controles.add(buscarTitulo);

        controles.add(Box.createHorizontalStrut(6));

        controles.add(limparCampos);
        controles.add(mostrarTodos);

        controles.add(Box.createHorizontalStrut(6));
        controles.add(botaoCapa);

        painelSuperior.add(controles, BorderLayout.CENTER);
        add(painelSuperior, BorderLayout.NORTH);

        // 2. Configuração do Modelo e JTable
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

        tabela.getColumnModel().getColumn(0).setPreferredWidth(50);   // ID
        tabela.getColumnModel().getColumn(1).setPreferredWidth(110);  // Capa
        tabela.getColumnModel().getColumn(2).setPreferredWidth(350);  // Título
        tabela.getColumnModel().getColumn(3).setPreferredWidth(250);  // Autor
        tabela.getColumnModel().getColumn(4).setPreferredWidth(80);   // Ano

        DefaultTableCellRenderer renderizador = new DefaultTableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(
                    JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {

                Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);

                if (!isSelected) {
                    c.setBackground(row % 2 == 0 ? COR_LINHA_PAR : COR_LINHA_IMPAR);
                }

                if (column == 0 || column == 1 || column == 4) {
                    setHorizontalAlignment(SwingConstants.CENTER);
                } else {
                    setHorizontalAlignment(SwingConstants.LEFT);
                }

                if (column == 1) {
                    if (value instanceof Icon) {
                        setIcon((Icon) value);
                        setText("");
                    } else {
                        setIcon(null);
                        String textoCapa = (value != null) ? value.toString() : "Sem capa";
                        setText(textoCapa);
                        if ("Sem capa".equals(textoCapa)) {
                            setFont(new Font("SansSerif", Font.ITALIC, 12));
                            setForeground(new Color(100, 116, 139));
                        } else {
                            setFont(new Font("SansSerif", Font.BOLD, 12));
                            setForeground(COR_DESTAQUE);
                        }
                    }
                } else {
                    setIcon(null);
                    setFont(new Font("SansSerif", column == 2 ? Font.BOLD : Font.PLAIN, 14));
                    setForeground(COR_TEXTO);
                }

                setBorder(new EmptyBorder(0, 8, 0, 8));
                return c;
            }
        };

        for (int i = 0; i < tabela.getColumnCount(); i++) {
            tabela.getColumnModel().getColumn(i).setCellRenderer(renderizador);
        }

        JScrollPane scrollPane = new JScrollPane(tabela);
        scrollPane.setBorder(new EmptyBorder(0, 12, 0, 12));
        scrollPane.getViewport().setBackground(Color.WHITE);
        add(scrollPane, BorderLayout.CENTER);

        // 3. Barra de Status Inferior
        status.setFont(new Font("SansSerif", Font.PLAIN, 13));
        status.setForeground(COR_TEXTO);
        status.setBorder(new EmptyBorder(6, 14, 10, 14));
        add(status, BorderLayout.SOUTH);

        // 4. Eventos
        buscarId.addActionListener(e -> buscarLivroPorId());
        campoId.addActionListener(e -> buscarLivroPorId());

        buscarTitulo.addActionListener(e -> buscarPorTitulo());
        campoTitulo.addActionListener(e -> buscarPorTitulo());

        limparCampos.addActionListener(e -> limparPesquisa());
        mostrarTodos.addActionListener(e -> carregarLivros());
        botaoCapa.addActionListener(e -> selecionarCapa());

        carregarLivros();
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

    private void carregarLivros() {
        modelo.setRowCount(0);
        List<Livro> livros = dao.listarLivros();

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText("Livros apresentados: " + livros.size());
    }

    private void adicionarLinha(Livro livro) {
        String infoCapa = (livro.getCapa() != null && !livro.getCapa().isBlank())
                ? "Capa cadastrada"
                : "Sem capa";

        modelo.addRow(new Object[]{
            livro.getId(),
            infoCapa,
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        });
    }

    private void selecionarCapa() {
        int linha = tabela.getSelectedRow();

        if (linha == -1) {
            JOptionPane.showMessageDialog(
                this,
                "Selecione um livro na tabela."
            );
            return;
        }

        int linhaModelo = tabela.convertRowIndexToModel(linha);
        int id = (int) modelo.getValueAt(linhaModelo, 0);

        JFileChooser seletor = new JFileChooser();
        seletor.setDialogTitle("Selecione a capa do livro");
        seletor.setFileFilter(
            new FileNameExtensionFilter(
                "Imagens JPG e PNG", "jpg", "jpeg", "png"
            )
        );

        if (seletor.showOpenDialog(this) != JFileChooser.APPROVE_OPTION) {
            return;
        }

        Path destino = null;

        try {
            destino = Path.of(
                ImagemLivro.salvar(
                    seletor.getSelectedFile().toPath(),
                    id
                )
            );

            boolean atualizado = dao.atualizarCapa(
                id, destino.toString().replace('\\', '/')
            );

            if (!atualizado) {
                Files.deleteIfExists(destino);
                JOptionPane.showMessageDialog(
                    this,
                    "Não foi possível atualizar o livro."
                );
                return;
            }

            carregarLivros();

            JOptionPane.showMessageDialog(
                this,
                "Capa salva com sucesso!"
            );

        } catch (Exception ex) {
            if (destino != null) {
                try {
                    Files.deleteIfExists(destino);
                } catch (IOException ignorado) {
                }
            }

            JOptionPane.showMessageDialog(
                this,
                "Erro ao salvar capa: " + ex.getMessage()
            );
        }
    }

    private void buscarLivroPorId() {
        String texto = campoId.getText().trim();
        int id;

        try {
            id = Integer.parseInt(texto);
            if (id <= 0) throw new NumberFormatException();
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(
                this,
                "Informe um ID inteiro positivo.",
                "Entrada inválida",
                JOptionPane.WARNING_MESSAGE
            );
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
            JOptionPane.showMessageDialog(
                this,
                "Informe o título do livro.",
                "Campo obrigatório",
                JOptionPane.WARNING_MESSAGE
            );
            return;
        }

        List<Livro> livros = dao.buscarLivrosPorTitulo(titulo);
        modelo.setRowCount(0);

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText("Livros encontrados: " + livros.size());

        if (livros.isEmpty()) {
            JOptionPane.showMessageDialog(
                this,
                "Nenhum livro encontrado.",
                "Resultado da Pesquisa",
                JOptionPane.INFORMATION_MESSAGE
            );
        }
    }

    private void limparPesquisa() {
        campoId.setText("");
        campoTitulo.setText("");
        carregarLivros();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new TelaLivros().setVisible(true);
        });
    }
}