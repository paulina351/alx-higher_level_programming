-- A script that lists all shows contained in hbtn_0d_tvshows without a genre linked
-- The database name will be passed as an argument of the mysql command
SELECT s.`title`, g.`genre_id`
  FROM  `tv_shows` AS s
        LEFT JOIN  `tv_show_genres` AS g
        ON s.`id` = g.`show_id`
        WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;
