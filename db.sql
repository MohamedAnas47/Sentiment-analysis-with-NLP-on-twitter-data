/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - sentiment_analysis
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sentiment_analysis` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `sentiment_analysis`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Feedback` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`Id`,`Feedback`,`Date`,`user_id`) values 
(1,'good','2021-04-06',2),
(2,'kjsw','2021-04-20',2),
(3,'qjhw','2021-04-20',2);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Id`,`Username`,`Password`,`Type`) values 
(1,'anas','1234','admin'),
(2,'user','user123','user'),
(3,'qqqq','qqqq','user'),
(4,'shameem','wertyjk','user');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Product` varchar(20) DEFAULT NULL,
  `Twitter handle` varchar(20) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`Id`,`Product`,`Twitter handle`,`Description`) values 
(6,'iphonex','ggg','hhhhh'),
(7,'poco','jkkk','fff'),
(8,'','','');

/*Table structure for table `twitter` */

DROP TABLE IF EXISTS `twitter`;

CREATE TABLE `twitter` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Product_id` varchar(20) DEFAULT NULL,
  `Twitter` varchar(20) DEFAULT NULL,
  `Polarity score` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `twitter` */

insert  into `twitter`(`Id`,`Product_id`,`Twitter`,`Polarity score`) values 
(1,'5','ffv33','uugt'),
(2,'6','hggf','ugfd');

/*Table structure for table `view user` */

DROP TABLE IF EXISTS `view user`;

CREATE TABLE `view user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(20) DEFAULT NULL,
  `Housename` varchar(20) DEFAULT NULL,
  `Place` varchar(20) DEFAULT NULL,
  `Post` varchar(20) DEFAULT NULL,
  `pin` int(10) DEFAULT NULL,
  `Mob number` int(20) DEFAULT NULL,
  `Email-id` varchar(20) DEFAULT NULL,
  `Login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `view user` */

insert  into `view user`(`User_id`,`Username`,`Housename`,`Place`,`Post`,`pin`,`Mob number`,`Email-id`,`Login_id`) values 
(1,'anas','dfsa','fds','hikjh',657,2147483647,'mohamedanascp@gmail.',2),
(2,'qqqq','hhhhh','ppppp','popopo',0,2147483647,'sdcfvgbhj',3),
(3,'shameem','tyujjhgff','ttyuui','pouygh',656671,2147483647,'kjhfdgh',4);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
