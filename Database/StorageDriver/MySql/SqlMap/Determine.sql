SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for determine
-- ----------------------------
DROP TABLE IF EXISTS `determine`;
CREATE TABLE `determine`  (
  `did` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'did',
  `mid` int NULL DEFAULT NULL COMMENT '对应会议的mid',
  `new_user_uid` int NULL DEFAULT NULL COMMENT '待注册用户的uid',
  PRIMARY KEY (`did`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '审批清单\r\n\r\nmid和new_user_uid取其一，优先判断mid。' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
