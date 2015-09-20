-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 127.0.0.1    Database: helpwanted
-- ------------------------------------------------------
-- Server version	5.6.25

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
-- Table structure for table `archcommit`
--

DROP TABLE IF EXISTS `archcommit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `archcommit` (
  `cid` int(11) DEFAULT NULL,
  `aid` int(11) DEFAULT NULL,
  KEY `aid_idx` (`aid`),
  KEY `cid_idx` (`cid`),
  CONSTRAINT `archcommit_aid` FOREIGN KEY (`aid`) REFERENCES `archenemy` (`aid`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `archcommit_cid` FOREIGN KEY (`cid`) REFERENCES `crime` (`cid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archcommit`
--

LOCK TABLES `archcommit` WRITE;
/*!40000 ALTER TABLE `archcommit` DISABLE KEYS */;
/*!40000 ALTER TABLE `archcommit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `archenemy`
--

DROP TABLE IF EXISTS `archenemy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `archenemy` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `id` int(11) NOT NULL,
  `name` varchar(405) DEFAULT NULL,
  `contact` varchar(405) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  KEY `id_idx` (`id`),
  CONSTRAINT `archenemy_id` FOREIGN KEY (`id`) REFERENCES `people` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archenemy`
--

LOCK TABLES `archenemy` WRITE;
/*!40000 ALTER TABLE `archenemy` DISABLE KEYS */;
INSERT INTO `archenemy` VALUES (1,5,'Scarlet Witch',''),(3,16,'Green Goblin',''),(4,14,'Sandman','896-000-0000');
/*!40000 ALTER TABLE `archenemy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `archpower`
--

DROP TABLE IF EXISTS `archpower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `archpower` (
  `pid` int(11) DEFAULT NULL,
  `aid` int(11) DEFAULT NULL,
  KEY `pid_idx` (`pid`),
  KEY `archpower_aid` (`aid`),
  CONSTRAINT `archpower_aid` FOREIGN KEY (`aid`) REFERENCES `archenemy` (`aid`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `archpower_pid` FOREIGN KEY (`pid`) REFERENCES `power` (`pid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archpower`
--

LOCK TABLES `archpower` WRITE;
/*!40000 ALTER TABLE `archpower` DISABLE KEYS */;
/*!40000 ALTER TABLE `archpower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crime`
--

DROP TABLE IF EXISTS `crime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crime` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `location` varchar(405) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `resolved` char(1) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crime`
--

LOCK TABLES `crime` WRITE;
/*!40000 ALTER TABLE `crime` DISABLE KEYS */;
INSERT INTO `crime` VALUES (1,'Manhattan','2013-06-17 21:03:03','Murder of 2 people','Y'),(2,'Michigan','2010-09-09 21:09:33','A cat was stuck in a tree.','Y');
/*!40000 ALTER TABLE `crime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fights`
--

DROP TABLE IF EXISTS `fights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fights` (
  `sid` int(11) DEFAULT NULL,
  `aid` int(11) DEFAULT NULL,
  KEY `sid_idx` (`sid`),
  KEY `aid_idx` (`aid`),
  CONSTRAINT `fights_aid` FOREIGN KEY (`aid`) REFERENCES `archenemy` (`aid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fights_sid` FOREIGN KEY (`sid`) REFERENCES `superhero` (`sid`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fights`
--

LOCK TABLES `fights` WRITE;
/*!40000 ALTER TABLE `fights` DISABLE KEYS */;
INSERT INTO `fights` VALUES (2,1),(5,3);
/*!40000 ALTER TABLE `fights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `location` varchar(405) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (4,'Courtney','Whitmore','F','Florida','1980-11-11'),(5,'Wanda','Maximoff','F','','1976-11-12'),(6,'Kyle','Jones','M','Utah','1900-08-19'),(7,'Manny','Dylan','M','Oregon','1987-01-01'),(8,'Robert Bruce','Banner','M','Ohio','1960-09-09'),(9,'Steven Grant','Rogers','M','Washington, DC','1980-07-18'),(10,'Anthony Edward','Stark','M','New York','1971-03-17'),(11,'Natalia','Romanova','F','Russia','1890-07-23'),(12,'Peter','Parker','M','New York','1981-05-14'),(13,'Otto Gunther','Octavius','M','New York','1967-09-01'),(14,'Flint','Marko','M','New York','1956-09-03'),(15,'Curt','Conners','M','Wyoming','1980-09-12'),(16,'Norman','Osborn','M','New York','1980-04-13'),(17,'Hello','Kitty','F','Japan','1700-12-12'),(18,'Karen','Mdsjf','M','Miami','1980-06-07');
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `power`
--

DROP TABLE IF EXISTS `power`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `power` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(405) DEFAULT NULL,
  `fatality` char(1) DEFAULT NULL,
  `description` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `power`
--

LOCK TABLES `power` WRITE;
/*!40000 ALTER TABLE `power` DISABLE KEYS */;
INSERT INTO `power` VALUES (2,'Flight','N','Allows one to soar above tall buildings'),(3,'Time-Travel','N','Allows one to manipulate time'),(4,'Mind-Reading','N','Allows one to read another person\'s thoughts'),(5,'Telekenesis','Y','Allows one to manipulate and control objects with the mind'),(6,'Duplication','N','Ability to create duplicates of oneself'),(7,'Invisibility','N','Ability to render oneself unseen'),(8,'Poison Generation','Y','Ability to assault others with a variety of toxins');
/*!40000 ALTER TABLE `power` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strategy`
--

DROP TABLE IF EXISTS `strategy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `strategy` (
  `pid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  KEY `cid_idx` (`cid`),
  KEY `pid_idx` (`pid`),
  CONSTRAINT `strategy_cid` FOREIGN KEY (`cid`) REFERENCES `crime` (`cid`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `strategy_pid` FOREIGN KEY (`pid`) REFERENCES `power` (`pid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strategy`
--

LOCK TABLES `strategy` WRITE;
/*!40000 ALTER TABLE `strategy` DISABLE KEYS */;
/*!40000 ALTER TABLE `strategy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `superhero`
--

DROP TABLE IF EXISTS `superhero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `superhero` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `id` int(11) NOT NULL,
  `name` varchar(405) DEFAULT NULL,
  `contact` varchar(405) DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `id_idx` (`id`),
  CONSTRAINT `superhero_id` FOREIGN KEY (`id`) REFERENCES `people` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `superhero`
--

LOCK TABLES `superhero` WRITE;
/*!40000 ALTER TABLE `superhero` DISABLE KEYS */;
INSERT INTO `superhero` VALUES (2,4,'Stargirl','123-456-7890'),(3,9,'Captain America','890-764-0973'),(4,10,'Iron Man','456-908-7890'),(5,12,'Spiderman','345-908-2222');
/*!40000 ALTER TABLE `superhero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `superpower`
--

DROP TABLE IF EXISTS `superpower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `superpower` (
  `pid` int(11) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  KEY `sid_idx` (`sid`),
  KEY `pid_idx` (`pid`),
  CONSTRAINT `superpower_pid` FOREIGN KEY (`pid`) REFERENCES `power` (`pid`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `superpower_sid` FOREIGN KEY (`sid`) REFERENCES `superhero` (`sid`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `superpower`
--

LOCK TABLES `superpower` WRITE;
/*!40000 ALTER TABLE `superpower` DISABLE KEYS */;
/*!40000 ALTER TABLE `superpower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supersave`
--

DROP TABLE IF EXISTS `supersave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supersave` (
  `sid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  KEY `sid_idx` (`sid`),
  KEY `cid_idx` (`cid`),
  CONSTRAINT `supersave_cid` FOREIGN KEY (`cid`) REFERENCES `crime` (`cid`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `supersave_sid` FOREIGN KEY (`sid`) REFERENCES `superhero` (`sid`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supersave`
--

LOCK TABLES `supersave` WRITE;
/*!40000 ALTER TABLE `supersave` DISABLE KEYS */;
/*!40000 ALTER TABLE `supersave` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-20 19:12:56
