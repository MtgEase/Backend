SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `uid` varchar(36) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  `wxid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  `hashed_passwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
