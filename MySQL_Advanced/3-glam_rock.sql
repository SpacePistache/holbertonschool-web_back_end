-- List groups categorized as glam rock and their longevity

SELECT band_name,
       CASE
           WHEN split IS NULL THEN 2024 - formed
           ELSE split - formed
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam%'
ORDER BY lifespan DESC;
