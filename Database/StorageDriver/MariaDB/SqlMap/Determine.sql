SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for determine
-- ----------------------------
DROP TABLE IF EXISTS `determine`;
CREATE TABLE `determine`  (
  `did` varchar(36) NOT NULL,
  `is_meeting` bit(1) NOT NULL,
  `id` varchar(36) NOT NULL,
  PRIMARY KEY (`did`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
