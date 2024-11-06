SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for room
-- ----------------------------
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room`  (
  `rid` varchar(36) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `position` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `tip` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  `available` bit(1) NULL DEFAULT NULL,
  `capacity` int NULL DEFAULT NULL,
  `devices` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  `rest` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  PRIMARY KEY (`rid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
