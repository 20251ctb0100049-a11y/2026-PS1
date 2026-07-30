package rafael;
public class Chamado {
    // Atributos privados (Encapsulamento)
    private int numero;
    private String descricao;
    private String prioridade; // Pode ser "BAIXA", "MEDIA", "ALTA"
    private boolean aberto;
    private String tecnicoResponsavel; // Desafio Complementar 1: Atributo adicional

    // Construtor completo
    public Chamado(int numero, String descricao, String prioridade) {
        if (!validarNumero(numero) || !validarDescricao(descricao) || !validarPrioridade(prioridade)) {
            throw new IllegalArgumentException("Dados inválidos fornecidos ao construtor.");
        }
        this.numero = numero;
        this.descricao = descricao;
        this.prioridade = prioridade.toUpperCase();
        this.aberto = true;
        this.tecnicoResponsavel = "Não atribuído";
    }

    // --- Validações (3 regras obrigatórias) ---
    private boolean validarNumero(int numero) {
        return numero > 0;
    }

    private boolean validarDescricao(String descricao) {
        return descricao != null && !descricao.trim().isEmpty();
    }

    private boolean validarPrioridade(String prioridade) {
        if (prioridade == null) return false;
        String p = prioridade.toUpperCase();
        return p.equals("BAIXA") || p.equals("MEDIA") || p.equals("ALTA");
    }

    // --- Métodos de Comportamento (Regras de Negócio) ---
    public boolean fechar() {
        if (!this.aberto) {
            System.out.println("❌ Falha: O chamado nº " + this.numero + " já está fechado.");
            return false;
        }
        this.aberto = false;
        System.out.println("✅ Chamado nº " + this.numero + " fechado com sucesso!");
        return true;
    }

    public boolean reabrir() {
        if (this.aberto) {
            System.out.println("❌ Falha: O chamado nº " + this.numero + " já está aberto.");
            return false;
        }
        this.aberto = true;
        System.out.println("✅ Chamado nº " + this.numero + " reaberto com sucesso!");
        return true;
    }

    public boolean alterarPrioridade(String novaPrioridade) {
        if (!validarPrioridade(novaPrioridade)) {
            System.out.println("❌ Falha: Prioridade '" + novaPrioridade + "' é inválida. Manteve: " + this.prioridade);
            return false;
        }
        this.prioridade = novaPrioridade.toUpperCase();
        System.out.println("✅ Prioridade do chamado nº " + this.numero + " alterada para: " + this.prioridade);
        return true;
    }

    // --- Desafio Complementar 2: Método de resumo textual ---
    public String gerarResumo() {
        return String.format("Chamado #%d | Descrição: '%s' | Prioridade: %s | Status: %s | Técnico: %s",
                numero, descricao, prioridade, (aberto ? "ABERTO" : "FECHADO"), tecnicoResponsavel);
    }

    // --- Getters e Setters Restritos ---
    public int getNumero() {
        return numero;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        if (validarDescricao(descricao)) {
            this.descricao = descricao;
            System.out.println("✅ Descrição do chamado nº " + this.numero + " atualizada.");
        } else {
            System.out.println("❌ Falha: Tentativa de atribuir descrição vazia ou nula recusada.");
        }
    }

    public String getPrioridade() {
        return prioridade;
    }

    public boolean isAberto() {
        return aberto;
    }

    public String getTecnicoResponsavel() {
        return tecnicoResponsavel;
    }

    public void setTecnicoResponsavel(String tecnicoResponsavel) {
        if (validarDescricao(tecnicoResponsavel)) {
            this.tecnicoResponsavel = tecnicoResponsavel;
        }
    }
}