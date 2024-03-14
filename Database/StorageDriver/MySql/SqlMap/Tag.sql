SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag`  (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'tag名称（具体见表注释）',
  `permissions` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '权限',
  `expiration` timestamp NULL DEFAULT NULL COMMENT '过期时间戳',
  `created_by` int NULL DEFAULT NULL COMMENT '创建者uid',
  PRIMARY KEY (`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = 'tag\r\n\r\ntag通常是管理员或老师编辑修改的，因此不应区分程序名称和显示名称。但是在用户输入处需要特别注意。' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
