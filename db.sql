/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - online_tutor
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_tutor` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `online_tutor`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add instructions_table',7,'add_instructions_table'),
(26,'Can change instructions_table',7,'change_instructions_table'),
(27,'Can delete instructions_table',7,'delete_instructions_table'),
(28,'Can view instructions_table',7,'view_instructions_table'),
(29,'Can add login_table',8,'add_login_table'),
(30,'Can change login_table',8,'change_login_table'),
(31,'Can delete login_table',8,'delete_login_table'),
(32,'Can view login_table',8,'view_login_table'),
(33,'Can add question_table',9,'add_question_table'),
(34,'Can change question_table',9,'change_question_table'),
(35,'Can delete question_table',9,'delete_question_table'),
(36,'Can view question_table',9,'view_question_table'),
(37,'Can add teacher_table',10,'add_teacher_table'),
(38,'Can change teacher_table',10,'change_teacher_table'),
(39,'Can delete teacher_table',10,'delete_teacher_table'),
(40,'Can view teacher_table',10,'view_teacher_table'),
(41,'Can add test_table',11,'add_test_table'),
(42,'Can change test_table',11,'change_test_table'),
(43,'Can delete test_table',11,'delete_test_table'),
(44,'Can view test_table',11,'view_test_table'),
(45,'Can add studymaterials_table',12,'add_studymaterials_table'),
(46,'Can change studymaterials_table',12,'change_studymaterials_table'),
(47,'Can delete studymaterials_table',12,'delete_studymaterials_table'),
(48,'Can view studymaterials_table',12,'view_studymaterials_table'),
(49,'Can add student_table',13,'add_student_table'),
(50,'Can change student_table',13,'change_student_table'),
(51,'Can delete student_table',13,'delete_student_table'),
(52,'Can view student_table',13,'view_student_table'),
(53,'Can add salary_table',14,'add_salary_table'),
(54,'Can change salary_table',14,'change_salary_table'),
(55,'Can delete salary_table',14,'delete_salary_table'),
(56,'Can view salary_table',14,'view_salary_table'),
(57,'Can add result_table',15,'add_result_table'),
(58,'Can change result_table',15,'change_result_table'),
(59,'Can delete result_table',15,'delete_result_table'),
(60,'Can view result_table',15,'view_result_table'),
(61,'Can add request_table',16,'add_request_table'),
(62,'Can change request_table',16,'change_request_table'),
(63,'Can delete request_table',16,'delete_request_table'),
(64,'Can view request_table',16,'view_request_table'),
(65,'Can add paymeny_salary',17,'add_paymeny_salary'),
(66,'Can change paymeny_salary',17,'change_paymeny_salary'),
(67,'Can delete paymeny_salary',17,'delete_paymeny_salary'),
(68,'Can view paymeny_salary',17,'view_paymeny_salary'),
(69,'Can add payment_table',18,'add_payment_table'),
(70,'Can change payment_table',18,'change_payment_table'),
(71,'Can delete payment_table',18,'delete_payment_table'),
(72,'Can view payment_table',18,'view_payment_table'),
(73,'Can add feedback_table',19,'add_feedback_table'),
(74,'Can change feedback_table',19,'change_feedback_table'),
(75,'Can delete feedback_table',19,'delete_feedback_table'),
(76,'Can view feedback_table',19,'view_feedback_table'),
(77,'Can add complaint_table',20,'add_complaint_table'),
(78,'Can change complaint_table',20,'change_complaint_table'),
(79,'Can delete complaint_table',20,'delete_complaint_table'),
(80,'Can view complaint_table',20,'view_complaint_table'),
(81,'Can add chat_table',21,'add_chat_table'),
(82,'Can change chat_table',21,'change_chat_table'),
(83,'Can delete chat_table',21,'delete_chat_table'),
(84,'Can view chat_table',21,'view_chat_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$ioK9gfwXdDbaQn8ttdZYVl$oRFCKA7oSbMhWuRlDgLg8sTB+0dTfEr2J2uDyVAwy4w=','2023-11-11 09:53:02.894023',1,'admin','','','admin@gmail.com',1,1,'2023-11-11 05:47:37.576772');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(21,'sapp','chat_table'),
(20,'sapp','complaint_table'),
(19,'sapp','feedback_table'),
(7,'sapp','instructions_table'),
(8,'sapp','login_table'),
(18,'sapp','payment_table'),
(17,'sapp','paymeny_salary'),
(9,'sapp','question_table'),
(16,'sapp','request_table'),
(15,'sapp','result_table'),
(14,'sapp','salary_table'),
(13,'sapp','student_table'),
(12,'sapp','studymaterials_table'),
(10,'sapp','teacher_table'),
(11,'sapp','test_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-11-11 05:43:11.845902'),
(2,'auth','0001_initial','2023-11-11 05:43:12.459617'),
(3,'admin','0001_initial','2023-11-11 05:43:12.779256'),
(4,'admin','0002_logentry_remove_auto_add','2023-11-11 05:43:12.812373'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-11-11 05:43:12.856443'),
(6,'contenttypes','0002_remove_content_type_name','2023-11-11 05:43:13.047128'),
(7,'auth','0002_alter_permission_name_max_length','2023-11-11 05:43:13.147553'),
(8,'auth','0003_alter_user_email_max_length','2023-11-11 05:43:13.224789'),
(9,'auth','0004_alter_user_username_opts','2023-11-11 05:43:13.240930'),
(10,'auth','0005_alter_user_last_login_null','2023-11-11 05:43:13.337978'),
(11,'auth','0006_require_contenttypes_0002','2023-11-11 05:43:13.344665'),
(12,'auth','0007_alter_validators_add_error_messages','2023-11-11 05:43:13.369610'),
(13,'auth','0008_alter_user_username_max_length','2023-11-11 05:43:13.456658'),
(14,'auth','0009_alter_user_last_name_max_length','2023-11-11 05:43:13.539804'),
(15,'auth','0010_alter_group_name_max_length','2023-11-11 05:43:13.591678'),
(16,'auth','0011_update_proxy_permissions','2023-11-11 05:43:13.614893'),
(17,'auth','0012_alter_user_first_name_max_length','2023-11-11 05:43:13.705891'),
(18,'sapp','0001_initial','2023-11-11 05:43:14.712003'),
(19,'sessions','0001_initial','2023-11-11 05:43:14.769666');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

/*Table structure for table `sapp_chat_table` */

DROP TABLE IF EXISTS `sapp_chat_table`;

CREATE TABLE `sapp_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `chatbox` varchar(90) NOT NULL,
  `FROM_ID_id` bigint NOT NULL,
  `TO_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_chat_table_FROM_ID_id_ba3e09a2_fk_sapp_login_table_id` (`FROM_ID_id`),
  KEY `sapp_chat_table_TO_ID_id_8b26a6da_fk_sapp_login_table_id` (`TO_ID_id`),
  CONSTRAINT `sapp_chat_table_FROM_ID_id_ba3e09a2_fk_sapp_login_table_id` FOREIGN KEY (`FROM_ID_id`) REFERENCES `sapp_login_table` (`id`),
  CONSTRAINT `sapp_chat_table_TO_ID_id_8b26a6da_fk_sapp_login_table_id` FOREIGN KEY (`TO_ID_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_chat_table` */

insert  into `sapp_chat_table`(`id`,`date`,`chatbox`,`FROM_ID_id`,`TO_ID_id`) values 
(1,'2023-11-11','Hi sir can i start my classes with my students ',2,1),
(2,'2023-11-11','yes you can start your classes from now onthe basis of syllabus',1,2),
(3,'2023-11-11','hii',1,1),
(4,'2023-11-11','YOU CAN START YOUR CLASSES FROM NOW ON',1,5),
(5,'2023-11-11','can 1 get more questions from module 1',3,2),
(6,'2023-11-11','ok i will upload within a week',2,3);

/*Table structure for table `sapp_complaint_table` */

DROP TABLE IF EXISTS `sapp_complaint_table`;

CREATE TABLE `sapp_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `complaint` varchar(90) NOT NULL,
  `reply` varchar(90) NOT NULL,
  `STUDENT_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_complaint_table_STUDENT_ID_id_108c8ec5_fk_sapp_stud` (`STUDENT_ID_id`),
  CONSTRAINT `sapp_complaint_table_STUDENT_ID_id_108c8ec5_fk_sapp_stud` FOREIGN KEY (`STUDENT_ID_id`) REFERENCES `sapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_complaint_table` */

insert  into `sapp_complaint_table`(`id`,`date`,`complaint`,`reply`,`STUDENT_ID_id`) values 
(1,'2023-11-11','MATERIALS ARE NOT PROVIDE ON TIME','sorry for inconvience it will be corrected shortly',1);

/*Table structure for table `sapp_feedback_table` */

DROP TABLE IF EXISTS `sapp_feedback_table`;

CREATE TABLE `sapp_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(90) NOT NULL,
  `rating` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `STUDENT_ID_id` bigint NOT NULL,
  `TEACHER_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_feedback_table_STUDENT_ID_id_b07ecd6f_fk_sapp_stud` (`STUDENT_ID_id`),
  KEY `sapp_feedback_table_TEACHER_ID_id_aa041a90_fk_sapp_teac` (`TEACHER_ID_id`),
  CONSTRAINT `sapp_feedback_table_STUDENT_ID_id_b07ecd6f_fk_sapp_stud` FOREIGN KEY (`STUDENT_ID_id`) REFERENCES `sapp_student_table` (`id`),
  CONSTRAINT `sapp_feedback_table_TEACHER_ID_id_aa041a90_fk_sapp_teac` FOREIGN KEY (`TEACHER_ID_id`) REFERENCES `sapp_teacher_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_feedback_table` */

insert  into `sapp_feedback_table`(`id`,`feedback`,`rating`,`date`,`STUDENT_ID_id`,`TEACHER_ID_id`) values 
(1,'its really amazing','5','2023-11-11',1,1);

/*Table structure for table `sapp_instructions_table` */

DROP TABLE IF EXISTS `sapp_instructions_table`;

CREATE TABLE `sapp_instructions_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `instructions_details` varchar(90) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_instructions_table` */

insert  into `sapp_instructions_table`(`id`,`instructions_details`,`date`) values 
(1,'make students aware about syllabus','2023-11-11');

/*Table structure for table `sapp_login_table` */

DROP TABLE IF EXISTS `sapp_login_table`;

CREATE TABLE `sapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(90) NOT NULL,
  `password` varchar(90) NOT NULL,
  `type` varchar(90) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_login_table` */

insert  into `sapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'KAVYA','kavya123','teacher'),
(3,'riya','riya123','student'),
(4,'adarsh','adarsh1','student'),
(5,'arun','arun123','teacher'),
(6,'arya','aryapavi','student');

/*Table structure for table `sapp_payment_table` */

DROP TABLE IF EXISTS `sapp_payment_table`;

CREATE TABLE `sapp_payment_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `fee` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `REQUEST_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_payment_table_REQUEST_ID_id_57bd8c50_fk_sapp_requ` (`REQUEST_ID_id`),
  CONSTRAINT `sapp_payment_table_REQUEST_ID_id_57bd8c50_fk_sapp_requ` FOREIGN KEY (`REQUEST_ID_id`) REFERENCES `sapp_request_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_payment_table` */

/*Table structure for table `sapp_paymeny_salary` */

DROP TABLE IF EXISTS `sapp_paymeny_salary`;

CREATE TABLE `sapp_paymeny_salary` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `month` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  `SALARY_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_paymeny_salary_SALARY_ID_id_009f5090_fk_sapp_sala` (`SALARY_ID_id`),
  CONSTRAINT `sapp_paymeny_salary_SALARY_ID_id_009f5090_fk_sapp_sala` FOREIGN KEY (`SALARY_ID_id`) REFERENCES `sapp_salary_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_paymeny_salary` */

/*Table structure for table `sapp_question_table` */

DROP TABLE IF EXISTS `sapp_question_table`;

CREATE TABLE `sapp_question_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `questions` varchar(90) NOT NULL,
  `option1` varchar(90) NOT NULL,
  `option2` varchar(90) NOT NULL,
  `option3` varchar(90) NOT NULL,
  `option4` varchar(90) NOT NULL,
  `result` varchar(90) NOT NULL,
  `TEST_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_question_table_TEST_ID_id_22b77bca_fk_sapp_test_table_id` (`TEST_ID_id`),
  CONSTRAINT `sapp_question_table_TEST_ID_id_22b77bca_fk_sapp_test_table_id` FOREIGN KEY (`TEST_ID_id`) REFERENCES `sapp_test_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_question_table` */

insert  into `sapp_question_table`(`id`,`questions`,`option1`,`option2`,`option3`,`option4`,`result`,`TEST_ID_id`) values 
(1,' Which of the following is the numerical coefficient of x2y2','0','1','X2','y2','1',1),
(2,' Which of the following is the numerical coefficient of x2y2','2','3','4','7','4',2),
(3,'  What is the value of 5x25 - 3x32 + 2x-12 at x=1?','0','2','4','none ','0',2),
(4,'Which of the following is the numerical coefficient of -5xy?','5','-x','-y','-5','-5',2),
(5,'The value of x2 - 5 at x= -1 is-','-5','-4','-3','-1','-1',2),
(6,'Which of the following is obtained by subtracting x2-y2 from y2 - x2','-2','-5','-8','10','-2',2),
(7,'what is a+b','1','3','9','11','9',2);

/*Table structure for table `sapp_request_table` */

DROP TABLE IF EXISTS `sapp_request_table`;

CREATE TABLE `sapp_request_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(90) NOT NULL,
  `STUDENT_ID_id` bigint NOT NULL,
  `TEACHER_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_request_table_STUDENT_ID_id_6d8d5dd6_fk_sapp_stud` (`STUDENT_ID_id`),
  KEY `sapp_request_table_TEACHER_ID_id_99cb367a_fk_sapp_teac` (`TEACHER_ID_id`),
  CONSTRAINT `sapp_request_table_STUDENT_ID_id_6d8d5dd6_fk_sapp_stud` FOREIGN KEY (`STUDENT_ID_id`) REFERENCES `sapp_student_table` (`id`),
  CONSTRAINT `sapp_request_table_TEACHER_ID_id_99cb367a_fk_sapp_teac` FOREIGN KEY (`TEACHER_ID_id`) REFERENCES `sapp_teacher_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_request_table` */

insert  into `sapp_request_table`(`id`,`date`,`status`,`STUDENT_ID_id`,`TEACHER_ID_id`) values 
(1,'2023-11-11','Accept',1,1),
(2,'2023-11-11','Accept',2,2);

/*Table structure for table `sapp_result_table` */

DROP TABLE IF EXISTS `sapp_result_table`;

CREATE TABLE `sapp_result_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `result` varchar(90) NOT NULL,
  `QUESTION_ID_id` bigint NOT NULL,
  `TEACHER_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_result_table_QUESTION_ID_id_446905c5_fk_sapp_ques` (`QUESTION_ID_id`),
  KEY `sapp_result_table_TEACHER_ID_id_82439106_fk_sapp_stud` (`TEACHER_ID_id`),
  CONSTRAINT `sapp_result_table_QUESTION_ID_id_446905c5_fk_sapp_ques` FOREIGN KEY (`QUESTION_ID_id`) REFERENCES `sapp_question_table` (`id`),
  CONSTRAINT `sapp_result_table_TEACHER_ID_id_82439106_fk_sapp_stud` FOREIGN KEY (`TEACHER_ID_id`) REFERENCES `sapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_result_table` */

insert  into `sapp_result_table`(`id`,`date`,`result`,`QUESTION_ID_id`,`TEACHER_ID_id`) values 
(1,'2023-11-11','1',1,1),
(2,'2023-11-11','0',2,1),
(3,'2023-11-11','1',3,1),
(4,'2023-11-11','1',4,1),
(5,'2023-11-11','1',5,1);

/*Table structure for table `sapp_salary_table` */

DROP TABLE IF EXISTS `sapp_salary_table`;

CREATE TABLE `sapp_salary_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `salary` varchar(90) NOT NULL,
  `TEACHER_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_salary_table_TEACHER_ID_id_75d49fa5_fk_sapp_teac` (`TEACHER_ID_id`),
  CONSTRAINT `sapp_salary_table_TEACHER_ID_id_75d49fa5_fk_sapp_teac` FOREIGN KEY (`TEACHER_ID_id`) REFERENCES `sapp_teacher_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_salary_table` */

insert  into `sapp_salary_table`(`id`,`date`,`salary`,`TEACHER_ID_id`) values 
(1,'2023-11-11','250',1);

/*Table structure for table `sapp_student_table` */

DROP TABLE IF EXISTS `sapp_student_table`;

CREATE TABLE `sapp_student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(90) NOT NULL,
  `lastname` varchar(90) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(90) NOT NULL,
  `place` varchar(90) NOT NULL,
  `post` varchar(90) NOT NULL,
  `pin` bigint NOT NULL,
  `email` varchar(90) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `phonenumber` bigint NOT NULL,
  `standard` varchar(90) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_student_table_LOGIN_id_80376218_fk_sapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sapp_student_table_LOGIN_id_80376218_fk_sapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_student_table` */

insert  into `sapp_student_table`(`id`,`firstname`,`lastname`,`age`,`gender`,`place`,`post`,`pin`,`email`,`photo`,`phonenumber`,`standard`,`LOGIN_id`) values 
(1,'RIYA','RAVI',11,'female','PARAVUR','NORTH PARAVUR',668815,'riya@gmail.com','stuimages.jpg',6789002211,'8',3),
(2,'adarsh','prakash',8,'female','anjoor','kunnakulam',123456,'adarshprakash@gmail.com','stdmphoto.jpg',8989898989,'6',4),
(3,'Arya','p p',5,'female','kannur','thayolaparambu',565656,'arya@mail.com','stdfphoto.png',9090909090,'2',6);

/*Table structure for table `sapp_studymaterials_table` */

DROP TABLE IF EXISTS `sapp_studymaterials_table`;

CREATE TABLE `sapp_studymaterials_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `subject` varchar(90) NOT NULL,
  `notes` varchar(100) NOT NULL,
  `TEACHER_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_studymaterials__TEACHER_ID_id_cc0de927_fk_sapp_teac` (`TEACHER_ID_id`),
  CONSTRAINT `sapp_studymaterials__TEACHER_ID_id_cc0de927_fk_sapp_teac` FOREIGN KEY (`TEACHER_ID_id`) REFERENCES `sapp_teacher_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_studymaterials_table` */

insert  into `sapp_studymaterials_table`(`id`,`date`,`subject`,`notes`,`TEACHER_ID_id`) values 
(1,'2023-11-11','Science','Module 4 notes.pdf',1),
(2,'2023-11-11','Maths','MATHS UNIT TEST 2.pdf',2);

/*Table structure for table `sapp_teacher_table` */

DROP TABLE IF EXISTS `sapp_teacher_table`;

CREATE TABLE `sapp_teacher_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(90) NOT NULL,
  `lastname` varchar(90) NOT NULL,
  `gender` varchar(90) NOT NULL,
  `place` varchar(90) NOT NULL,
  `post` varchar(90) NOT NULL,
  `pin` bigint NOT NULL,
  `qualification` varchar(90) NOT NULL,
  `proof` varchar(100) NOT NULL,
  `experience` varchar(90) NOT NULL,
  `phonenumber` bigint NOT NULL,
  `email` varchar(90) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_teacher_table_LOGIN_id_5835062e_fk_sapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sapp_teacher_table_LOGIN_id_5835062e_fk_sapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_teacher_table` */

insert  into `sapp_teacher_table`(`id`,`firstname`,`lastname`,`gender`,`place`,`post`,`pin`,`qualification`,`proof`,`experience`,`phonenumber`,`email`,`photo`,`LOGIN_id`) values 
(1,'kavya','k','other','thekkadi','thekkadi',668814,'Bed in english','teacher_resume.jpg','3',9947161588,'kavya@gmail.com','tchr photo.jpg',2),
(2,'Arun','prakash','female','althara','punnayurkulam',123456,'Bed in general','resume.png','5',8989898989,'arun@gmail.com','tcrm.png',5);

/*Table structure for table `sapp_test_table` */

DROP TABLE IF EXISTS `sapp_test_table`;

CREATE TABLE `sapp_test_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `test` varchar(90) NOT NULL,
  `details` varchar(90) NOT NULL,
  `TEACHERS_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_test_table_TEACHERS_ID_id_55408c43_fk_sapp_teacher_table_id` (`TEACHERS_ID_id`),
  CONSTRAINT `sapp_test_table_TEACHERS_ID_id_55408c43_fk_sapp_teacher_table_id` FOREIGN KEY (`TEACHERS_ID_id`) REFERENCES `sapp_teacher_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_test_table` */

insert  into `sapp_test_table`(`id`,`date`,`test`,`details`,`TEACHERS_ID_id`) values 
(1,'2023-11-11','maths aptitude test','there will be maths aptitude test on monday prepare well',1),
(2,'2023-11-11','maths 2nd module','aptitude test',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
