-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Quais são as maiores universidades?

SELECT university_name, num_students_enrolled
FROM universities_ranking
WHERE num_students_enrolled IS NOT NULL
ORDER BY num_students_enrolled DESC
LIMIT 10;