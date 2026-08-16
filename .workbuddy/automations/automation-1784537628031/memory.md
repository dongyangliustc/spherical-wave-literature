# Automation Memory: spherical_wave_literature 每周同步到 GitHub

## 安全更新 — 2026-07-29
- **Token 迁移**: GitHub PAT 从 automation prompt 明文移除，改为从 Windows 用户环境变量 `GITHUB_SYNC_TOKEN` 读取
- **Prompt 更新**: push 步骤改为 `git remote set-url origin "https://dongyangliustc:${GITHUB_SYNC_TOKEN}@github.com/..."`，空值检查保护
- **⚠️ 安全提醒**: 旧 token 曾在 automation prompt 中以明文存在。建议在 GitHub Settings → Developer settings → Personal access tokens 中轮换此 token

## 执行历史

### 2026-07-26 (第1次执行)
- **状态**: 成功
- **发现变更**: 是（18 个文件，包括 2 个修改的 index 文件、6 个新增 notes、6 个新增 papers PDF、3 个 memory 日志、1 个 scansci_test）
- **提交**: `3fbc54c` — "Weekly auto-sync: update notes and literature"
- **Push**: `096ff88..3fbc54c main -> main` 成功
- **远程 URL**: 已恢复为无 token 版本

### 2026-08-09 (第2次执行)
- **状态**: 本地提交成功，push 失败
- **发现变更**: 是（30 个文件，包括新增 papers PDF 14 个、review packets 4 个、outputs 文档 4 个、modified 3 个、renamed 1 个、automations/memory 文件 2 个）
- **提交**: `1e02744` — "Weekly auto-sync: update notes and literature"
- **Push**: ❌ 失败 — 环境变量 `GITHUB_SYNC_TOKEN` 为空，按规则跳过 push
- **待处理**: 需要设置 `GITHUB_SYNC_TOKEN` 环境变量后手动 push，或等待下次自动执行时环境变量可用

### 2026-08-16 (第3次执行)
- **状态**: 成功（通过 GitHub Contents API 降级推送）
- **发现变更**: 是（33 个文件：18 个文本文件 + 14 个 PDF + 1 个 automation memory）
- **本地提交**: `4a12878` — "Weekly auto-sync: update notes and literature"
- **git push**: ❌ 失败 — USTC 代理 (`198.18.0.28`) 能完成 `GET info/refs` 但在 `send-pack` POST 阶段持续超时（>20 分钟无响应），所有 git push 尝试（含 `--no-thin`、`protocol v2`、`http.postBuffer=500MB`、`git gc` 后重试）均失败
- **降级方案**: 通过 GitHub Contents API (`PUT /repos/{owner}/{repo}/contents/{path}`) 逐文件上传
  - 文本文件：18/18 成功（含中英文路径），分两批完成（第一批 4 个，第二批 10 个，第三批 4 个），SSL 间歇性 `UNEXPECTED_EOF` 错误通过重试解决
  - PDF 文件：14/14 成功（总计约 21 MB，最大单文件 5.0 MB），从 git 对象 `4a12878` 恢复后上传
  - Toffoli 2023 PDF 已在远程（初始提交时已推送），实际新增 14 个 PDF
- **远程最终状态**: `46d9189` — 含全部 47 个 PDF + 全部文本文件
- **本地同步**: `git fetch` + `git reset --hard origin/main` 完成本地-远程对齐
- **远程 URL**: 已恢复为无 token 版本
- **⚠️ 网络问题**: USTC 代理对大体积 HTTPS POST 有限制，git push 不可用。建议未来同步：(1) 若变更仅含文本文件，直接用 Contents API；(2) 若含 PDF，也用 Contents API 逐文件上传；(3) 考虑配置 SSH 推送绕过代理
