from Analise_SQL.SQLExecutor import SQLExecutor

def main():

    executor = SQLExecutor()

    # Análise de diversidade
    print("Análise de diversidade:")
    executor.execute_file("Analise_SQL/queries/diversidade/genre_dominance.sql")
    executor.execute_file("Analise_SQL/queries/diversidade/genre_distribution.sql")

    print("\nAnálise de eficiência operacional:")
    # Análise de eficiência operacional
    executor.execute_file("Analise_SQL/queries/eficiencia_operacional/correlation_university_students.sql")
    executor.execute_file("Analise_SQL/queries/eficiencia_operacional/min_relation_university.sql")

    print("\nAnálise de estrutura:")
    # Análise de estrutura
    executor.execute_file("Analise_SQL/queries/estrutura/avg_university.sql")
    executor.execute_file("Analise_SQL/queries/estrutura/qnt_university.sql")
    executor.execute_file("Analise_SQL/queries/estrutura/qnt_country.sql")

    print("\nAnálise de internacionalização:")
    # Análise de internacionalização
    executor.execute_file("Analise_SQL/queries/Internacionalizacao/avg_students_international.sql")
    executor.execute_file("Analise_SQL/queries/Internacionalizacao/max_trend_university.sql")
    executor.execute_file("Analise_SQL/queries/Internacionalizacao/max_university_international.sql")

    print("\nAnálise de porte:")
    # Análise de porte
    executor.execute_file("Analise_SQL/queries/porte/max_university.sql")
    executor.execute_file("Analise_SQL/queries/porte/num_student.sql")

    print("Análise SQL executada com sucesso!")


if __name__ == "__main__":
    main()