-- A script that lists all shows contained in the database hbtn_0d_tvshows
-- The database name will be passed as an argument of the mysql command
SELECT  s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN  `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
