-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2021 at 05:25 PM
-- Server version: 5.5.39
-- PHP Version: 5.4.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `connnectozona`
--
CREATE DATABASE IF NOT EXISTS `connnectozona` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `connnectozona`;

-- --------------------------------------------------------

--
-- Table structure for table `create_account_step`
--

CREATE TABLE IF NOT EXISTS `create_account_step` (
`no` int(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(200) NOT NULL,
  `otp_code` varchar(255) NOT NULL,
  `otp_valid_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- Table structure for table `friends`
--

CREATE TABLE IF NOT EXISTS `friends` (
`no` int(11) NOT NULL,
  `user_id` varchar(55) NOT NULL,
  `friend_id` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `profiles`
--

CREATE TABLE IF NOT EXISTS `profiles` (
`no` int(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `user_id` varchar(200) NOT NULL,
  `country` varchar(50) NOT NULL DEFAULT 'NA',
  `friends` varchar(200) NOT NULL DEFAULT 'NA',
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `profiles`
--

INSERT INTO `profiles` (`no`, `email`, `user_id`, `country`, `friends`, `created_date`) VALUES
(11, 'pcic095@gmail.com', '7814907645', 'NA', 'NA', '2021-05-10 14:58:17'),
(12, 'pcic067@gmail.com', '2308791981', 'NA', 'NA', '2021-05-10 15:06:24');

-- --------------------------------------------------------

--
-- Table structure for table `requests_friends`
--

CREATE TABLE IF NOT EXISTS `requests_friends` (
`no` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `friend_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
`no` int(11) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `email` varchar(200) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  `api_key` varchar(100) NOT NULL,
  `otp_code` varchar(200) NOT NULL,
  `otp_valid_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`no`, `user_id`, `email`, `username`, `password`, `api_key`, `otp_code`, `otp_valid_time`) VALUES
(7, '7814907645', 'pcic095@gmail.com', '', 'bcc15bf701b4fed1538d2fa3cdccf2cb5a00534007f74843e10e433213d4e5f5', 'fec0c599e53242063d410584ab2593a05b475f4a2d8a5ac2b1cf98072d78c72d', '07c34db0f9b498e6d52c5de8ecf9fd8464fefc92f17b8cc0dacb53f87b4776bc', '2021-05-11 01:00:03'),
(8, '2308791981', 'pcic067@gmail.com', '', 'bcc15bf701b4fed1538d2fa3cdccf2cb5a00534007f74843e10e433213d4e5f5', 'c35e0d9e4045cfc6c0083f3bd90de56896b52d406d98198a7ab9edc68c7e7a7b', 'b4a3f79c4ccf5b4b929d80195cd1b0ffb4700e33e53f617d2d53b1e4b8eb0a8f', '2021-05-11 01:07:26');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `create_account_step`
--
ALTER TABLE `create_account_step`
 ADD PRIMARY KEY (`no`);

--
-- Indexes for table `friends`
--
ALTER TABLE `friends`
 ADD PRIMARY KEY (`no`);

--
-- Indexes for table `profiles`
--
ALTER TABLE `profiles`
 ADD PRIMARY KEY (`no`), ADD UNIQUE KEY `username` (`email`,`user_id`);

--
-- Indexes for table `requests_friends`
--
ALTER TABLE `requests_friends`
 ADD PRIMARY KEY (`no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
 ADD PRIMARY KEY (`no`), ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `create_account_step`
--
ALTER TABLE `create_account_step`
MODIFY `no` int(255) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `friends`
--
ALTER TABLE `friends`
MODIFY `no` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `profiles`
--
ALTER TABLE `profiles`
MODIFY `no` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `requests_friends`
--
ALTER TABLE `requests_friends`
MODIFY `no` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
MODIFY `no` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
