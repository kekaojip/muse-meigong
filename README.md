# muse 结合 GPT 美工工作流

Muse 直接登录用户的 ChatGPT 处理美工，用户只批准和审核。
GPT 出第一版参考，Muse 按参考出生产版，后续修复与补图都由 Muse 包办。

## 工作流
见 WORKFLOW.md（已封存版）：第一阶段只做资产包交付，第二阶段接代码暂缓。
核心规矩：一次只做一套动作，8 帧拆 4+4 同名合并；门禁 openbixel sheet_score ≥85 分才打包；
背景优先级：真透明底 > 纯色绿底 #00FF00 > 白底/纯色底（rembg 备胎）；
拼表后必做去绿（tools/despill.py），绿残留降到 0；
预览一律先压白底或 GIF disposal=2，否则透明帧会重影；
进游戏必须整帧替换贴图；数字和文字不画进图里，由代码渲染。

## 目录
- WORKFLOW.md：封存的工作流全文
- tools/despill.py：去绿 + 透明边缩 1px
- tools/convert_phaser.py：openbixel atlas JSON 转 Phaser JSON Hash
- templates/FULL_MANIFEST.md：全套素材包清单模板

## 实测案例（2026-11-03）
- 主角 5 套（写作/思考/摸鱼/睡觉/爆更），每套 8 帧，GPT 版原图 sheet_score 全部 100/100。
- 主界面全套：场景、道具、按钮底、面板底、图标 20 个、御兽封面、落日横幅，切分后 56 个单件透明 PNG，
  合入主角 atlas 后 69 个文件。
- 注意：本仓库只放工作流文档与工具，不放 23MB 的生成资产包，资产包由上面流程现生成。

## 适用范围
只限本批主角与主界面线，不覆盖其他游戏线。Muse 绝不在本机登录用户的 Claude。
