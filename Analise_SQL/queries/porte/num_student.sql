-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Como está distribuído o número de alunos?

SELECT
    COUNT(*) AS total_universidades,
    AVG(num_students_enrolled) AS media,
    MIN(num_students_enrolled) AS minimo,
    MAX(num_students_enrolled) AS maximo
FROM universities_ranking
WHERE num_students_enrolled IS NOT NULL;