-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Qual a média de estudantes internacionais?

select round(AVG(percentual_international_students)::numeric,2) AS media_estudantes_internacionais
from universities_ranking
where percentual_international_students IS NOT NULL;