SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for determine
-- ----------------------------
DROP TABLE IF EXISTS `determine`;
CREATE TABLE `determine`  (
  `did` binary(16) NOT NULL,
  `is_meeting` bit(1) NOT NULL,
  `id` binary(16) NOT NULL,
  PRIMARY KEY (`did`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
