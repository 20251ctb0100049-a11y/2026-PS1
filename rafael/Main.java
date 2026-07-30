package rafael;
public class Main {
    public static void main(String[] args) {
        System.out.println("=== EXECUÇÃO DOS CASOS DE TESTE (SysControl v2.0) ===\n");

        // TESTE 1: Criar objeto com dados válidos
        // Personalização: '7' (dia do nascimento) e 'RA' (iniciais)
        System.out.println("--- Teste 1: Criar objeto com dados válidos ---");
        Chamado c1 = new Chamado(7, "RA - Falha no servidor de banco de dados", "ALTA");
        Chamado c2 = new Chamado(102, "RA - Instalação de software IDE", "BAIXA");
        Chamado c3 = new Chamado(103, "Configuração de rede local", "MEDIA");
        System.out.println(c1.gerarResumo());
        System.out.println(c2.gerarResumo());
        System.out.println(c3.gerarResumo());
        System.out.println();

        // TESTE 2: Tentar atribuir texto vazio a um campo obrigatório
        System.out.println("--- Teste 2: Tentativa de alteração com texto vazio ---");
        c1.setDescricao(""); // Deve ser recusado
        System.out.println();

        // TESTE 3: Tentar alterar para uma prioridade inválida (Restrição)
        System.out.println("--- Teste 3: Tentativa de alterar prioridade com valor inválido ---");
        c1.alterarPrioridade("SUPER_URGENTE"); // Deve ser recusado pela validação
        System.out.println();

        // TESTE 4: Executar um comportamento permitido
        System.out.println("--- Teste 4: Executar um comportamento permitido ---");
        c1.fechar(); // Altera o estado do chamado c1
        System.out.println();

        // TESTE 5: Executar um comportamento impossível
        System.out.println("--- Teste 5: Executar um comportamento impossível ---");
        c1.fechar(); // Tentar fechar um chamado já fechado (Estado preservado)
        System.out.println();

        // EXIBIÇÃO DO ESTADO FINAL (sem acesso direto aos atributos)
        System.out.println("--- ESTADO FINAL DOS OBJETOS ---");
        System.out.println(c1.gerarResumo());
        System.out.println(c2.gerarResumo());
        System.out.println(c3.gerarResumo());
    }
}