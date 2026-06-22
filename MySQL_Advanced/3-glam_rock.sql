--List groups categorized as glam rock and their longevity

SELECT band_name,
       CASE
           WHEN split IS NULL THEN 2024 - formed
           ELSE split - formed
       END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
