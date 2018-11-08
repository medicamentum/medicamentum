-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema DRUGS
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema DRUGS
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DRUGS` DEFAULT CHARACTER SET utf8 ;
USE `DRUGS` ;

-- -----------------------------------------------------
-- Table `DRUGS`.`DRUG`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DRUGS`.`DRUG` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `agency` VARCHAR(500) NULL,
  `name` VARCHAR(500) NULL,
  `laboratory` VARCHAR(500) NULL,
  `agency_id` VARCHAR(500) NULL,
  `publication_date` VARCHAR(45) NULL,
  `leaflet` VARCHAR(100) NULL,
  `medical_leaftlet` VARCHAR(500) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DRUGS`.`DRUG_LEAFTLET`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DRUGS`.`DRUG_LEAFTLET` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `leaflet` VARCHAR(100) NULL,
  `content` LONGTEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DRUGS`.`DRUG_SIDE_EFFECT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DRUGS`.`DRUG_SIDE_EFFECT` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `leaflet` VARCHAR(100) NULL,
  `side_effect_url` LONGTEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DRUGS`.`DRUG_DISEASE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DRUGS`.`DRUG_DISEASE` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `leaflet` VARCHAR(100) NULL,
  `disease` LONGTEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DRUGS`.`DRUG_COMPONENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DRUGS`.`DRUG_COMPONENT` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `leaflet` VARCHAR(100) NULL,
  `component` LONGTEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
