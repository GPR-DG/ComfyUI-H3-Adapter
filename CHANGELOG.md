# Changelog

## 0.1.5 — 最终独立源码审计修复（2026-10-11）

- 修复配置读取与凭据读取之间的并发修改：提交和模型发现使用锁内配置 revision，拒绝旧配置借用新供应商的 Key。
- 任务快照记录非秘密 credential_generation；恢复时区分连续身份轮换与删除重建，阻止旧环境 Key 任务使用新身份的 Key。
- 冷却记录按地址、认证身份和代际匹配；旧数据库平滑增加可空 identity 列，保留旧任务记录和保守冷却。
- 供应商、模型 ID 或别名实际变化时清空节点 parameters；选择未变保留用户参数。
- 新增 8 项 Python 回归、6 个前端回归场景，以及使用官方 ComfyUI 宿主和本地 Mock 的导入/IMAGE 消费验证脚本；原测试未改。
- 新增 SOURCE_MAP、FINAL_AUDIT_REPORT、RELEASE_CHECKLIST，更新安装与协议说明，发行白名单收录本次文档与验证文件。
- 仍使用原 H3ImageEdit 节点、输入输出合同、nonce 语义、主备调度和 SQLite 提交预留流程。真实商家/RH 与目标 Windows 存储环境仍须验收。

更早的版本历史见 docs/CHANGELOG.md；其中旧 PASS/计数不代表本次源码结论。
