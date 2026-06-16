-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
-- existem universidades com forte predominância masculina ou feminina?

SELECT university_name, female_pct, male_pct,
CASE 
    WHEN female_pct ISNULL THEN  
        'Dados Faltantes'
    WHEN male_pct ISNULL THEN  
        'Dados Faltantes'
    WHEN female_pct > male_pct THEN  
        'Predominância Feminina'
    WHEN female_pct < male_pct THEN  
        'Predominância Masculina'
    ELSE  'Equilíbrio'
END as predominance_gender
FROM universities_ranking
ORDER BY predominance_gender desc
LIMIT 10;