/*
 * Disciplina: 2026-PS
 * Projeto    : bibliotech
 * Arquivo    : Usuario.java
 * Autor      : seu nome
 * Descricao  : a classe geral do diagrama. Leitor e Bibliotecario sao tipos de
 */

public class Usuario {

    private String nome;
    private String matricula;

    public Usuario(String nome, String matricula) {
        this.nome = nome;
        this.matricula = matricula;
    }

    public String getNome() {
        return nome;
    }

    public String getMatricula() {
        return matricula;
    }

    // entrar(): a operacao da caixa. Regra provisoria: entra quem tem matricu
    public boolean entrar() {
        return !matricula.isEmpty();
    }

    public String toString() {
        return nome + " (" + matricula + ")";
    }
}
