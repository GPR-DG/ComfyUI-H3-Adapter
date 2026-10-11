# RELEASE_CHECKLIST

版本 0.1.5；2026-10-11。本清单区分源码/包门禁与外部部署验收；远端发布成功只在核对远端 HEAD 后报告。

## 源码与最小修复

- [x] 全部原始 Python/JS/MJS、注册、配置、provider、调度、ledger、协议、测试与打包脚本逐文件读取。
- [x] SOURCE_MAP.md 描述真实模块、调用关系与数据流。
- [x] 六个历史问题独立判定 CONFIRMED/REJECTED；四类确认问题先复现后修复。
- [x] 不修改旧测试、不改 H3ImageEdit 名称/端口/工作流合同、不重写调度。
- [x] 旧 ledger 自动迁移保留任务/预算；连续身份 Key 轮换与原任务恢复合同保持。

## 免费验证与公开内容

- [x] Python 173 项无 skip；JS 5 套通过。
- [x] 配置保存、重复、并发、安全失败切换、unknown 不换家、恢复与 Mock API 均覆盖。
- [x] 官方 ComfyUI CPU 宿主导入、路由、有/无 MASK、缓存重放、Save/Preview 成功。
- [x] 真实 TCP Mock 27 类场景通过。
- [x] 解压 ZIP 副本验证与 manifest/CRC/SHA256 复核。
- [x] README 安装、配置、参数/Mask/nonce 示例和 RH 边界完善。
- [x] 根目录 FINAL_AUDIT_REPORT.md、SOURCE_MAP.md、CHANGELOG.md 完成。
- [x] 暂存内容排除个人路径/用户名、真实 Token/Key、日志、数据库、缓存、临时文件及活动配置。
- [x] tests 中 FAKE/SYNTHETIC/mock-only 是不可用测试 fixture，不是真实商家 Key；保留它们以便验证行为。
- [x] 历史文档保留并标记为历史；最终结论不引用旧 PASS 当源码证据。

## GitHub 发布执行门禁

1. 验证当前连接的真实 GitHub 用户，查询目标仓库与实际 push 权限；404 时在该用户下创建 ComfyUI-H3-Adapter。
2. 暂存经过审查的公开文件，执行 git status、git diff --cached、git diff --cached --check。
3. 使用提交信息：release: ComfyUI H3 Adapter initial stable audit release。
4. push 后比较远端 HEAD 与本地 HEAD，并确认工作树干净。权限或网络失败即报告失败并给手动命令；不能伪造成功。
5. 本报告/清单描述验证门禁；实际远端结果记录在交付 PUBLICATION_RESULT.json 和最终回复，不把预先具备 scope 当作 push 证据。

GitHub 账户认证与公开仓库创建已成功，实测 push 权限为 true。全量暂存 diff 中仅三份未改的历史文档/旧测试/第三方许可存在原有尾空白或末尾空行，已记录在最终报告；本次改动文件检查通过。

## 仍需部署方验收

- [ ] 真实供应商正式协议、safe rejection语义、模型/Mask/size能力及实际账单。
- [ ] AI 编辑效果及背景保留要求。
- [ ] RH 安装、外连、密钥/租户管理、持久卷与云端闭环。
- [ ] 目标 Windows 文件替换/ACL/外部句柄；本轮一条 WinError 5 失败证据保留。
- [ ] 目标版本/平台/Python/GPU 的运行兼容性与完整浏览器 E2E。
