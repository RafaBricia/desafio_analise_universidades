-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Existe correlação entre tamanho da universidade e relação aluno/funcionário?

SELECT  CORR(num_students_enrolled, num_students_employee) AS correlacao
FROM universities_ranking;