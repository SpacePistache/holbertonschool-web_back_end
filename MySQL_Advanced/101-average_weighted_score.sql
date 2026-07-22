-- Computes and stores the weighted average score for all users

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections AS c
        JOIN projects AS p
            ON c.project_id = p.id
        WHERE c.user_id = users.id
    );
END$$

DELIMITER ;
