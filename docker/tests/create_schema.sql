CREATE DATABASE `tests`;
USE `tests`;

DROP TABLE IF EXISTS `breads`;

CREATE TABLE `breads` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_breads_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;