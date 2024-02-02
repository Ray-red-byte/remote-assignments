-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: assignment
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Article`
--

DROP TABLE IF EXISTS `Article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Article` (
  `article_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` varchar(255) DEFAULT NULL,
  `author_id` int NOT NULL,
  PRIMARY KEY (`article_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Article`
--

LOCK TABLES `Article` WRITE;
/*!40000 ALTER TABLE `Article` DISABLE KEYS */;
INSERT INTO `Article` VALUES (1,'Title 1','Content for Title 1',4),(2,'Title 2','Content for Title 2',2),(3,'Title 3','Content for Title 3',3),(4,'Title 4','Content for Title 4',1),(5,'Title 5','Content for Title 5',4),(6,'Title 6','Content for Title 6',2),(7,'Title 7','Content for Title 7',2),(8,'Title 8','Content for Title 8',2),(9,'Title 9','Content for Title 9',1),(10,'Title 10','Content for Title 10',2),(11,'Title 11','Content for Title 11',3),(12,'Title 12','Content for Title 12',1),(13,'Title 13','Content for Title 13',1),(14,'Title 14','Content for Title 14',3),(15,'Title 15','Content for Title 15',1),(16,'Title 16','Content for Title 16',3),(17,'Title 17','Content for Title 17',3),(18,'Title 18','Content for Title 18',2),(19,'Title 19','Content for Title 19',3),(20,'Title 20','Content for Title 20',4),(21,'Title 21','Content for Title 21',4),(22,'Title 22','Content for Title 22',1),(23,'Title 23','Content for Title 23',2),(24,'Title 24','Content for Title 24',1),(25,'Title 25','Content for Title 25',3),(26,'Title 26','Content for Title 26',1),(27,'Title 27','Content for Title 27',3),(28,'Title 28','Content for Title 28',4),(29,'Title 29','Content for Title 29',1),(30,'Title 30','Content for Title 30',2);
/*!40000 ALTER TABLE `Article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'ray67672@gmail.com','12345678'),(2,'ray558053@yahoo.com.tw','789456'),(3,'simongood2986@gmail.com','147852'),(4,'brbb200709+21@gmail.com','963852');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Query 1: Select all articles with their author’s email
SELECT user.email as author_email
FROM Article
JOIN user ON Article.author_id = user.id;


-- Query 2: Select articles from 7th to 12th sorted by id
SELECT * FROM Article
ORDER BY article_id
LIMIT 6 OFFSET 6;


-- Dump completed on 2024-02-02 10:27:20
