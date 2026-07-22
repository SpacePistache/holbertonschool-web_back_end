-- Computes and stores the weighted average score for a user

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN p_user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections AS c
        JOIN projects AS p
            ON c.project_id = p.id
        WHERE c.user_id = p_user_id
    )
    WHERE id = p_user_id;
END$$

DELIMITER ;
