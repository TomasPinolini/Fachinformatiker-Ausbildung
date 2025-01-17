-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2025 at 11:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5-wd&dbd-4`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id_products` int(8) NOT NULL,
  `price` float(6,2) NOT NULL,
  `description` text NOT NULL,
  `id_admin` int(8) NOT NULL,
  `state` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id_products`, `price`, `description`, `id_admin`, `state`) VALUES
(1, 19.99, 'Wireless Mouse', 4, '1'),
(2, 49.50, 'Bluetooth Keyboard', 4, '1'),
(3, 299.99, '27-inch Monitor', 4, '1'),
(4, 15.75, 'USB-C Cable', 4, '0'),
(5, 89.99, 'Mechanical Keyboard', 4, '1'),
(6, 12.49, 'Laptop Stand', 8, '1'),
(7, 29.99, 'External Hard Drive', 8, '0'),
(8, 159.49, 'Gaming Chair', 8, '1'),
(9, 5.99, 'Wireless Charger', 8, '1'),
(10, 399.99, 'High-End GPU', 4, '0');

-- --------------------------------------------------------

--
-- Table structure for table `purchases`
--

CREATE TABLE `purchases` (
  `id_purchase` int(11) NOT NULL,
  `id_users` int(11) NOT NULL,
  `id_product` int(11) NOT NULL,
  `purchase_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `purchases`
--

INSERT INTO `purchases` (`id_purchase`, `id_users`, `id_product`, `purchase_date`) VALUES
(1, 7, 9, '2024-09-09 22:00:00'),
(2, 6, 3, '2024-06-24 22:00:00'),
(3, 1, 1, '2024-12-06 23:00:00'),
(4, 5, 5, '2024-10-30 23:00:00'),
(5, 3, 10, '2024-02-13 23:00:00'),
(6, 8, 5, '2024-02-24 23:00:00'),
(7, 10, 4, '2024-09-27 22:00:00'),
(8, 8, 7, '2024-06-22 22:00:00'),
(9, 9, 9, '2024-10-01 22:00:00'),
(10, 3, 9, '2024-12-10 23:00:00'),
(11, 5, 2, '2024-01-03 23:00:00'),
(12, 3, 3, '2024-07-18 22:00:00'),
(13, 4, 8, '2024-08-02 22:00:00'),
(14, 5, 6, '2024-01-19 23:00:00'),
(15, 9, 8, '2024-09-02 22:00:00'),
(16, 4, 7, '2024-12-22 23:00:00'),
(17, 2, 10, '2024-11-21 23:00:00'),
(18, 1, 10, '2024-01-16 23:00:00'),
(19, 1, 8, '2024-07-20 22:00:00'),
(20, 7, 7, '2024-07-19 22:00:00'),
(21, 9, 5, '2024-05-09 22:00:00'),
(22, 3, 7, '2024-09-19 22:00:00'),
(23, 10, 10, '2024-06-18 22:00:00'),
(24, 1, 2, '2024-12-15 23:00:00'),
(25, 8, 2, '2024-06-15 22:00:00'),
(26, 3, 2, '2024-09-13 22:00:00'),
(27, 2, 9, '2024-01-13 23:00:00'),
(28, 7, 8, '2024-10-25 22:00:00'),
(29, 1, 1, '2024-06-21 22:00:00'),
(30, 8, 5, '2024-02-24 23:00:00'),
(31, 9, 7, '2024-03-20 23:00:00'),
(32, 5, 5, '2024-06-03 22:00:00'),
(33, 4, 10, '2024-09-02 22:00:00'),
(34, 4, 10, '2024-07-28 22:00:00'),
(35, 6, 8, '2024-08-11 22:00:00'),
(36, 8, 8, '2024-09-18 22:00:00'),
(37, 9, 1, '2024-01-04 23:00:00'),
(38, 2, 9, '2024-10-30 23:00:00'),
(39, 10, 8, '2024-06-23 22:00:00'),
(40, 7, 2, '2024-04-10 22:00:00'),
(41, 2, 7, '2024-10-31 23:00:00'),
(42, 7, 9, '2024-01-15 23:00:00'),
(43, 8, 1, '2024-11-27 23:00:00'),
(44, 6, 1, '2024-01-05 23:00:00'),
(45, 4, 4, '2024-01-09 23:00:00'),
(46, 8, 6, '2024-01-13 23:00:00'),
(47, 8, 1, '2024-08-08 22:00:00'),
(48, 8, 9, '2024-01-14 23:00:00'),
(49, 2, 1, '2024-02-29 23:00:00'),
(50, 5, 7, '2024-11-17 23:00:00'),
(51, 1, 3, '2024-06-02 22:00:00'),
(52, 6, 7, '2024-02-01 23:00:00'),
(53, 3, 2, '2024-11-14 23:00:00'),
(54, 4, 4, '2024-07-18 22:00:00'),
(55, 5, 10, '2024-05-06 22:00:00'),
(56, 5, 5, '2024-07-23 22:00:00'),
(57, 8, 1, '2024-10-21 22:00:00'),
(58, 5, 4, '2024-05-23 22:00:00'),
(59, 5, 1, '2024-11-20 23:00:00'),
(60, 5, 2, '2024-05-15 22:00:00'),
(61, 4, 8, '2024-01-18 23:00:00'),
(62, 4, 6, '2024-05-06 22:00:00'),
(63, 9, 8, '2024-02-17 23:00:00'),
(64, 10, 2, '2024-10-04 22:00:00'),
(65, 9, 9, '2024-10-31 23:00:00'),
(66, 4, 9, '2024-11-08 23:00:00'),
(67, 8, 2, '2024-01-01 23:00:00'),
(68, 6, 5, '2024-11-19 23:00:00'),
(69, 1, 8, '2024-08-23 22:00:00'),
(70, 2, 1, '2024-01-01 23:00:00'),
(71, 7, 4, '2024-11-13 23:00:00'),
(72, 5, 3, '2024-06-27 22:00:00'),
(73, 1, 10, '2024-02-18 23:00:00'),
(74, 5, 6, '2024-09-10 22:00:00'),
(75, 6, 7, '2024-09-20 22:00:00'),
(76, 7, 7, '2024-01-30 23:00:00'),
(77, 10, 1, '2024-04-16 22:00:00'),
(78, 5, 9, '2024-04-25 22:00:00'),
(79, 9, 3, '2024-06-12 22:00:00'),
(80, 5, 8, '2024-12-27 23:00:00'),
(81, 9, 2, '2024-05-26 22:00:00'),
(82, 4, 8, '2024-12-24 23:00:00'),
(83, 7, 9, '2024-08-17 22:00:00'),
(84, 9, 2, '2024-11-11 23:00:00'),
(85, 2, 6, '2024-03-10 23:00:00'),
(86, 8, 2, '2024-06-14 22:00:00'),
(87, 6, 7, '2024-01-29 23:00:00'),
(88, 9, 8, '2024-03-17 23:00:00'),
(89, 10, 2, '2024-02-04 23:00:00'),
(90, 9, 8, '2024-05-07 22:00:00'),
(91, 7, 4, '2024-01-06 23:00:00'),
(92, 6, 7, '2024-05-15 22:00:00'),
(93, 8, 7, '2024-11-28 23:00:00'),
(94, 4, 5, '2024-05-30 22:00:00'),
(95, 3, 2, '2024-03-16 23:00:00'),
(96, 7, 5, '2024-05-23 22:00:00'),
(97, 7, 1, '2024-07-01 22:00:00'),
(98, 4, 2, '2024-07-22 22:00:00'),
(99, 6, 2, '2024-02-14 23:00:00'),
(100, 6, 3, '2024-04-09 22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id_users` int(11) NOT NULL,
  `email` varchar(50) NOT NULL DEFAULT '',
  `birthdate` date NOT NULL,
  `password` varchar(25) NOT NULL,
  `type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id_users`, `email`, `birthdate`, `password`, `type`) VALUES
(1, 'johndoe123@gmail.com', '1990-05-15', 'pass1234', 'client'),
(2, 'janedoe456@gmail.com', '1985-09-10', 'secure987', 'client'),
(3, 'tomaspinolini2003@gmail.com', '2022-02-22', '123321pino', 'client'),
(4, 'adminmaster@domain.com', '1980-12-01', 'admin2021', 'admin'),
(5, 'guestuser1@domain.com', '2000-07-21', 'guest987', 'guest'),
(6, 'clientuser1@domain.com', '1995-03-30', 'clientPass1', 'client'),
(7, 'clientuser2@domain.com', '1998-11-19', 'Pass54321', 'client'),
(8, 'adminuser2@domain.com', '1983-06-10', 'Admin123', 'admin'),
(9, 'guestuser2@domain.com', '2001-04-25', 'Guest4321', 'guest'),
(10, 'clientuser3@domain.com', '1992-02-14', 'MyPassword1', 'client');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id_products`);

--
-- Indexes for table `purchases`
--
ALTER TABLE `purchases`
  ADD PRIMARY KEY (`id_purchase`),
  ADD KEY `id_users` (`id_users`),
  ADD KEY `id_product` (`id_product`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_users`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id_products` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `purchases`
--
ALTER TABLE `purchases`
  MODIFY `id_purchase` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id_users` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `purchases`
--
ALTER TABLE `purchases`
  ADD CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`id_users`) REFERENCES `users` (`id_users`) ON DELETE CASCADE,
  ADD CONSTRAINT `purchases_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_products`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
