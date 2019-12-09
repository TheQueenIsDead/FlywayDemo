ALTER TABLE `myschema`.`person`
ADD COLUMN `likes_candy` TINYINT(1) NULL DEFAULT 1 AFTER `age`;
UPDATE person SET likes_candy = 0 where first_name = 'Diggal';