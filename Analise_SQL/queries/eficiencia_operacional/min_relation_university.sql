-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Quais universidades possuem menor relação aluno/funcionário?

SELECT university_name, num_students_employee
FROM universities_ranking
WHERE num_students_employee IS NOT NULL
ORDER BY num_students_employee ASC
LIMIT 10;