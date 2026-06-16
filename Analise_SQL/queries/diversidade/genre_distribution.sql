-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Como está a distribuição de gênero?

SELECT
    AVG(female_pct) AS media_feminina,
    AVG(male_pct) AS media_masculina
FROM universities_ranking
WHERE female_pct IS NOT NULL
  AND male_pct IS NOT NULL;
