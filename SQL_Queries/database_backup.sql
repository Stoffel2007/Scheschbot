-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 01. Mai 2019 um 21:11
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
-- Tabellenstruktur für Tabelle `random_messages`
--

CREATE TABLE `random_messages` (
  `random_message_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `probability_percentage` decimal(10,2) NOT NULL DEFAULT '3.00',
  `fk_message_type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `random_messages`
--

INSERT INTO `random_messages` (`random_message_id`, `message`, `probability_percentage`, `fk_message_type_id`) VALUES
(1, 'Welch ein unglaublicher Zufall!\nDiese Nachricht ist ULTRASELTEN und kommt nur mit einer Chance von 0,01%.', '0.01', 1),
(2, 'Schesch', '3.00', 1),
(3, 'Opfa!', '3.00', 1),
(4, 'Affe!', '3.00', 1),
(5, 'Halt\'s Maul!', '3.00', 1),
(6, 'Witzig!', '3.00', 1),
(7, 'SCHEI?VEREIN!', '3.00', 1),
(8, 'Ficken ist gut für den Rücken!', '3.00', 1),
(9, 'Du isst wie ein Schwein!', '3.00', 1),
(10, '\\uD83D\\uDC18!', '3.00', 1),
(11, 'THC statt AfD!', '3.00', 1),
(12, 'Kein Gras für Nazis!', '3.00', 1),
(13, 'Yaaay, Scheschbot!', '3.00', 1),
(14, 'Kapitalismus! Schweinesystem! Vietkong!', '3.00', 1),
(15, 'Das ist so spannend wie der Oma beim Gebiss wechseln zuzuschauen....!', '3.00', 1),
(16, 'Chauvis und Nazis muss man behandeln wie rohe Eier! Man haut sie in die Pfanne!!', '3.00', 1),
(17, 'Das klingt ja furchtbar!', '50.00', 2),
(18, 'Wunderschöne Klänge :3!', '50.00', 2),
(19, 'So ein furchtarer Krach!', '50.00', 2),
(20, 'Das kann ich nicht öffnen, du Trottel!', '50.00', 3),
(21, 'Tolle Datei! Ganz toll!', '50.00', 3),
(22, 'So eine unselige akustische Furzpampe!', '50.00', 2),
(23, 'Meine Ohren fangen an zu bluten D:', '50.00', 2),
(24, 'Uff, das übersteigt meine Aufmerksamkeitsspanne....', '50.00', 3),
(25, '#teamgif', '2.00', 4),
(26, 'Oh, ach so, ein Dschiff!', '20.00', 4),
(27, 'zoggn:3', '50.00', 5),
(28, 'Oh, eine animierte Spiel und Spahaß-Datei! :3', '50.00', 5),
(29, 'Ihr Suchtis!', '50.00', 5),
(30, 'Dopamin!!!', '50.00', 5),
(31, 'Hübsches Bild :3', '5.00', 6),
(32, 'Ich kann das zwar nicht genau erkennen, aber wehe, es ist ein Star Wars-Meme!', '5.00', 6),
(33, 'Was für ein Scheißbild....', '5.00', 6),
(34, 'Netter Sticker, aber bist du da nicht ein wenig zu alt dafür?', '5.00', 7),
(35, 'Uff, Sticker sind ja soooo kindisch!', '5.00', 7),
(36, 'Was für ein Kindergarten....', '5.00', 7),
(37, 'Na hoffentlich ist das kein Porno....', '20.00', 8),
(38, 'Das schau ich mir etz ned an, dafür ist mir mein Zeit zu schade. ICH, als Bot, habe wichtigere Dinge zu tun.', '20.00', 8),
(39, 'Diese neumodischen Bewegtbilder werden sich niemals durchsetzen!', '20.00', 8),
(40, 'Mich INTERESSIERT nicht, was du zu sagen hast!', '25.00', 9),
(41, 'Dein Gschmarri kannst du dir echt sparen....', '25.00', 9),
(42, 'Kreisfunktion :3', '50.00', 10),
(43, 'x² + y² = 1, legg0! :3', '50.00', 10),
(44, 'Soll ich da etz etwas hinlatschen oder was? Zu Fuß?!', '80.00', 11),
(45, 'Hoffentlich ist das nicht in Kassel....', '80.00', 11),
(46, 'Da geh ich ned hin!', '75.00', 12),
(47, 'Ich bin für Antwort A!', '50.00', 13),
(48, 'Ich bin für Antwort B!', '50.00', 13),
(49, 'Ich bin für Antwort C (ist mir egal, ob die vorhanden ist oder nicht....)!', '50.00', 13),
(50, 'Ich bin für Antwort D (auch wenn\'s die vielleicht nich gibt, mir doch egal :3)!', '50.00', 13),
(51, 'Hallo und herzlich willkommen in diesem Chat voller Idioten und Arschlöcher! ud83dude04', '100.00', 14),
(52, 'Uff, diese Person kann ich nicht leiden, welcher Trottel hat die denn hinzugefügt?!', '100.00', 14),
(53, 'Oh, hallo! Haben sie schon über ihren neuen Mobilfunkvertrag nachgedacht?', '100.00', 14),
(54, 'Wer bist DU denn?!?!?!', '100.00', 14),
(55, 'Naus mit dir! Wir wollen dich hier nicht!', '100.00', 14),
(56, 'Gut, dass er/sie weg ist, konnte sie eh nie leiden....', '100.00', 15),
(57, 'HÖ?! Wo bist du hin?!', '100.00', 15),
(58, 'Tschüss!', '100.00', 15),
(59, 'Und bleib draußen!', '100.00', 15),
(60, 'Der neue Titel gefällt mir nicht!', '100.00', 16),
(61, 'Der neue Titel gefällt mir \\ud83d\\ude04', '100.00', 16),
(62, 'Was für ein einfallsloser Titel, ey....', '100.00', 16),
(63, 'Ich hasse Veränderung! ud83dude29 Das alte bild war doch so schön....', '100.00', 17),
(64, 'Naja....', '100.00', 17),
(65, 'Das Bild war eh hässlich', '100.00', 18),
(66, 'Na toll, jetzt stehen wir ohne Bild da \\ud83d\\ude29', '100.00', 18);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `random_messages`
--
ALTER TABLE `random_messages`
  ADD PRIMARY KEY (`random_message_id`),
  ADD KEY `fk_message_type_id` (`fk_message_type_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `random_messages`
--
ALTER TABLE `random_messages`
  MODIFY `random_message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `random_messages`
--
ALTER TABLE `random_messages`
  ADD CONSTRAINT `fk_message_type_id` FOREIGN KEY (`fk_message_type_id`) REFERENCES `message_types` (`message_type_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
