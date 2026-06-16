-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
-- Qual o tamanho médio das universidades?

SELECT ROUND(AVG(num_students_enrolled)::numeric,2) AS media_estudantes
FROM universities_ranking;