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
    private int idade; // Atributo extra

    public Aluno(String matricula, String nome, String curso, int idade) {
        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.idade = idade;
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

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    @Override
    public String toString() {
        return "Matrícula: " + matricula + 
               " | Nome: " + nome + 
               " | Curso: " + curso + 
               " | Idade: " + idade;
    }
}