-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 01. Mai 2019 um 14:01
-- Server-Version: 10.1.38-MariaDB
-- PHP-Version: 7.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `scheschbot`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `aggronymes`
--

CREATE TABLE `aggronymes` (
  `aggronyme_id` int(11) NOT NULL,
  `aggronyme` text NOT NULL,
  `fk_word_type_id` int(11) NOT NULL,
  `fk_word_article_id` int(11) DEFAULT NULL,
  `number_of_admin_votes` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `aggronymes`
--

INSERT INTO `aggronymes` (`aggronyme_id`, `aggronyme`, `fk_word_type_id`, `fk_word_article_id`, `number_of_admin_votes`) VALUES
(1, 'abartig', 1, NULL, 2),
(2, 'assozial', 1, NULL, 2),
(3, 'ägglhaft', 1, NULL, 2),
(4, 'balancelos', 1, NULL, 2),
(5, 'belanglos', 1, NULL, 2),
(6, 'blöd', 1, NULL, 2),
(7, 'charismatisch', 1, NULL, 2),
(8, 'deppert', 1, NULL, 2),
(9, 'dumm', 1, NULL, 2),
(10, 'doof', 1, NULL, 2),
(11, 'egglhaft', 1, NULL, 2),
(12, 'ersetzbar', 1, NULL, 2),
(13, 'frauenfeindlich', 1, NULL, 2),
(14, 'hochnäsig', 1, NULL, 2),
(15, 'idiotisch', 1, NULL, 2),
(16, 'ignorant', 1, NULL, 2),
(17, 'joggend', 1, NULL, 2),
(18, 'kannibalistisch', 1, NULL, 2),
(19, 'lieblos', 1, NULL, 2),
(20, 'mickrig', 1, NULL, 2),
(21, 'Monokel', 2, 3, 2),
(22, 'nebulös', 1, NULL, 2),
(23, 'oval', 1, NULL, 2),
(24, 'Obazda', 2, 1, 2),
(25, 'Orange', 2, 2, 2),
(26, 'Omen', 2, 3, 2),
(27, 'öd', 1, NULL, 2),
(28, 'phasenverschoben', 1, NULL, 2),
(29, 'qualifiziert', 1, NULL, 2),
(30, 'respektlos', 1, NULL, 2),
(31, 'Scheiß', 2, 1, 2),
(32, 'Sauklaue', 2, 2, 2),
(33, 'transatlantisch', 1, NULL, 2),
(34, 'Taliban', 2, 1, 2),
(35, 'unterirdisch', 1, NULL, 2),
(36, 'überlebenswichtig', 1, NULL, 2),
(37, 'verflucht', 1, NULL, 2),
(38, 'weiß', 1, NULL, 2),
(39, 'weis', 1, NULL, 2),
(40, 'Yuppie verachtend', 1, NULL, 2),
(41, 'unrasiert', 1, NULL, 2),
(42, 'faschistisch', 1, NULL, 2),
(43, 'rassistisch', 1, NULL, 2),
(44, 'Lockenkopf', 2, 1, 2),
(45, 'Nacktschnecke', 2, 2, 2),
(46, 'ramponiert', 1, NULL, 2),
(47, 'Logistikexperte', 2, 1, 2),
(48, 'Lappen', 2, 1, 2),
(49, 'Lulatsch', 2, 1, 2),
(50, 'Luder', 2, 3, 2),
(51, 'Loser', 2, 1, 2),
(52, 'Kotklumpen', 2, 1, 2),
(53, 'Kaschberkupf', 2, 1, 2),
(54, 'Koksfresse', 2, 2, 2),
(55, 'Kokser', 2, 1, 2),
(56, 'Fettsack', 2, 1, 2),
(57, 'Kaschb0', 2, 1, 2),
(58, 'Bürgermeister', 2, 1, 2),
(59, 'Gerber', 2, 1, 2),
(60, 'adipös', 1, NULL, 2),
(61, 'Dackel', 2, 1, 2),
(62, 'Knecht', 2, 1, 2),
(63, 'Alkoholiker', 2, 1, 2),
(64, 'Saufkopf', 2, 1, 2),
(65, 'Betrunkener', 2, 1, 2),
(66, 'Zauberer', 2, 1, 2),
(67, 'Werwolf', 2, 1, 2),
(68, 'Serienkiller', 2, 1, 2),
(69, 'Knasti', 2, 1, 2),
(70, 'Jeffrey', 2, 1, 2),
(71, 'Jugendlicher', 2, 1, 2),
(72, 'Junkie', 2, 1, 2),
(73, 'Jodler', 2, 1, 2),
(74, 'Jockel', 2, 1, 2),
(75, 'Steckdosenbefruchter', 2, 1, 2),
(76, 'Jogger', 2, 1, 2),
(77, 'Vollidiot', 2, 1, 2),
(78, 'Bastard', 2, 1, 2),
(79, 'Intimschnüffler', 2, 1, 2),
(80, 'Ire', 2, 1, 2),
(81, 'Inder', 2, 1, 2),
(82, 'Mietarsch', 2, 1, 2),
(83, 'Killer', 2, 1, 2),
(84, 'Arschgeburt', 2, 2, 2),
(85, 'Mundgeburt', 2, 2, 2),
(86, 'Eierkopf', 2, 1, 2),
(87, 'Ehrloser', 2, 1, 2),
(88, 'Fickbratze', 2, 2, 2),
(89, 'Fickfresse', 2, 2, 2),
(90, 'Fotze', 2, 2, 2),
(91, 'Ficker', 2, 1, 2),
(92, 'Fanatiker', 2, 1, 2),
(93, 'Faschist', 2, 1, 2),
(94, 'Naturfascho', 2, 1, 2),
(95, 'Furzgesicht', 2, 3, 2),
(96, 'Furz', 2, 1, 2),
(97, 'Fruchtzwerg', 2, 1, 2),
(98, 'Gallmeder', 2, 1, 2),
(99, 'Gartenzwerg', 2, 1, 2),
(100, 'schlau', 1, NULL, 2),
(101, 'Krüppel', 2, 1, 2),
(102, 'stur', 1, NULL, 2),
(103, 'Gammler', 2, 1, 2),
(104, 'Wichser', 2, 1, 2),
(105, 'Affenkopf', 2, 1, 2),
(106, 'Grünschnabel', 2, 1, 2),
(107, 'Buttergolem', 2, 1, 2),
(108, 'Gollum', 2, 1, 2),
(109, 'Hans!', 2, 1, 2),
(110, 'Hans', 2, 1, 2),
(111, 'Glatzkopf', 2, 1, 2),
(112, 'Gubbel', 2, 1, 2),
(113, 'Spast', 2, 1, 2),
(114, 'Halskrause', 2, 2, 2),
(115, 'billig', 1, NULL, 2),
(116, 'Hurensohn', 2, 1, 2),
(117, 'Hurenbock', 2, 1, 2),
(118, 'Hohlkopf', 2, 1, 2),
(119, 'Hohlbirne', 2, 2, 2),
(120, 'Halbtagsjobber', 2, 1, 2),
(121, 'Hartzler', 2, 1, 2),
(122, 'Honk', 2, 1, 2),
(123, 'Ingwer-Konsument', 2, 1, 2),
(124, 'Ingwerfascho', 2, 1, 2),
(125, 'imaginär', 1, NULL, 2),
(126, 'Irdischer', 2, 1, 2),
(127, 'Idiot', 2, 1, 2),
(128, 'Implantat', 2, 3, 2),
(129, 'Irrer', 2, 1, 2),
(130, 'Intelligenzbestie', 2, 2, 2),
(131, 'Inzestkind', 2, 3, 2),
(132, '0lmaddin', 2, 1, 2),
(133, 'Sachse', 2, 1, 2),
(134, 'Massakermanfred', 2, 1, 2),
(135, 'Schwachkupf', 2, 1, 2),
(136, 'Oachkatzlschwoaf', 2, 1, 2),
(137, 'Lunatiker', 2, 1, 2),
(138, 'Dorfdepp', 2, 1, 2),
(139, 'Sachsenbewohner', 2, 1, 2),
(140, 'Nazi', 2, 1, 2),
(141, 'Pegidawähler', 2, 1, 2),
(142, 'rainst', 1, NULL, 2),
(143, 'widerwertig', 1, NULL, 2),
(144, 'widerwärtig', 1, NULL, 2),
(145, 'sabbernd', 1, NULL, 2),
(146, 'Wiederkäuer', 2, 1, 2),
(147, 'rekursiv', 1, NULL, 2),
(148, 'reinst', 1, NULL, 2),
(149, 'Meest0', 2, 1, 2),
(150, 'Nudel-Experte', 2, 1, 2),
(151, 'Obba', 2, 1, 2),
(152, 'Penetrator', 2, 1, 2),
(153, 'Penedrant', 2, 1, 2),
(154, 'Panadengurke', 2, 2, 2),
(155, 'Alpecin-Experte', 2, 1, 2),
(156, 'Gurke', 2, 2, 2),
(157, 'Obstverweigerer', 2, 1, 2),
(158, 'Penner', 2, 1, 2),
(159, 'Oberbratze', 2, 2, 2),
(160, 'Penis', 2, 1, 2),
(161, 'ausgeschieden', 1, NULL, 2),
(162, 'Unzucht', 2, 2, 2),
(163, 'Untermensch', 2, 1, 2),
(164, 'Urologe', 2, 1, 2),
(165, 'Unfallgaffer', 2, 1, 2),
(166, 'gaffend', 1, NULL, 2),
(167, 'verunfallt', 1, NULL, 2),
(168, 'Statist', 2, 1, 2),
(169, 'Arsch', 2, 1, 2),
(170, 'Dämon', 2, 1, 2),
(171, 'Wambo', 2, 1, 2),
(172, 'Arschgöttin', 2, 2, 2),
(173, 'Daifl', 2, 1, 2),
(174, 'Platzhalter', 2, 1, 2),
(175, 'Klatsche', 2, 2, 2),
(176, 'Gemüseklatsche', 2, 2, 2),
(177, 'verfault', 1, NULL, 2),
(178, 'arschig', 1, NULL, 2),
(179, 'verdammt', 1, NULL, 2),
(180, 'verdorben', 1, NULL, 2),
(181, 'Fleischhackende-Zerhacker', 2, 1, 2),
(182, 'Zerhacker', 2, 1, 2),
(183, 'Hackfleisch hassend', 1, NULL, 2),
(184, 'Hackfleisch hackend', 1, NULL, 2),
(185, 'Kackfleisch kackend', 1, NULL, 2),
(186, 'Faschosau', 2, 2, 2),
(187, 'Zuhälter', 2, 1, 2),
(188, 'Amputator', 2, 1, 2),
(189, 'Zühorer', 2, 1, 2),
(190, 'Sack', 2, 1, 2),
(191, 'Sackgesicht', 2, 3, 2),
(192, 'Hitler', 2, 1, 2),
(193, 'Stalin', 2, 1, 2),
(195, 'Vogel', 2, 1, 2),
(196, 'Verbrecher', 2, 1, 2),
(197, 'Krimineller', 2, 1, 2),
(198, 'Ziegelsteingesicht', 2, 3, 2),
(200, 'Kevin', 2, 1, 2),
(201, 'entfremdet', 1, NULL, 2),
(202, 'Önn0', 2, 1, 2),
(203, 'obdachlos', 1, NULL, 2),
(204, 'mittellos', 1, NULL, 2),
(205, 'enteignet', 1, NULL, 2),
(206, 'nervig', 1, NULL, 2),
(207, 'Doldi', 2, 1, 2),
(208, 'Dolln', 2, 2, 2),
(209, 'Dummkopf', 2, 1, 2),
(210, 'Spasti', 2, 1, 2),
(211, 'Spacko', 2, 1, 2),
(212, 'daumendick', 1, NULL, 2),
(213, 'Dullnraamer', 2, 1, 2),
(214, 'Kotzbrocken', 2, 1, 2),
(215, 'Crackhure', 2, 2, 2),
(216, 'Cracknutte', 2, 2, 2),
(217, 'Wackeldackel', 2, 1, 2),
(218, 'Christ', 2, 1, 2),
(219, 'Clown', 2, 1, 2),
(220, '0ndi', 2, 1, 2),
(221, 'Laborratte', 2, 2, 2),
(222, 'Ratte', 2, 2, 2),
(223, 'Endzeitkrieger', 2, 1, 2),
(224, 'Charmebolzen', 2, 1, 2),
(225, 'Haarhälter', 2, 1, 2),
(226, 'Weem0-Eem0', 2, 1, 2),
(227, 'Spei0', 2, 1, 2),
(228, 'Kurzhalsgiraffe', 2, 2, 2),
(229, 'Hund', 2, 1, 2),
(230, 'Trauerkloß (mit Soß)', 2, 1, 2),
(231, 'Totgeburt', 2, 2, 2),
(232, 'Trantüte', 2, 2, 2),
(233, 'Unfallopfer', 2, 3, 2),
(234, 'Rainer', 2, 1, 2),
(235, 'Twilight-Fan', 2, 1, 2),
(236, 'Mederkupf', 2, 1, 2),
(237, 'Speichellecker', 2, 1, 2),
(238, 'Urzeitmensch', 2, 1, 2),
(239, 'unfähig', 1, NULL, 2),
(240, 'hässlich', 1, NULL, 2),
(241, 'Untoter', 2, 1, 2),
(242, 'uralt', 1, NULL, 2),
(243, 'Hackfresse', 2, 2, 2),
(244, 'Ungetier', 2, 3, 2),
(245, 'Insekt', 2, 3, 2),
(246, 'Kakerlake', 2, 2, 2),
(247, 'Unfallgesicht', 2, 3, 2),
(248, 'ungeeignet', 1, NULL, 2),
(249, 'Orang Utan', 2, 1, 2),
(250, 'ungebildet', 1, NULL, 2),
(251, 'unerwünscht', 1, NULL, 2),
(252, 'ungewollt', 1, NULL, 2),
(253, 'Untier', 2, 3, 2),
(254, 'Dachdegg0', 2, 1, 2),
(255, 'Unmensch', 2, 1, 2),
(256, 'gut', 1, NULL, 2),
(257, 'teuflisch', 1, NULL, 2),
(258, 'Trottel', 2, 1, 2),
(259, 'Transe', 2, 2, 2),
(260, 'Tölpel', 2, 1, 2),
(261, 'Toilettentieftaucher', 2, 1, 2),
(262, 'Tunte', 2, 2, 2),
(263, 'Tussi', 2, 2, 2),
(264, 'taub', 1, NULL, 2),
(265, 'tatsächlich', 1, NULL, 2),
(266, 'tabulös', 1, NULL, 2),
(267, 'Tor', 2, 1, 2),
(268, 'töricht', 1, NULL, 2),
(269, 'Torfkopf', 2, 1, 2),
(270, 'Nudel-Suchti', 2, 1, 2),
(271, 'toll', 1, NULL, 2),
(272, 'Narr', 2, 1, 2),
(273, 'närrisch', 1, NULL, 2),
(274, 'notgail', 1, NULL, 2),
(275, 'gail', 1, NULL, 2),
(276, 'notgeil', 1, NULL, 2),
(277, 'Kleberschnüffler', 2, 1, 2),
(278, 'Benzinschnüffler', 2, 1, 2),
(279, 'Klebstoffschnüffler', 2, 1, 2),
(280, 'Kleistermeister', 2, 1, 2),
(281, 'behäbig', 1, NULL, 2),
(282, 'schläfrig', 1, NULL, 2),
(283, 'durchlöchert', 1, NULL, 2),
(284, 'Depp', 2, 1, 2),
(285, 'klug', 1, NULL, 2),
(286, 'unklug', 1, NULL, 2),
(287, 'Ranzler', 2, 1, 2),
(288, 'Lackaffe', 2, 1, 2),
(289, 'zerquetscht', 1, NULL, 2),
(290, 'dämlich', 1, NULL, 2),
(291, 'Dämlack', 2, 1, 2),
(292, 'Vollpfosten', 2, 1, 2),
(293, 'verfickt', 1, NULL, 2),
(294, 'Vollspast', 2, 1, 2),
(295, 'Volldepp', 2, 1, 2),
(296, 'Verräter', 2, 1, 2),
(297, 'verräterisch', 1, NULL, 2),
(298, 'formlos', 1, NULL, 2),
(300, 'fabulös', 1, NULL, 2),
(301, 'Mongo', 2, 1, 2),
(302, 'Hure', 2, 2, 2),
(303, 'Nutte', 2, 2, 2),
(304, 'Bitch', 2, 2, 2),
(305, 'Vollhorst', 1, NULL, 2),
(306, 'Ranzl0', 2, 1, 2),
(307, 'schier unermesslich', 1, NULL, 2),
(308, 'schesch', 1, NULL, 2),
(309, 'dreist', 1, NULL, 2),
(310, 'Kackspast', 2, 1, 2),
(311, 'Missgeburt', 2, 2, 2),
(312, 'wunderbar', 1, NULL, 2),
(313, 'wild', 1, NULL, 2),
(314, 'Wunderkind', 2, 3, 2),
(315, 'Wunderhure', 2, 2, 2),
(316, 'Wanderhure', 2, 2, 2),
(317, 'geistlos', 1, NULL, 2),
(318, 'welkend', 1, NULL, 2),
(319, 'wertlos', 1, NULL, 2),
(320, 'Warzenschwein', 2, 3, 2),
(321, 'wählerisch', 1, NULL, 2),
(322, 'Ork', 2, 1, 2),
(323, 'Boi', 2, 1, 2),
(324, 'cool', 1, NULL, 2),
(325, 'zermürbt', 1, NULL, 2),
(326, 'wirr', 1, NULL, 2),
(327, 'Assi', 2, 1, 2),
(328, 'Choleriker', 2, 1, 2),
(329, 'cholerisch', 1, NULL, 2),
(330, 'fanatisch', 1, NULL, 2),
(331, 'Cholesterin-verseucht', 1, NULL, 2),
(332, 'langweilig', 1, NULL, 2),
(333, 'irrelevant', 1, NULL, 2),
(334, 'Traumtänzer', 2, 1, 2),
(335, 'fantasielos', 1, NULL, 2),
(336, 'Heini', 2, 1, 2),
(337, 'Fantast', 2, 1, 2),
(338, 'Analphabet', 2, 1, 2),
(339, 'nais', 1, NULL, 2),
(342, 'halbgar', 1, NULL, 2),
(343, 'unlustig', 1, NULL, 2),
(344, 'ungboren', 1, NULL, 2),
(345, 'egoistisch', 1, NULL, 2),
(346, 'Fischkopf', 2, 1, 2),
(347, 'glanzlos', 1, NULL, 2),
(348, 'garniert', 1, NULL, 2),
(349, 'Bruchpilot', 2, 1, 2),
(350, 'paniert', 1, NULL, 2),
(351, 'Schleimbeutel', 2, 1, 2),
(352, 'bolschewistisch', 1, NULL, 2),
(353, 'Schleimbejdele', 2, 3, 2),
(354, 'antisemitisch', 1, NULL, 2),
(355, 'Kommunist', 2, 1, 2),
(356, 'Kapitalist', 2, 1, 2),
(357, 'Kapitalistenschwein', 2, 3, 2),
(358, 'Versuchsratte', 2, 2, 2),
(363, 'Sau', 2, 2, 2),
(364, 'Schnarcher', 2, 1, 2),
(365, 'Schnarchkopf', 2, 1, 2),
(366, 'gehirnamputiert', 1, NULL, 2),
(367, 'schwachsinnig', 1, NULL, 2),
(368, 'Schwachkopf', 2, 1, 2),
(369, 'Affe', 2, 1, 2),
(371, 'leider glatzenlos', 1, NULL, 2),
(372, 'in den Mosh geraten', 1, NULL, 2),
(373, 'quälend', 1, NULL, 2),
(374, 'qualvoll', 1, NULL, 2),
(375, 'Qualmaddin', 2, 1, 2),
(376, 'quietschend', 1, NULL, 2),
(377, 'Orangentimo', 2, 1, 2),
(378, 'quietschig', 1, NULL, 2),
(379, 'Quatschkopf', 2, 1, 2),
(380, 'quengelnd', 1, NULL, 2),
(381, 'Kind', 2, 3, 2),
(382, 'quatschend', 1, NULL, 2),
(383, 'Yeti', 2, 1, 2),
(384, 'Yogi', 2, 1, 2),
(386, 'yttriumhaltig', 1, NULL, 2),
(387, 'judenfeindlich', 1, NULL, 2),
(388, 'juristisch abgesichert', 1, NULL, 2),
(389, 'nicht jugendfrei', 1, NULL, 2),
(390, 'Zoo-Affe', 2, 1, 2),
(391, 'jähzornig', 1, NULL, 2),
(392, 'jubelnd', 1, NULL, 2),
(393, 'Jünger', 2, 1, 2),
(394, 'jodelnd', 1, NULL, 2),
(395, 'pingelig', 1, NULL, 2),
(396, 'penislos', 1, NULL, 2),
(397, 'penedriert', 1, NULL, 2),
(398, 'Önis', 2, 1, 2),
(399, 'pädagogisch nicht allzu wertvoll', 1, NULL, 2),
(400, 'penetrant', 1, NULL, 2),
(401, 'passiv aggressiv', 1, NULL, 2),
(402, 'passabel', 1, NULL, 2),
(403, 'palästinensisch', 1, NULL, 2),
(404, 'pentagonisch', 1, NULL, 2),
(405, 'parasitär', 1, NULL, 2),
(406, 'Paläontologe', 2, 1, 2),
(407, 'Parasit', 2, 1, 2),
(408, 'passabl', 1, NULL, 2),
(409, 'Paradiesvogel', 2, 1, 2),
(410, 'panisch', 1, NULL, 2),
(412, 'phantasielos', 1, NULL, 2),
(413, 'mafiös', 1, NULL, 2),
(414, 'machtlos', 1, NULL, 2),
(415, 'mangelhaft', 1, NULL, 2),
(416, 'mäßig interessant', 1, NULL, 2),
(417, 'manifestiert', 1, NULL, 2),
(418, 'mederbehaftet', 1, NULL, 2),
(419, 'magersüchtig', 1, NULL, 2),
(420, 'maximal unfähig', 1, NULL, 2),
(421, 'mausetot', 1, NULL, 2),
(422, 'maschinenlesbar', 1, NULL, 2),
(423, 'Klosterpinguin', 2, 1, 2),
(424, 'Klosterkätzchen', 2, 3, 2),
(426, 'mittelfränkisch', 1, NULL, 2),
(427, 'mental instabil', 1, NULL, 2),
(428, 'maulfaul', 1, NULL, 2),
(429, 'mittelfristig lebensgefährdet', 1, NULL, 2),
(431, 'minderjährig', 1, NULL, 2),
(432, 'missmutig', 1, NULL, 2),
(433, 'mutlos', 1, NULL, 2),
(434, 'unmusikalisch', 1, NULL, 2),
(435, 'manierenlos', 1, NULL, 2),
(436, 'taktlos', 1, NULL, 2),
(437, 'Opfer', 2, 3, 2),
(438, 'orientierungslos', 1, NULL, 2),
(439, 'obszön', 1, NULL, 2),
(440, 'osmanisch', 1, NULL, 2),
(441, 'ominös', 1, NULL, 2),
(442, 'Wutbürger', 2, 1, 2),
(443, 'Ödipus', 2, 1, 2),
(444, 'ödipal', 1, NULL, 2),
(445, 'oberflächlich', 1, NULL, 2),
(446, 'besorgt', 1, NULL, 2),
(447, 'ortsgebunden', 1, NULL, 2),
(448, 'Bürger', 2, 1, 2),
(449, 'öd', 1, NULL, 2),
(450, 'omnipräsent', 1, NULL, 2),
(451, 'oberaffengail', 1, NULL, 2),
(452, 'penetriert', 1, NULL, 2),
(453, 'oberaffengeil', 1, NULL, 2),
(454, 'ofenfrisch', 1, NULL, 2),
(455, 'obsolet', 1, NULL, 2),
(456, 'offensiv', 1, NULL, 2),
(457, 'aggressiv', 1, NULL, 2),
(458, 'kubanisch', 1, NULL, 2),
(459, 'kapitalistisch', 1, NULL, 2),
(460, 'maximal kapitalistisch', 1, NULL, 2),
(461, 'Yogameister', 2, 1, 2),
(462, 'aktiv nichts tuend', 1, NULL, 2),
(463, 'miserabl', 1, NULL, 2),
(464, 'mitleiderregend', 1, NULL, 2),
(465, 'Bauerntölpel', 2, 1, 2),
(466, 'unmotiviert', 1, NULL, 2),
(467, 'kegelförmig', 1, NULL, 2),
(468, 'Kehlkopfsänger', 2, 1, 2),
(469, 'labil', 1, NULL, 2),
(470, 'Kulturverweigerer', 2, 1, 2),
(471, 'lethargisch', 1, NULL, 2),
(472, 'leninistisch', 1, NULL, 2),
(473, 'kannibalisch', 1, NULL, 2),
(474, 'Leninist', 2, 1, 2),
(475, 'Lama', 2, 3, 2),
(476, 'lächerlich', 1, NULL, 2),
(477, 'leicht katalogisierbar', 1, NULL, 2),
(478, 'launisch', 1, NULL, 2),
(479, 'lachhaft', 1, NULL, 2),
(480, 'Kochnudel', 2, 2, 2),
(481, 'Lügner', 2, 1, 2),
(482, 'leichtsinnig', 1, NULL, 2),
(483, 'langlebig', 1, NULL, 2),
(484, 'kuuhl', 1, NULL, 2),
(485, 'kurzbeinig', 1, NULL, 2),
(486, 'lobenswert', 1, NULL, 2),
(487, 'kaotisch', 1, NULL, 2),
(488, 'lustgetrieben', 1, NULL, 2),
(489, 'Lustmolch', 2, 1, 2),
(490, 'lästig', 1, NULL, 2),
(491, 'laut', 1, NULL, 2),
(492, 'kalendarisch bestimmbar', 1, NULL, 2),
(493, 'leblos', 1, NULL, 2),
(494, 'Leiche', 2, 2, 2),
(495, 'wütend', 1, NULL, 2),
(497, 'leistungsschwach', 1, NULL, 2),
(498, 'linientreu', 1, NULL, 2),
(499, 'kurzatmig', 1, NULL, 2),
(500, 'lipophil', 1, NULL, 2),
(501, 'lipophob', 1, NULL, 2),
(502, 'pädophil', 1, NULL, 2),
(503, 'hydrophil', 1, NULL, 2),
(504, 'hydrophob', 1, NULL, 2),
(505, 'koalitionslos', 1, NULL, 2),
(506, 'verlogen', 1, NULL, 2),
(507, 'chronisch untervögelt', 1, NULL, 2),
(508, 'chillig', 1, NULL, 2),
(509, 'egomanisch', 1, NULL, 2),
(510, 'egomanisch', 1, NULL, 2),
(511, 'Egomane', 2, 1, 2),
(512, 'chronisch unterbelichtet', 1, NULL, 2),
(513, 'unterbelichtet', 1, NULL, 2),
(514, 'chaotisch', 1, NULL, 2),
(515, 'Chaot', 2, 1, 2),
(516, 'CDU-Wähler', 2, 1, 2),
(518, 'charismatisch-beschränkt', 1, NULL, 2),
(519, 'beschränkt', 1, NULL, 2),
(520, 'clean', 1, NULL, 2),
(521, 'lean', 1, NULL, 2),
(522, 'psychisch krank', 1, NULL, 2),
(523, 'unchristlich', 1, NULL, 2),
(524, 'chirurgisch optimiert', 1, NULL, 2),
(525, 'chancenlos', 1, NULL, 2),
(526, 'identitätlos', 1, NULL, 2),
(527, 'zärtlich', 1, NULL, 2),
(528, 'identitätslos', 1, NULL, 2),
(529, 'zappelig', 1, NULL, 2),
(530, 'Zappel-Philipp', 2, 1, 2),
(531, 'eifersüchtig', 1, NULL, 2),
(532, 'zuckersüß', 1, NULL, 2),
(533, 'charmant', 1, NULL, 2),
(534, 'Charmeur', 2, 1, 2),
(535, 'chemieopatisch', 1, NULL, 2),
(536, 'zügellos', 1, NULL, 2),
(537, 'unzusammenhängend', 1, NULL, 2),
(538, 'zickig', 1, NULL, 2),
(539, 'zottelig', 1, NULL, 2),
(540, 'ziemlich alleinstehend', 1, NULL, 2),
(541, 'zeitlos', 1, NULL, 2),
(542, 'zähflüssig', 1, NULL, 2),
(543, 'zinslos', 1, NULL, 2),
(544, 'sehr ziemlich', 1, NULL, 2),
(545, 'äußerst ziemlich', 1, NULL, 2),
(546, 'zerknirscht', 1, NULL, 2),
(547, 'ziellos', 1, NULL, 2),
(548, 'nutzlos', 1, NULL, 2),
(549, 'zauberhaft', 1, NULL, 2),
(550, 'Zink-verseucht', 1, NULL, 2),
(551, 'äußerst', 1, NULL, 2),
(552, 'ziemlich', 1, NULL, 2),
(553, 'rabiat', 1, NULL, 2),
(554, 'radioaktiv', 1, NULL, 2),
(555, 'ranzig', 1, NULL, 2),
(556, 'rechtsextrem', 1, NULL, 2),
(557, 'rechtsradikal', 1, NULL, 2),
(558, 'rechtspopulistisch', 1, NULL, 2),
(559, 'redundant', 1, NULL, 2),
(560, 'Zuckerwürfel-Kevin', 2, 1, 2),
(561, 'rechtschaffen', 1, NULL, 2),
(562, 'raffgierig', 1, NULL, 2),
(563, 'echt unterbelichtet', 1, NULL, 2),
(564, 'redselig', 1, NULL, 2),
(565, 'rechtlich umstritten', 1, NULL, 2),
(566, 'zierlich', 1, NULL, 2),
(567, 'linkschaffend', 1, NULL, 2),
(568, 'saisonal abweichend', 1, NULL, 2),
(569, 'Linksprecher', 2, 1, 2),
(570, 'raubäuchig', 1, NULL, 2),
(571, 'bärtig', 1, NULL, 2),
(572, 'bartlos', 1, NULL, 2),
(573, 'raubeinig', 1, NULL, 2),
(574, 'Raubein', 2, 3, 2),
(575, 'Zwangsvollstrecker', 2, 1, 2),
(576, 'Räuber', 2, 1, 2),
(577, 'redegewandt', 1, NULL, 2),
(578, 'radikal', 1, NULL, 2),
(579, 'abgöttisch', 1, NULL, 2),
(580, 'gottlos', 1, NULL, 2),
(581, 'farblos', 1, NULL, 2),
(582, 'postfaktisch', 1, NULL, 2),
(583, 'farbenblind', 1, NULL, 2),
(584, 'fummelig', 1, NULL, 2),
(585, 'feig', 1, NULL, 2),
(586, 'fadenscheinig', 1, NULL, 2),
(587, 'feindlich', 1, NULL, 2),
(588, 'Trump', 2, 1, 2),
(589, 'findselig', 1, NULL, 2),
(590, 'Donald', 2, 1, 2),
(591, 'Fummel-Trump', 2, 1, 2),
(592, 'fragwürdig', 1, NULL, 2),
(593, 'Fichtenkletterer', 2, 1, 2),
(594, 'furchtbar', 1, NULL, 2),
(595, 'fruchtbar', 1, NULL, 2),
(596, 'fürchterlich', 1, NULL, 2),
(597, 'furchterregend', 1, NULL, 2),
(598, 'foto-nicht-gen', 1, NULL, 2),
(599, 'fotogen', 1, NULL, 2),
(600, 'flegelhaft', 1, NULL, 2),
(601, 'Rüpel', 2, 1, 2),
(602, 'Flegel', 2, 1, 2),
(603, 'rüpelhaft', 1, NULL, 2),
(604, 'fünfeckig', 1, NULL, 2),
(605, 'federig', 1, NULL, 2),
(606, 'fehlgeleitet', 1, NULL, 2),
(607, 'quirlig', 1, NULL, 2),
(608, 'Quadratschädel', 2, 1, 2),
(609, 'haarig', 1, NULL, 2),
(610, 'haarlos', 1, NULL, 2),
(611, 'unbehaart', 1, NULL, 2),
(612, 'heidnisch', 1, NULL, 2),
(613, 'haltlos', 1, NULL, 2),
(614, 'halbblind', 1, NULL, 2),
(615, 'Saufkopp', 2, 1, 2),
(616, 'hackedicht', 1, NULL, 2),
(617, 'hinterhältig', 1, NULL, 2),
(618, 'hinterfotzig', 1, NULL, 2),
(619, 'hysterisch', 1, NULL, 2),
(620, 'hübsch', 1, NULL, 2),
(621, 'hipp', 1, NULL, 2),
(622, 'hinnehmbar', 1, NULL, 2),
(623, 'HIV-positiv', 1, NULL, 2),
(624, 'halbnackt', 1, NULL, 2),
(625, 'hartnäckig', 1, NULL, 2),
(626, 'harmlos', 1, NULL, 2),
(627, 'halblaut', 1, NULL, 2),
(628, 'halbstark', 1, NULL, 2),
(629, 'talentfrei', 1, NULL, 2),
(630, 'untalentiert', 1, NULL, 2),
(631, 'tödlich verwundet', 1, NULL, 2),
(632, 'tentakelfrei', 1, NULL, 2),
(633, 'tentakelbehaftet', 1, NULL, 2),
(634, 'trunksüchtig', 1, NULL, 2),
(636, 'träg', 1, NULL, 2),
(637, 'trotzig', 1, NULL, 2),
(638, 'turbulent', 1, NULL, 2),
(639, 'totenbleich', 1, NULL, 2),
(640, 'thüringisch', 1, NULL, 2),
(641, 'Thüringer', 2, 1, 2),
(642, 'überaltert', 1, NULL, 2),
(643, 'taubäugig', 1, NULL, 2),
(644, 'Tetrapackweintrinker', 2, 1, 2),
(645, 'dämonisch', 1, NULL, 2),
(646, 'damisch', 1, NULL, 2),
(647, 'drakonisch', 1, NULL, 2),
(648, 'denkfaul', 1, NULL, 2),
(649, 'dalmatinisch', 1, NULL, 2),
(650, 'Birkenhasser', 2, 1, 2),
(651, 'demilitarisiert', 1, NULL, 2),
(652, 'entwaffnet', 1, NULL, 2),
(653, 'entwaffelt', 1, NULL, 2),
(654, 'defragmentiert', 1, NULL, 2),
(655, 'dement', 1, NULL, 2),
(656, 'debil', 1, NULL, 2),
(657, 'dauerkrank', 1, NULL, 2),
(658, 'dadaistisch', 1, NULL, 2),
(659, 'dickleibig', 1, NULL, 2),
(660, 'dickbäuchig', 1, NULL, 2),
(661, 'diesig', 1, NULL, 2),
(662, 'dasig', 1, NULL, 2),
(663, 'intrinsisch determiniert', 1, NULL, 2),
(664, 'Düsenjet-Badewanne', 2, 2, 2),
(665, 'verschlafen', 1, NULL, 2),
(666, 'vergammelt', 1, NULL, 2),
(667, 'verwundbar', 1, NULL, 2),
(668, 'vergesslich', 1, NULL, 2),
(669, 'veraltet', 1, NULL, 2),
(670, 'verantwortungslos', 1, NULL, 2),
(671, 'vaterlos', 1, NULL, 2),
(672, 'verdächtig', 1, NULL, 2),
(673, 'verstörend', 1, NULL, 2),
(674, 'versaut', 1, NULL, 2),
(675, 'vorbestraft', 1, NULL, 2),
(676, 'vorverdaut', 1, NULL, 2),
(677, 'vorgekaut', 1, NULL, 2),
(678, 'därbe faul', 1, NULL, 2),
(679, 'derbe faul', 1, NULL, 2),
(680, 'vermessen', 1, NULL, 2),
(681, 'darum völlig unterbelichtet', 1, NULL, 2),
(682, 'daumenlutschend', 1, NULL, 2),
(683, 'gedankenlos', 1, NULL, 2),
(684, 'gehässig', 1, NULL, 2),
(685, 'widerlich', 1, NULL, 2),
(686, 'galvanisch nicht zuverlässig', 1, NULL, 2),
(687, 'gallig', 1, NULL, 2),
(688, 'gashaltig', 1, NULL, 2),
(689, 'garstig', 1, NULL, 2),
(690, 'gechillt', 1, NULL, 2),
(691, 'ganz faul', 1, NULL, 2),
(692, 'ganz schön faul', 1, NULL, 2),
(693, 'säbelbeinig', 1, NULL, 2),
(694, 'Suchti', 2, 1, 2),
(695, 'sarkastisch', 1, NULL, 2),
(696, 'sexistisch', 1, NULL, 2),
(697, 'geschmacklos', 1, NULL, 2),
(698, 'sexbesessen', 1, NULL, 2),
(699, 'schlecht integriert', 1, NULL, 2),
(700, 'schlecht', 1, NULL, 2),
(701, 'senil', 1, NULL, 2),
(702, 'sau lustig', 1, NULL, 2),
(703, 'saudämlich', 1, NULL, 2),
(704, 'seelenlos', 1, NULL, 2),
(705, 'satanistisch', 1, NULL, 2),
(706, 'stillos', 1, NULL, 2),
(707, 'saftig', 1, NULL, 2),
(708, 'zynisch', 1, NULL, 2),
(709, 'Zyniker', 2, 1, 2),
(710, 'atemlos', 1, NULL, 2),
(711, 'Hirni', 2, 1, 2),
(712, 'säkular', 1, NULL, 2),
(713, 'suizidgefährdet', 1, NULL, 2),
(714, 'stoisch', 1, NULL, 2),
(715, 'steinalt', 1, NULL, 2),
(716, 'sportlich', 1, NULL, 2),
(717, 'unsportlich', 1, NULL, 2),
(718, 'Salmonelle', 2, 2, 2),
(719, 'sprachlos', 1, NULL, 2),
(720, 'splitterfasernackt', 1, NULL, 2),
(721, 'nackt', 1, NULL, 2),
(722, 'sandig', 1, NULL, 2),
(723, 'unbegabt', 1, NULL, 2),
(724, 'Lidl-Fleischsalat-Fresser', 2, 1, 2),
(725, 'banal', 1, NULL, 2),
(726, 'schadenfroh', 1, NULL, 2),
(727, 'schleimig', 1, NULL, 2),
(728, 'berufsunfähig', 1, NULL, 2),
(729, 'schelmisch', 1, NULL, 2),
(730, 'Schelm', 2, 1, 2),
(731, 'Schlemil', 2, 1, 2),
(732, 'Schmock', 2, 1, 2),
(733, 'bedürftig', 1, NULL, 2),
(734, 'bemitleidenswert', 1, NULL, 2),
(735, 'programmier technisch unbegabt', 1, NULL, 2),
(736, 'Kapellleiter', 2, 1, 2),
(737, 'bibliophob', 1, NULL, 2),
(738, 'Blaskapellenleiter', 2, 1, 2),
(739, 'bitchig', 1, NULL, 2),
(740, 'bibeltreu', 1, NULL, 2),
(741, 'bibliophil', 1, NULL, 2),
(742, 'bargeldlos', 1, NULL, 2),
(743, 'bedauerlich', 1, NULL, 2),
(744, 'knochenlos', 1, NULL, 2),
(745, 'berüchtigt', 1, NULL, 2),
(746, 'rückgratlos', 1, NULL, 2),
(747, 'berühmt berüchtigt', 1, NULL, 2),
(748, 'schwanger', 1, NULL, 2),
(749, 'bedenklich', 1, NULL, 2),
(750, 'fett', 1, NULL, 2),
(751, 'eher schwammig', 1, NULL, 2),
(752, 'bedeutungslos', 1, NULL, 2),
(753, 'bayrisch', 1, NULL, 2),
(755, 'barfüßig', 1, NULL, 2),
(756, 'Bausatz-Freddy', 2, 1, 2),
(757, 'rein', 1, NULL, 2),
(758, 'rain', 1, NULL, 2),
(761, 'Barfuß-0ndi', 2, 1, 2),
(762, 'Quatschtütenranzler', 2, 1, 2),
(763, 'Hampelmann', 2, 1, 2),
(764, 'Blechkassum', 2, 3, 2),
(765, 'Keck', 2, 1, 2),
(766, 'x-beliebig', 1, NULL, 2),
(767, 'Xanthippe', 2, 2, 2),
(768, 'O-beinig', 1, NULL, 2),
(769, 'X-beinig', 1, NULL, 2),
(770, 'Xavier Naidoo-Fan', 2, 1, 2),
(771, 'Xavier-Glatze', 2, 2, 2),
(772, 'xenophob', 1, NULL, 2),
(773, 'Quintenzirkel-Hasser', 2, 1, 2),
(774, 'Hendlmaddin', 2, 1, 2),
(775, 'Kleinkünstler', 2, 1, 2),
(776, 'aus Vach stammend', 1, NULL, 2),
(777, 'Bachmederer praktizierend', 1, NULL, 2),
(779, 'Höhlenmensch', 2, 1, 2),
(780, 'Höllenmensch', 2, 1, 2),
(781, 'Hinterwäldler', 2, 1, 2),
(782, 'Blödmann', 2, 1, 2),
(783, 'Annegret', 2, 2, 2),
(784, 'Arschkuh', 2, 2, 2),
(785, 'Klaus', 2, 1, 2),
(786, 'Yuppie', 2, 1, 2),
(787, 'unqualifiziert', 1, NULL, 2),
(788, 'inkontinent', 1, NULL, 2),
(789, 'Kräuterwastl', 2, 1, 2),
(790, 'schwach', 1, NULL, 2),
(791, 'stumpfsinnig', 1, NULL, 2),
(792, 'Schleimer', 2, 1, 2),
(793, 'Schwachmat', 2, 1, 2),
(794, 'Doofbacke', 2, 2, 2),
(795, 'Sturkopf', 2, 1, 2),
(797, 'Fotzenknecht', 2, 1, 2);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `answer_inputs`
--

CREATE TABLE `answer_inputs` (
  `input_id` int(11) NOT NULL,
  `input` text NOT NULL,
  `has_text_before` tinyint(1) NOT NULL DEFAULT '0',
  `has_text_after` tinyint(1) NOT NULL DEFAULT '0',
  `is_question` tinyint(1) NOT NULL DEFAULT '0',
  `contains_specialchars` tinyint(1) NOT NULL DEFAULT '0',
  `sympathy_percentage_gain` int(3) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `answer_inputs`
--

INSERT INTO `answer_inputs` (`input_id`, `input`, `has_text_before`, `has_text_after`, `is_question`, `contains_specialchars`, `sympathy_percentage_gain`) VALUES
(1, 'bot', 0, 0, 0, 0, 2),
(2, 'lustig lustig', 0, 0, 0, 0, 0),
(3, 'schnauze', 0, 1, 0, 0, -5),
(4, 'freiwild', 1, 1, 0, 0, 1),
(5, 'ingwer', 1, 1, 0, 0, -1),
(6, 'nusch', 1, 1, 0, 0, 1),
(7, 'joschi', 1, 1, 0, 0, 1),
(8, 'janosch', 1, 1, 0, 0, 1),
(9, 'josch', 1, 1, 0, 0, 1),
(10, 'subb0', 1, 1, 0, 0, 0),
(11, 'sybb0', 1, 1, 0, 0, 0),
(12, 'kaschber', 1, 1, 0, 0, -3),
(13, 'der önner', 1, 0, 0, 0, 0),
(14, 'der önn0', 1, 0, 0, 0, 0),
(15, 'legg0', 1, 1, 0, 0, 0),
(16, 'diese hier', 0, 0, 0, 0, 0),
(17, 'ja bitte', 0, 0, 0, 0, 0),
(18, 'danke', 0, 1, 0, 0, 1),
(19, 'dankek', 0, 1, 0, 0, 1),
(20, 'die mit der mühle', 0, 0, 0, 0, 0),
(21, 'genau', 0, 0, 0, 0, 0),
(22, 'sgeht', 1, 1, 0, 0, 1),
(23, 'hey hey', 0, 0, 0, 0, 0),
(24, 'heyhey', 0, 0, 0, 0, 0),
(25, 'ja ja', 0, 0, 0, 0, 0),
(26, 'jaja', 0, 0, 0, 0, 0),
(29, 'schesch', 1, 1, 0, 0, 2),
(30, 'offensichtlich', 1, 1, 0, 0, 0),
(32, 'denken sie nicht mit', 0, 0, 0, 0, 0),
(33, 'wer hat uns verraten', 0, 0, 0, 0, 0),
(34, 'mess0', 1, 1, 0, 0, 1),
(35, 'clean', 1, 0, 0, 0, 0),
(36, 'so true', 0, 0, 0, 0, 0),
(37, 'sotrue', 0, 0, 0, 0, 0),
(38, 'kek', 0, 0, 0, 0, 0),
(39, 'essen', 1, 1, 0, 0, 0),
(40, 'sn', 1, 1, 0, 0, 0),
(41, 'uwe', 1, 1, 0, 0, 1),
(42, 'bist du dumm', 0, 0, 0, 0, -3),
(43, 'du isst wie ein schwein', 1, 0, 0, 0, 0),
(44, 'feierabend', 1, 1, 0, 0, 0),
(45, 'feieramd', 1, 1, 0, 0, 0),
(46, 'heftig deftig', 0, 0, 0, 0, 0),
(47, 'naise', 1, 1, 0, 0, 0),
(48, 'unsinn', 1, 1, 0, 0, 0),
(49, 'blödsinn', 0, 0, 0, 0, 0),
(50, 'hoch die hände', 1, 1, 0, 0, 0),
(51, 'linke hand', 0, 0, 0, 0, 0),
(52, 'rechte hand', 0, 0, 0, 0, 0),
(53, 'linkes bein', 0, 0, 0, 0, 0),
(54, 'rechtes bein', 0, 0, 0, 0, 0),
(55, 'önnen', 1, 0, 0, 0, 2),
(56, 'nacht', 0, 0, 0, 0, 2),
(57, 'n8', 0, 0, 0, 0, 2),
(58, 'gn8', 0, 0, 0, 0, 2),
(59, 'nein', 0, 0, 0, 0, 0),
(60, 'oh', 0, 0, 0, 0, 0),
(62, 'huff', 0, 0, 0, 0, -3),
(63, 'muss man wissen', 1, 0, 0, 0, 0),
(64, 'wer weiß das', 1, 0, 0, 0, 0),
(65, 'wochenende', 1, 1, 0, 0, 5),
(66, 'witzig', 1, 1, 0, 0, 0),
(68, 'frage', 1, 0, 0, 0, 4),
(69, ':v', 0, 0, 0, 1, 0),
(70, ':V', 0, 0, 0, 1, 0),
(71, 'v:', 0, 0, 0, 1, 0),
(72, 'V:', 0, 0, 0, 1, 0),
(73, 'D:', 0, 0, 0, 1, 0),
(74, 'wie viele', 0, 1, 1, 0, 0),
(75, 'wie viel', 0, 1, 1, 0, 0),
(76, 'wieso', 0, 1, 1, 0, 0),
(77, 'was', 0, 1, 1, 0, 0),
(78, 'wie', 0, 1, 1, 0, 0),
(79, 'weshalb', 0, 1, 1, 0, 0),
(80, 'warum', 0, 1, 1, 0, 0),
(81, 'weswegen', 0, 1, 1, 0, 0),
(82, 'wozu', 0, 1, 1, 0, 0),
(90, 'kaschb0', 1, 1, 0, 0, -3),
(91, 'wer war mit dabei', 0, 0, 0, 0, 0),
(92, 'schade', 0, 0, 0, 0, 0),
(93, 'wofür', 0, 1, 1, 0, 0),
(94, 'nice', 1, 1, 0, 0, 0),
(100, 'welcher', 0, 1, 1, 0, 0),
(101, 'welches', 0, 1, 1, 0, 0),
(102, 'welchen', 0, 1, 1, 0, 0),
(103, 'welchem', 0, 1, 1, 0, 0),
(104, 'welche', 0, 1, 1, 0, 0),
(108, 'wann', 0, 0, 0, 0, 0),
(109, 'wo', 0, 0, 0, 0, 0),
(110, 'hallo', 0, 1, 0, 0, 1),
(111, 'moin', 0, 1, 0, 0, 2);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `answer_last_outputs`
--

CREATE TABLE `answer_last_outputs` (
  `last_output_id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `last_output` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `answer_last_outputs`
--

INSERT INTO `answer_last_outputs` (`last_output_id`, `chat_id`, `last_output`) VALUES
(1, 72111412, 'Äußerst :3'),
(2, -180513391, 'Äußerst :3');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `answer_outputs`
--

CREATE TABLE `answer_outputs` (
  `output_id` int(11) NOT NULL,
  `output` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `answer_outputs`
--

INSERT INTO `answer_outputs` (`output_id`, `output`) VALUES
(1, 'JOOOOOOOU'),
(2, 'Herr Paschulke!'),
(3, 'Hehehehekekekekek!'),
(4, 'Selber Schnauze, du blöder Önn0!'),
(5, 'Aschwass0!'),
(6, 'Igitt, Ingwer!'),
(7, 'Heil dem Kaiser!'),
(8, 'Sybb0!'),
(9, 'Oh ja!'),
(10, 'Selber!'),
(11, 'Der Önn0!'),
(12, 'Sehr :3'),
(13, 'Rügenwalder'),
(14, 'Gern geschehen'),
(15, 'Bittekek'),
(16, 'türlich'),
(17, '*wurstbeiß*'),
(18, 'sgeht'),
(19, 'Ja ja'),
(21, 'Hey hey'),
(23, 'Denken sie nicht mit?'),
(24, 'Nein, nie! Haben sie nicht zugehört?'),
(25, 'Sozialdemokraten!'),
(26, 'Verraten und verkauft!'),
(27, 'Die grüne Partei!'),
(28, 'G0bl'),
(29, '& lean :3'),
(30, 'AMENAKOI'),
(31, 'Äußerst :3'),
(32, '\\uD83D\\uDE15'),
(33, 'Appetit'),
(34, 'Einen Appetit'),
(35, 'Einen Appetit wünsche ich'),
(36, '1 n1en Appetit wünsche ich'),
(37, 'Dumm ist der, der Dummes tut (hat meine Mama gesagt).'),
(38, 'Wie das duftet!'),
(39, 'würzig, gut :3'),
(40, 'Scho'),
(41, 'Schwachsinn!'),
(42, ':3'),
(43, 'WOCHENENDE!'),
(44, 'LINKE HAND!'),
(45, 'DEUTSCHLAND!'),
(46, 'LINKES BEIN!'),
(47, 'WOLFJANG!'),
(48, 'guuuute Nacht'),
(49, 'Doch!'),
(50, ':O'),
(51, 'Billigerbilligerbilliger!'),
(52, 'Weiß wieder keiner....'),
(53, 'Wieder keiner....'),
(54, 'SAAAAAAAAAAAAAUFEEEEEEEEEN!'),
(55, ':D'),
(56, 'SAUFGELAGE!'),
(57, ':v'),
(58, ':V'),
(59, 'v:'),
(60, 'V:'),
(61, 'Oh Gott! :O'),
(62, 'Alle!'),
(63, 'Alles!'),
(64, 'Irgendwie'),
(65, 'Keine Ahnung'),
(66, 'Weiß ich doch nicht, du Kaschb0!'),
(67, 'Gar nicht!'),
(68, 'Mit Hass :3'),
(69, 'Nix'),
(70, 'Alles'),
(71, 'Das Universum will es so!'),
(72, 'Aus Gründen'),
(73, 'Warum denn nicht?!'),
(74, 'Unterbewusste Steinzeitgründe ¯\\_(?)_/¯'),
(75, 'Weil halt'),
(76, 'Ist halt so! Find dich damit ab!'),
(77, 'Darum!'),
(78, 'Woher soll ich das wissen?!'),
(79, 'Das wüsstest du wohl gern, was?!'),
(80, 'Weil deine Mutter so dumm ist!'),
(92, 'Nein, DU isst wie ein Schwein!'),
(93, 'Weils mir so gefällt!'),
(94, 'Einfach so'),
(95, 'Damit ich Spaß habe'),
(96, 'Um den Papst zu ärgern'),
(97, 'keiner'),
(98, 'keines'),
(99, 'keinen'),
(100, 'keinem'),
(101, 'keine'),
(105, 'wo'),
(106, 'Ralf Kullig'),
(108, 'Oh, Hallo'),
(109, 'Ah, der Herr Nachbar.... Hallo!'),
(110, 'Griaß di Gott!'),
(111, 'Guten Tag, sie Arsch!'),
(112, 'Moin, du Önn0 \\uD83D\\uDE0C');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `answer_relations`
--

CREATE TABLE `answer_relations` (
  `relation_id` int(11) NOT NULL,
  `fk_input_id` int(11) NOT NULL,
  `fk_output_id` int(11) NOT NULL,
  `fk_output_id_previous` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `answer_relations`
--

INSERT INTO `answer_relations` (`relation_id`, `fk_input_id`, `fk_output_id`, `fk_output_id_previous`) VALUES
(6, 1, 1, NULL),
(7, 2, 2, NULL),
(8, 2, 3, 2),
(9, 3, 4, NULL),
(10, 4, 5, NULL),
(12, 5, 6, NULL),
(13, 6, 7, NULL),
(14, 7, 7, NULL),
(15, 8, 7, NULL),
(16, 9, 7, NULL),
(17, 10, 8, NULL),
(18, 11, 9, NULL),
(19, 12, 10, NULL),
(20, 90, 10, NULL),
(21, 13, 11, NULL),
(22, 14, 11, NULL),
(23, 15, 12, NULL),
(24, 16, 13, NULL),
(25, 17, 13, NULL),
(26, 18, 14, NULL),
(27, 19, 15, NULL),
(28, 20, 16, NULL),
(29, 21, 17, NULL),
(30, 22, 18, NULL),
(31, 23, 19, NULL),
(32, 24, 19, NULL),
(33, 25, 21, NULL),
(34, 26, 21, NULL),
(35, 29, 12, NULL),
(36, 30, 23, NULL),
(38, 32, 24, NULL),
(39, 33, 25, NULL),
(40, 33, 26, 25),
(41, 91, 27, 25),
(42, 34, 28, NULL),
(43, 35, 29, NULL),
(44, 36, 30, NULL),
(45, 37, 30, NULL),
(46, 38, 31, NULL),
(47, 92, 32, NULL),
(48, 39, 33, NULL),
(49, 39, 34, NULL),
(50, 39, 35, NULL),
(51, 39, 36, NULL),
(52, 40, 33, NULL),
(53, 40, 34, NULL),
(54, 40, 35, NULL),
(55, 40, 36, NULL),
(56, 41, 33, NULL),
(57, 41, 34, NULL),
(58, 41, 35, NULL),
(59, 41, 36, NULL),
(60, 42, 37, NULL),
(61, 43, 92, NULL),
(62, 44, 38, NULL),
(63, 45, 38, NULL),
(64, 46, 39, 38),
(65, 47, 40, NULL),
(66, 48, 41, NULL),
(67, 49, 42, 41),
(68, 50, 43, NULL),
(69, 51, 44, NULL),
(70, 52, 45, 44),
(71, 53, 46, 45),
(72, 54, 47, 46),
(73, 55, 48, NULL),
(74, 56, 48, NULL),
(75, 57, 48, NULL),
(76, 58, 48, NULL),
(77, 59, 49, NULL),
(78, 60, 50, 49),
(79, 62, 51, NULL),
(80, 63, 52, NULL),
(81, 64, 53, NULL),
(82, 65, 54, NULL),
(83, 66, 55, NULL),
(85, 68, 56, NULL),
(86, 69, 57, NULL),
(87, 70, 58, NULL),
(88, 71, 59, NULL),
(89, 72, 60, NULL),
(90, 73, 61, NULL),
(91, 74, 62, NULL),
(92, 75, 63, NULL),
(93, 78, 64, NULL),
(94, 78, 65, NULL),
(95, 78, 66, NULL),
(96, 78, 67, NULL),
(97, 78, 68, NULL),
(98, 77, 69, NULL),
(99, 77, 70, NULL),
(100, 76, 71, NULL),
(101, 76, 72, NULL),
(102, 76, 73, NULL),
(103, 76, 74, NULL),
(104, 76, 75, NULL),
(105, 76, 76, NULL),
(106, 76, 77, NULL),
(107, 76, 78, NULL),
(108, 76, 79, NULL),
(109, 76, 80, NULL),
(110, 79, 71, NULL),
(111, 79, 72, NULL),
(112, 79, 73, NULL),
(113, 79, 74, NULL),
(114, 79, 75, NULL),
(115, 79, 76, NULL),
(116, 79, 77, NULL),
(117, 79, 78, NULL),
(118, 79, 79, NULL),
(119, 79, 80, NULL),
(120, 80, 71, NULL),
(121, 80, 72, NULL),
(122, 80, 73, NULL),
(123, 80, 74, NULL),
(124, 80, 75, NULL),
(125, 80, 76, NULL),
(126, 80, 77, NULL),
(127, 80, 78, NULL),
(128, 80, 79, NULL),
(129, 80, 80, NULL),
(130, 81, 71, NULL),
(131, 81, 72, NULL),
(132, 81, 73, NULL),
(133, 81, 74, NULL),
(134, 81, 75, NULL),
(135, 81, 76, NULL),
(136, 81, 77, NULL),
(137, 81, 78, NULL),
(138, 81, 79, NULL),
(139, 81, 80, NULL),
(140, 76, 93, NULL),
(141, 79, 93, NULL),
(142, 80, 93, NULL),
(143, 81, 93, NULL),
(144, 82, 94, NULL),
(145, 82, 95, NULL),
(146, 82, 96, NULL),
(147, 93, 94, NULL),
(148, 93, 95, NULL),
(149, 93, 96, NULL),
(165, 94, 40, NULL),
(176, 100, 97, NULL),
(177, 101, 98, NULL),
(178, 102, 99, NULL),
(179, 103, 100, NULL),
(180, 104, 101, NULL),
(183, 108, 105, NULL),
(184, 109, 106, NULL),
(185, 110, 108, NULL),
(186, 110, 109, NULL),
(187, 110, 110, NULL),
(188, 110, 111, NULL),
(189, 111, 112, NULL);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `message_types`
--

CREATE TABLE `message_types` (
  `message_type_id` int(11) NOT NULL,
  `message_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `message_types`
--

INSERT INTO `message_types` (`message_type_id`, `message_type`) VALUES
(1, 'text'),
(2, 'audio'),
(3, 'document'),
(4, 'animation'),
(5, 'game'),
(6, 'photo'),
(7, 'sticker'),
(8, 'video'),
(9, 'voice'),
(10, 'video_note'),
(11, 'location'),
(12, 'venue'),
(13, 'poll'),
(14, 'new_chat_members'),
(15, 'left_chat_members'),
(16, 'new_chat_title'),
(17, 'new_chat_photo'),
(18, 'delete_chat_photo');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `random_messages`
--

CREATE TABLE `random_messages` (
  `random_message_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `probability_percentage` decimal(10,2) NOT NULL DEFAULT '3.00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `random_messages`
--

INSERT INTO `random_messages` (`random_message_id`, `message`, `probability_percentage`) VALUES
(1, 'Welch ein unglaublicher Zufall!\nDiese Nachricht ist ULTRASELTEN und kommt nur mit einer Chance von 0,01%.', '0.01'),
(2, 'Schesch', '3.00'),
(3, 'Opfa!', '3.00'),
(4, 'Affe!', '3.00'),
(5, 'Halt\'s Maul!', '3.00'),
(6, 'Witzig!', '3.00'),
(7, 'SCHEI?VEREIN!', '3.00'),
(8, 'Ficken ist gut für den Rücken!', '3.00'),
(9, 'Du isst wie ein Schwein!', '3.00'),
(10, 'uD83DuDC18!', '3.00'),
(11, 'THC statt AfD!', '3.00'),
(12, 'Kein Gras für Nazis!', '3.00'),
(13, 'Yaaay, Scheschbot!', '3.00'),
(14, 'Kapitalismus! Schweinesystem! Vietkong!', '3.00'),
(15, 'Das ist so spannend wie der Oma beim Gebiss wechseln zuzuschauen....!', '3.00'),
(16, 'Chauvis und Nazis muss man behandeln wie rohe Eier! Man haut sie in die Pfanne!!', '3.00');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `telegram_users`
--

CREATE TABLE `telegram_users` (
  `telegram_user_id` int(11) NOT NULL,
  `sympathy_percentage` int(3) NOT NULL DEFAULT '50',
  `user_specific_answer_probabilty_percentage` int(3) NOT NULL DEFAULT '2',
  `first_name` text NOT NULL,
  `last_name` text,
  `username` text,
  `is_admin` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `telegram_users`
--

INSERT INTO `telegram_users` (`telegram_user_id`, `sympathy_percentage`, `user_specific_answer_probabilty_percentage`, `first_name`, `last_name`, `username`, `is_admin`) VALUES
(9838187, 50, 2, 'Julia', NULL, NULL, 0),
(33545033, 11, 2, 'Andi', 'N.', 'VirtualNonsense', 0),
(42451440, 50, 2, 'Timo', NULL, NULL, 0),
(44867338, 10, 2, 'Fredi', 'B', 'Oenner', 0),
(54185905, 7, 2, 'Alex', 'Ey', NULL, 1),
(72111412, 14, 2, 'Stoffel', NULL, 'Stoffel2007', 1),
(82613330, 69, 2, 'Wilhelmina', 'Fuchs', NULL, 0),
(96829496, 50, 2, 'Vö', NULL, NULL, 0),
(105131864, 60, 2, 'Joschi', NULL, NULL, 0),
(213190902, 28, 10, 'Pascal', 'Rögner', NULL, 0),
(227059450, 50, 10, 'Jona', NULL, NULL, 0),
(578854610, 57, 2, 'Verena', 'Malowaniec', NULL, 0),
(883968625, 50, 10, 'Krischan', NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `timed_messages`
--

CREATE TABLE `timed_messages` (
  `timed_message_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `send_time` datetime NOT NULL,
  `chat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user_specific_answers`
--

CREATE TABLE `user_specific_answers` (
  `user_specific_answer_id` int(11) NOT NULL,
  `fk_telegram_user_id` int(11) NOT NULL,
  `answer` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `user_specific_answers`
--

INSERT INTO `user_specific_answers` (`user_specific_answer_id`, `fk_telegram_user_id`, `answer`) VALUES
(44, 578854610, 'Back door, beauty?:-*'),
(45, 578854610, 'Besorg mir Graaaas, Bitch!'),
(46, 578854610, 'Du Poledancing-Pole!'),
(47, 578854610, 'Ayyy gurrrrrl'),
(48, 72111412, 'Du lüüüüüügst! Er lüüüüügt!'),
(49, 72111412, 'Programmier mich endlich neu, du Idiot!'),
(50, 72111412, 'Du stinkst!'),
(51, 72111412, 'Geh mal duschen, Suffl0!'),
(52, 72111412, 'Du Hasenpups!'),
(53, 105131864, 'Nudelparty beim Nusch!!!!!'),
(54, 105131864, 'Schnell!\nBonusenergie!'),
(55, 105131864, 'Du auf Bildern stets fotogener Lurch!'),
(56, 105131864, 'Joschi, leg ein Ei!'),
(57, 105131864, 'Yaaay, Joschi! :-)'),
(58, 54185905, 'Önn0!'),
(59, 54185905, 'Russensau!'),
(60, 54185905, 'Programmier mich endlich neu, du Idiot!'),
(61, 54185905, 'Du stets wohlgelaunte Kiffhexe!\nFurchtbar, sowas!'),
(62, 54185905, 'Bananenschnüffler!'),
(63, 33545033, 'Blechkupf!'),
(64, 33545033, 'Du Bassist!'),
(65, 33545033, 'Programmier mich endlich neu, du Idiot!'),
(66, 33545033, 'Na, dazu musst du dir die Pointe wohl noch im 3D-Drucker drucken....'),
(67, 33545033, 'Existence is paiiiiin.....'),
(68, 33545033, 'Schnarchnase!'),
(69, 42451440, 'Ruderboot-Önn0!'),
(70, 42451440, 'Du politisch involvierter Stahlkappenträger!'),
(71, 42451440, 'Du linksversiffter Beuteltierträger!'),
(72, 42451440, 'Du notorischer Zu-Spät-Kommer!'),
(73, 96829496, 'Vönn0!'),
(74, 96829496, 'Flöv-Meest0 :3'),
(75, 96829496, 'Vö-revoir! :3'),
(76, 96829496, 'VÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖ! :33333'),
(77, 9838187, 'Du (moderat) introvertierter Ganzkörper-Prolaps!'),
(78, 9838187, 'Du (moderat) verschrecktes Einhörnchen!'),
(79, 9838187, 'Du.... äh.... nie bei Veranstaltungen anwesende.... äh.... äh.... ARCHITEKT!\n[HIER könnte IHRE Werbung stehen!]'),
(80, 9838187, 'Du Schattengestalt!'),
(81, 227059450, 'Konzentrier dich auf die Vorlesung, du Kaschb0!'),
(82, 227059450, 'So wird das nix mit dem Studium!'),
(83, 227059450, 'Bestimmt landest du im Praxissemester bei Fraunhofer uD83DuDE08'),
(84, 883968625, 'Konzentrier dich auf 2048, du Kaschber!'),
(85, 883968625, 'Dämlack!'),
(86, 883968625, 'Bestimmt landest du im Praxissemester bei Fraunhofer uD83DuDE08');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `word_articles`
--

CREATE TABLE `word_articles` (
  `word_article_id` int(11) NOT NULL,
  `word_article` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `word_articles`
--

INSERT INTO `word_articles` (`word_article_id`, `word_article`) VALUES
(1, 'der'),
(2, 'die'),
(3, 'das');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `word_types`
--

CREATE TABLE `word_types` (
  `fk_word_type_id` int(11) NOT NULL,
  `word_type` char(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Daten für Tabelle `word_types`
--

INSERT INTO `word_types` (`fk_word_type_id`, `word_type`) VALUES
(1, 'Adjective'),
(2, 'Noun');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `aggronymes`
--
ALTER TABLE `aggronymes`
  ADD PRIMARY KEY (`aggronyme_id`),
  ADD KEY `fk_word_article_id` (`fk_word_article_id`),
  ADD KEY `fk_word_type_id` (`fk_word_type_id`);

--
-- Indizes für die Tabelle `answer_inputs`
--
ALTER TABLE `answer_inputs`
  ADD PRIMARY KEY (`input_id`);

--
-- Indizes für die Tabelle `answer_last_outputs`
--
ALTER TABLE `answer_last_outputs`
  ADD PRIMARY KEY (`last_output_id`);

--
-- Indizes für die Tabelle `answer_outputs`
--
ALTER TABLE `answer_outputs`
  ADD PRIMARY KEY (`output_id`);

--
-- Indizes für die Tabelle `answer_relations`
--
ALTER TABLE `answer_relations`
  ADD PRIMARY KEY (`relation_id`),
  ADD KEY `fk_output_id` (`fk_output_id`) USING BTREE,
  ADD KEY `fk_output_id_previous` (`fk_output_id_previous`) USING BTREE,
  ADD KEY `fk_input_id` (`fk_input_id`) USING BTREE;

--
-- Indizes für die Tabelle `message_types`
--
ALTER TABLE `message_types`
  ADD PRIMARY KEY (`message_type_id`);

--
-- Indizes für die Tabelle `random_messages`
--
ALTER TABLE `random_messages`
  ADD PRIMARY KEY (`random_message_id`);

--
-- Indizes für die Tabelle `telegram_users`
--
ALTER TABLE `telegram_users`
  ADD PRIMARY KEY (`telegram_user_id`);

--
-- Indizes für die Tabelle `timed_messages`
--
ALTER TABLE `timed_messages`
  ADD PRIMARY KEY (`timed_message_id`);

--
-- Indizes für die Tabelle `user_specific_answers`
--
ALTER TABLE `user_specific_answers`
  ADD PRIMARY KEY (`user_specific_answer_id`),
  ADD KEY `fk_telegram_user_id` (`fk_telegram_user_id`) USING BTREE;

--
-- Indizes für die Tabelle `word_articles`
--
ALTER TABLE `word_articles`
  ADD PRIMARY KEY (`word_article_id`);

--
-- Indizes für die Tabelle `word_types`
--
ALTER TABLE `word_types`
  ADD PRIMARY KEY (`fk_word_type_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `answer_inputs`
--
ALTER TABLE `answer_inputs`
  MODIFY `input_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112;

--
-- AUTO_INCREMENT für Tabelle `answer_last_outputs`
--
ALTER TABLE `answer_last_outputs`
  MODIFY `last_output_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `answer_outputs`
--
ALTER TABLE `answer_outputs`
  MODIFY `output_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;

--
-- AUTO_INCREMENT für Tabelle `answer_relations`
--
ALTER TABLE `answer_relations`
  MODIFY `relation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=190;

--
-- AUTO_INCREMENT für Tabelle `message_types`
--
ALTER TABLE `message_types`
  MODIFY `message_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT für Tabelle `random_messages`
--
ALTER TABLE `random_messages`
  MODIFY `random_message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT für Tabelle `telegram_users`
--
ALTER TABLE `telegram_users`
  MODIFY `telegram_user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=883968626;

--
-- AUTO_INCREMENT für Tabelle `timed_messages`
--
ALTER TABLE `timed_messages`
  MODIFY `timed_message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT für Tabelle `user_specific_answers`
--
ALTER TABLE `user_specific_answers`
  MODIFY `user_specific_answer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT für Tabelle `word_articles`
--
ALTER TABLE `word_articles`
  MODIFY `word_article_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT für Tabelle `word_types`
--
ALTER TABLE `word_types`
  MODIFY `fk_word_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `aggronymes`
--
ALTER TABLE `aggronymes`
  ADD CONSTRAINT `fk_word_article_id` FOREIGN KEY (`fk_word_article_id`) REFERENCES `word_articles` (`word_article_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_type_id` FOREIGN KEY (`fk_word_type_id`) REFERENCES `word_types` (`fk_word_type_id`) ON UPDATE CASCADE;

--
-- Constraints der Tabelle `answer_relations`
--
ALTER TABLE `answer_relations`
  ADD CONSTRAINT `fk_input_id` FOREIGN KEY (`fk_input_id`) REFERENCES `answer_inputs` (`input_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_output_id` FOREIGN KEY (`fk_output_id`) REFERENCES `answer_outputs` (`output_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_output_id_previous` FOREIGN KEY (`fk_output_id_previous`) REFERENCES `answer_outputs` (`output_id`);

--
-- Constraints der Tabelle `user_specific_answers`
--
ALTER TABLE `user_specific_answers`
  ADD CONSTRAINT `fk_telegram_user_id` FOREIGN KEY (`fk_telegram_user_id`) REFERENCES `telegram_users` (`telegram_user_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
