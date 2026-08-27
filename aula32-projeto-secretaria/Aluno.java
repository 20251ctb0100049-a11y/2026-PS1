/*
 * Disciplina: Programação / Orientação a Objetos
 * Nome: Rafael Lopes
 * Data: 20/08/2026
 * Projeto: Secretaria do Campus
 * Arquivo: Aluno.java
 */

public class Aluno {
    private String matricula;
    private String nome;
    private String curso;
    private String cidade; 

    public Aluno(String matricula, String nome, String curso, String cidade) {
        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.cidade = cidade;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    @Override
    public String toString() {
        return matricula + " | " + nome + " | " + curso + " | " + cidade;
    }
}