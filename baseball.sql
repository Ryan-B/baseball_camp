-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 127.0.0.1    Database: baseball
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `registered_campers`
--

DROP TABLE IF EXISTS `registered_campers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registered_campers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `camper_first` varchar(245) DEFAULT NULL,
  `camper_last` varchar(245) DEFAULT NULL,
  `camper_password` varchar(245) DEFAULT NULL,
  `parent_first` varchar(245) DEFAULT NULL,
  `parent_last` varchar(245) DEFAULT NULL,
  `parent_password` varchar(245) DEFAULT NULL,
  `email` varchar(245) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `home_address` varchar(245) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registered_campers`
--

LOCK TABLES `registered_campers` WRITE;
/*!40000 ALTER TABLE `registered_campers` DISABLE KEYS */;
INSERT INTO `registered_campers` VALUES (1,'Tim','Lincecum','$2a$12$hIRmm/ta55MuJd2bUnazgeQbZ8G83RcfyKsbpa0kKRDGMcQDKXj5O','Pappa','Lincecum','$2a$12$m/.2jR7nKJPWHjW3fGPuB.Q1QXz5.1vpRGBGuKc5E7KErbyxuI.zi','doog@doog.com','206.866.3688','5118 Nettot ct NW  Olympia, Wa 98502','2015-09-28 10:34:15','2015-09-28 10:34:15'),(2,'Marshawn','Lynch','$2a$12$7Y53toq6vA5bRrYlA71YyuixiUROue2MDduF0.R5ku4OPPqQwG8O6','Mamma','Lynch','$2a$12$GVoiQRvmGjr6cMYGFm.SxemYu3cuHfbI.2yVdltzoVbA9/ZMo6QvG','lynch@doog.com','206.856.8927','763 32nd ave Seattle, Wa 98122','2015-09-28 11:21:28','2015-09-28 11:21:28'),(3,'Ryan','Bird','$2a$12$rurqfB6AUldMhQxDIkE/neu3yE6JRxQV0MhQCHIibNLA2ui1i44Ne','Rick','Bird','$2a$12$WMB1dIl4i3gY/rP0h752Hu42fkBPbiiUvPlBT21y2Evr.MO1sjIsW','rick@bird.com','206.883.8888','711 Aurora Ave, University District 98115','2015-09-28 11:43:59','2015-09-28 11:43:59');
/*!40000 ALTER TABLE `registered_campers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-29 13:40:10
