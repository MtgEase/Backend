SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for meeting
-- ----------------------------
DROP TABLE IF EXISTS `meeting`;
CREATE TABLE `meeting`  (
  `mid` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'mid',
  `topic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '会议主题',
  `time_start` timestamp NOT NULL COMMENT '会议开始时间戳',
  `time_stop` timestamp NOT NULL COMMENT '会议结束时间戳',
  `rid` int NOT NULL COMMENT '会议室的rid',
  `tip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  `status` int NOT NULL COMMENT '会议审批状态\r\n\r\n0: draft 未提交\r\n\r\n1: pending 待管理员审批\r\n\r\n2: reviewing 待辅导员审批\r\n\r\n3: approved 已通过\r\n\r\n4: rejected 未通过',
  PRIMARY KEY (`mid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '会议' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
