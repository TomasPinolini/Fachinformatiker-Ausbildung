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
-- Database: `5-wd&dbd-3`
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
(1, 1, 2, '2023-01-15 13:23:00'),
(2, 2, 3, '2023-02-20 09:45:00'),
(3, 1, 5, '2023-03-05 15:30:00'),
(4, 3, 1, '2023-04-18 09:15:00'),
(5, 4, 6, '2023-05-22 07:50:00'),
(6, 5, 7, '2023-06-10 15:40:00'),
(7, 6, 8, '2023-07-14 17:30:00'),
(8, 7, 4, '2023-08-01 11:10:00'),
(9, 8, 9, '2023-08-25 06:55:00'),
(10, 9, 10, '2023-09-15 16:20:00'),
(16, 1, 2, '2025-01-07 10:28:45'),
(17, 1, 3, '2025-01-07 10:28:45'),
(18, 1, 5, '2025-01-07 10:28:45'),
(19, 1, 6, '2025-01-07 10:28:45');

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
(2, 'tota@gmail.com', '0001-01-01', '321', 'client'),
(3, 'tomaspinolini2003@gmail.com', '2022-02-22', '123321pino', 'client'),
(4, 'adminmaster@domain.com', '1980-12-01', 'admin2021', 'admin'),
(5, 'guestuser1@domain.com', '2000-07-21', 'guest987', 'guest'),
(6, 'totin@gmail.com', '2003-01-01', '123ewq', 'admin'),
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
  MODIFY `id_purchase` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

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
