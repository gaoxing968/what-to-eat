# 开心猫·吃什么 · 开发复盘

## 项目概述

| 项目 | 内容 |
|------|------|
| 名称 | 开心猫·吃什么 (what-to-eat) |
| 目的 | 转盘解决"今天吃什么"选择困难 |
| 仓库 | https://github.com/gaoxing968/what-to-eat |
| 在线地址 | https://gaoxing968.github.io/what-to-eat/ |
| 版本 | v1.0 |

---

## 技术栈

| 组件 | 技术 |
|------|------|
| 前端 | 纯 HTML + CSS + JavaScript（无框架依赖）|
| 图形 | Canvas 2D API（转盘绘制）|
| 动画 | 指数衰减物理模拟（`1 - e^(-k*t)`）|
| PWA | manifest.json + Service Worker + 离线缓存 |
| 图标生成 | Python PIL（渐变圆形 + emoji）|
| 托管 | GitHub Pages（无需服务器）|
| 版本管理 | Git + GitHub |

---

## 开发流程

### 步骤

1. 确定方向：参考今天吃什么转盘，决定单 HTML 轻量方案
2. 写 `SPEC.md` 设计文档（109行）
3. 写 `index.html`（~1000行，含转盘+心情+灵魂拷问+成就）
4. 调字体大小、颜色、动画参数
5. 本地 `python -m http.server 8899` 测试
6. 开发阶段 12次 → 改 100次方便测试
7. 完成，发布前改回 12次
8. 创建 PWA 配置：`manifest.json` + `sw.js` + `icons/`
9. `git init` → `git commit` → `git push`
10. `gh repo create` 建仓
11. GitHub Pages 启用（`build_type=legacy`）
12. `gh release create v1.0`
13. 上传截图、README 嵌入截图、添加 FUNDING.yml

---

## 踩坑记录

### 1. 转盘动画太快

**症状：** 初始转盘动画用 `easeOut(t^4)` 曲线，转完太快（约2秒）

**解决：** 改用指数衰减 `1 - e^(-k*t)`，总时长 6 秒，视觉更真实

### 2. 今日次数 localStorage 污染

**症状：** 开发测试时多次旋转耗尽 localStorage 的 `todaySpins`，页面一打开就提示"今日次数用完"无法继续测试

**解决：** 开发阶段改为 100 次限制，完成后统一改回 12 次，注释标注 `// ⚠️ 发布前改回 12`

### 3. Python HTTP 服务器 serving icons 404

**症状：** `http.server` 可以 serve 根目录文件，但子目录 `/icons/` 下的 PNG 持续 404

**原因：** Bash shell 的 MSYS 路径映射和 Python `http.server` 的文件系统视图不同步——`os.listdir()` 能看到 icons 目录但 HTTP 服务器找不到

**解决：** 用 Windows Python（PIL 脚本所在环境）重新生成图标到目标路径，服务器重启后正常

### 4. cua-driver 无法抓 Tkinter 窗口

**原因：** Tk 窗口不走标准 Accessibility API

**解决：** 用 `PIL.ImageGrab.grab()` 全屏截图再裁剪

### 5. GitHub Pages build_type 参数错误

**症状：** 初次调用 `-X POST` 时 `build_type=workflow`，但没有 workflow 文件导致构建卡住

**解决：** 使用 `build_type=legacy`（无需 workflow 文件，GitHub 直接托管静态文件）

---

## 经验总结

### 上 GitHub 公开项目标准流程

```
1. 创建干净项目目录
2. 写 SPEC.md + README.md（先写，代码后补）
3. git init → commit → push
4. gh repo create --public
5. git push -u origin master
6. GitHub Pages: API 调 build_type=legacy
7. 等待 ~1 分钟 Pages 就绪
8. gh release create v1.0
9. 上传截图、README 嵌入、添加 FUNDING.yml
```

### PWA 上线要点

- `manifest.json`：name / short_name / icons / theme_color / display=standalone
- Service Worker：`install` 缓存核心文件，`fetch` 网络优先 + 降级缓存
- 图标：192px + 512px 两张，用 `purpose=maskable` 适配各种形状
- iOS 支持：`<meta apple-mobile-web-app-*>` 系列标签

### 截图发布最佳实践

- 截图 commit 进仓库（不用 release assets）
- README 用 `![截图](screenshot.png)` 嵌入（相对路径）
- Release notes 用 raw.githubusercontent.com 链接

---

## 后续待办

- [ ] 注册 Ko-fi / 爱发电确认用户名
- [ ] 小红书推广引流
- [ ] 掘金/知乎文章（技术原理 + 玩法介绍）
- [ ] 考虑增加自定义菜名功能
- [ ] 考虑增加历史记录功能

---

## 修改记录

| 日期 | 修改内容 |
|------|---------|
| 2026-07-07 | v1.0 首次发布，PWA + GitHub Pages |