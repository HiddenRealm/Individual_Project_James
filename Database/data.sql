-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `id` smallint(6) NOT NULL,
  `first_name` varchar(8) NOT NULL,
  `last_name` varchar(13) NOT NULL,
  `team` varchar(12) NOT NULL,
  `worth` smallint(6) NOT NULL,
  `posistion` varchar(9) NOT NULL,
  `picture` varchar(0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'Charlie','Faumuina','New Zealand',2005,'Prop',''),(2,'Dan','Cole','England',2623,'Prop',''),(3,'Jack','McGrath','Ireland',2543,'Prop',''),(4,'Joe','Moody','New Zealand',2306,'Prop',''),(5,'Mako','Vunipola','England',2054,'Prop',''),(6,'Owen','Franks','New Zealand',2321,'Prop',''),(7,'Sekope','Kepu','Australia',2499,'Prop',''),(8,'Tadhg','Furlong','Ireland',1791,'Prop',''),(9,'Tendai','Mtawarira','South Africa',1786,'Prop',''),(10,'Wyatt','Crockett','New Zealand',1785,'Prop',''),(11,'Adriaan','Strauss','South Africa',1831,'Hooker',''),(12,'Agustin','Creevy','Argentina',1556,'Hooker',''),(13,'Dane','Coles','New Zealand',4053,'Hooker',''),(14,'Dylan','Hartley','England',2241,'Hooker',''),(15,'Guilhem','Guirado','France',1442,'Hooker',''),(16,'Ken','Owens','Wales',1525,'Hooker',''),(17,'Rory','Best','Ireland',2127,'Hooker',''),(18,'Ross','Ford','Scotland',892,'Hooker',''),(19,'Scott','Baldwin','Wales',1133,'Hooker',''),(20,'Stephen','Moore','Australia',2289,'Hooker',''),(21,'Alun','Wyn-Jones','Wales',1734,'Locks',''),(22,'Brodie','Retallick','New Zealand',2982,'Locks',''),(23,'Courtney','Lawes','England',2405,'Locks',''),(24,'Devin','Toner','Ireland',2376,'Locks',''),(25,'Eben','Etzebeth','South Africa',1587,'Locks',''),(26,'Joe','Launchbury','England',1858,'Locks',''),(27,'Jonny','Gray','Scotland',1884,'Locks',''),(28,'Richie','Gray','Scotland',1634,'Locks',''),(29,'Sam','Whitelock','New Zealand',2869,'Locks',''),(30,'Yoann','Maestri','France',1596,'Locks',''),(31,'Ardie','Savea','New Zealand',1707,'Flanker',''),(32,'Chris','Robshaw','England',1748,'Flanker',''),(33,'CJ','Stander','Ireland',2531,'Flanker',''),(34,'James','Haskell','England',1572,'Flanker',''),(35,'Jerome','Kaino','New Zealand',2169,'Flanker',''),(36,'Justin','Tipuric','Wales',1444,'Flanker',''),(37,'Kevin','Gourdon','France',2182,'Flanker',''),(38,'Michael','Hooper','Australia',3175,'Flanker',''),(39,'Pablo','Matera','Argentina',1766,'Flanker',''),(40,'Sam','Cane','New Zealand',1890,'Flanker',''),(41,'Billy','Vunipola','England',1649,'Number 8',''),(42,'David','Pocock','Australia',834,'Number 8',''),(43,'Facunda','Isa','Argentina',1611,'Number 8',''),(44,'Jamie','Heaslip','Ireland',2785,'Number 8',''),(45,'Kieran','Read','New Zealand',3728,'Number 8',''),(46,'Louis','Picamoles','France',1645,'Number 8',''),(47,'Nathan','Hughes','England',1124,'Number 8',''),(48,'Ross','Moriarty','Wales',1119,'Number 8',''),(49,'Taulupe','Faletau','Wales',1412,'Number 8',''),(50,'Warren','Whiteley','South Africa',2124,'Number 8',''),(51,'Aaron','Smith','New Zealand',1637,'Scrumhalf',''),(52,'Ben','Youngs','England',1852,'Scrumhalf',''),(53,'Conor','Murray','Ireland',2159,'Scrumhalf',''),(54,'Fef','De-Klerk','South Africa',1036,'Scrumhalf',''),(55,'Greig','Laidlaw','Scotland',1115,'Scrumhalf',''),(56,'Martin','Landajo','Argentina',1323,'Scrumhalf',''),(57,'Nick','Phipps','Australia',1177,'Scrumhalf',''),(58,'Rhys','Webb','Wales',1406,'Scrumhalf',''),(59,'TJ','Perenara','New Zealand',1725,'Scrumhalf',''),(60,'Will','Genia','Australia',1508,'Scrumhalf',''),(61,'Aaron','Cruden','New Zealand',1435,'Flyhalf',''),(62,'Beauden','Barrett','New Zealand',4399,'Flyhalf',''),(63,'Bernard','Foley','Australia',2106,'Flyhalf',''),(64,'Dan','Biggar','Wales',2125,'Flyhalf',''),(65,'Elton','Jantjies','South Africa',1074,'Flyhalf',''),(66,'Finn','Russell','Scotland',1072,'Flyhalf',''),(67,'George','Ford','England',2275,'Flyhalf',''),(68,'Jonathan','Sexton','Ireland',901,'Flyhalf',''),(69,'Nicolas','Sanchez','Argentina',1411,'Flyhalf',''),(70,'Paddy','Jackson','Ireland',1745,'Flyhalf',''),(71,'Dane','Haylett-Petty','Australia',3400,'Wings',''),(72,'Julian','Savea','New Zealand',3169,'Wings',''),(73,'Waisake','Naholo','New Zealand',2731,'Wings',''),(74,'Israel','Dagg','New Zealand',2641,'Wings',''),(75,'Keith','Earls','Ireland',2112,'Wings',''),(76,'George','North','Wales',1961,'Wings',''),(77,'Virimi','Vakatawa','France',1899,'Wings',''),(78,'Liam','Williams','Wales',1686,'Wings',''),(79,'Santiago','Cordero','Argentina',1666,'Wings',''),(80,'Jack','Nowell','England',1575,'Wings',''),(81,'Anton','Lienert-Brown','New Zealand',2587,'Centre',''),(82,'Ryan','Crotty','New Zealand',2560,'Centre',''),(83,'Jonathan','Joseph','England',2531,'Centre',''),(84,'Jonathan','Davies','Wales',2436,'Centre',''),(85,'Malakai','Fekitoa','New Zealand',2406,'Centre',''),(86,'Tevita','Kuridrani','Australia',2282,'Centre',''),(87,'Owen','Farrell','England',2178,'Centre',''),(88,'Samu','Kerevi','Australia',1839,'Centre',''),(89,'Gary','Ringrose','Ireland',1536,'Centre',''),(90,'Robbie','Henshaw','Ireland',1511,'Centre',''),(91,'Israel','Folau','Australia',2923,'Fullback',''),(92,'Ben','Smith','New Zealand',2751,'Fullback',''),(93,'Mike','Brown','England',2428,'Fullback',''),(94,'Stuart','Hogg','Scotland',1762,'Fullback',''),(95,'Joaquin','Tuculet','Argentina',1290,'Fullback',''),(96,'Scott','Spedding','France',1250,'Fullback',''),(97,'Israel','Dagg','New Zealand',1128,'Fullback',''),(98,'Liam','Williams','Wales',834,'Fullback',''),(99,'Willie','le-Roux','South Africa',761,'Fullback',''),(100,'Rob','Kearney','Ireland',694,'Fullback','');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:25
