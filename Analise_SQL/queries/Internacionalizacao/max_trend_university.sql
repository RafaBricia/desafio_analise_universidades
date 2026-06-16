-- rank,university_name,num_students_enrolled,num_students_employee,percentual_international_students,date_random,type,female_pct,male_pct
--Universidades maiores tendem a ser mais internacionais?

-- SELECT
--     CORR(num_students_enrolled, percentual_international_students) AS correlacao_tamanho_internacionalizacao
-- FROM universities_ranking
-- WHERE num_students_enrolled IS NOT NULL
--   AND percentual_international_students IS NOT NULL;

SELECT
    CASE 
        WHEN num_students_enrolled > 50000 THEN 'Grande'
        WHEN num_students_enrolled > 20000 THEN 'Média'
        ELSE 'Pequena'
    END AS tamanho,
    AVG(percentual_international_students) AS media_internacionalizacao
FROM universities_ranking
WHERE percentual_international_students IS NOT NULL
GROUP BY tamanho
ORDER BY media_internacionalizacao DESC;