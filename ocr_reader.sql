-- phpMyAdmin SQL Dump
-- version 4.9.11
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 13, 2023 at 07:49 PM
-- Server version: 8.1.0
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ocr_reader`
--

-- --------------------------------------------------------

--
-- Table structure for table `business_cards`
--

CREATE TABLE `business_cards` (
  `id` int NOT NULL,
  `card_holder_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `designation` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mobile_number1` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email_address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `website_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `business_cards`
--

INSERT INTO `business_cards` (`id`, `card_holder_name`, `designation`, `mobile_number1`, `email_address`, `website_url`, `address`) VALUES
(5, 'Selva', 'DATA MANAGER', '+123-456-7890, +123-456-7891', 'hello@XYZ1.com', 'XYZI.com', '123 ABC St , Chennai;, selva, TamilNadu 600113, digitals'),
(6, 'Amit kumar', 'CEO & FOUNDER', '', 'hello@global.com', 'global.com', '123-456-7569, WWW, 123 global, Erode,, GLOBAL, TamilNadu 600115, INSURANCE, St ,'),
(7, 'KARTHICK', 'General Manager', '+123-456-7890', 'hello@Borcelle.com', 'wwW.Borcelle.com', '123 ABC St , Salem,, TamilNadu 6004513, BORCELLE, AIRLINES'),
(8, 'REVANTH', 'Marketing Executive', '+91-456-1234', 'hello@CHRISTMAS.com', 'wwW.CHRISTMAS.com', '123 ABC St,, HYDRABAD, TamilNadu;, 600001, Family, Restaurant'),
(9, 'SANTHOSH', 'Technical Manager', '+123-456-1234', 'hello@Sun.com', 'www.Suncom', '123 ABC St , Tirupur, TamiINadu,, 641603, Sun Electricals');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `business_cards`
--
ALTER TABLE `business_cards`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `business_cards`
--
ALTER TABLE `business_cards`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
