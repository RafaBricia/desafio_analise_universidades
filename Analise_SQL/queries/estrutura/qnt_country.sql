-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
-- Quantos países estão representados?

SELECT COUNT(*) AS quantidade_paises
FROM universities_ranking
WHERE category_type = 'Country';