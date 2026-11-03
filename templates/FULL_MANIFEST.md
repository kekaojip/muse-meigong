# 西红柿作家模拟器 全套素材包（直接可用版，2026-11-03）

## 包含什么
- 主角精灵图：GPT 版 5 套，每套 8 帧，atlas（透明）+ Phaser JSON，帧率 think/slack/burst/write 10fps、sleep 8fps。文件在 hero/ 下，atlas 名 *_atlas_despill.png，JSON 名 *_phaser.json。
- 场景：room_empty（空房间，1254x1254）、scene_grid 切出的 6 件：room_empty、desk、bookshelf、window、bed、goal_board，均为透明 PNG。
- 道具：laptop、mug、books、noodles、lamp、plant、papers、tomato_mascot，均为透明 PNG。
- 按钮底：ui_button_1 为顶栏长条；ui_button_2-7 为竖向菜单按钮底（6 个，目标左侧菜单是 7 个，第 7 个请代码复用其中一个形状）；ui_button_8-13 为底部导航按钮底（6 个，目标底部是 5 个，用前 5 个，第 6 个备用）。
- 面板底：ui_panel_1-4 为空白圆角面板底（可复用给当前作品、今日写作、状态、天赋），ui_panel_5 为落日条带（作底部横幅背景备选，不是空白卡片）。
- 图标：icon_* 共 20 个，透明 PNG，顺序按图集实际格位：write、inspiration、outline、character、entries、data、backpack、topic_market、workshop、event、editor、ranking、trophy、settings、stamina、money、tomato_coin、calendar、book、tomato。
- 特殊：special_book_cover（竖版御兽封面）、special_banner（落日剪影横幅，含作家与猫剪影）。
- 单独成图：scene_desk_single（绿幕去底后的书桌大图）、scene_room_empty_single。

## 直接可用是什么意思
- 所有单件都是透明 PNG，一件一个文件，代码按文件名分层叠放即可，不用再切图集。
- 数字和文字不画进图里：体力、稿费、在读、收藏、进度等由代码渲染；按钮和面板上的文字标签也由代码渲染，图里只有底和图标。
- 主角动画：用 hero/ 下的 atlas + Phaser JSON，整帧替换播放，不要在上一帧上叠加画，否则会重影；预览一律压白底或 GIF disposal=2。

## 已知的偏差（不隐瞒）
- GPT 原始交付多为图集，不是每件单张；本包已由 Muse 按格切分并去底、裁边，变成单件。
- 道具原图是白底，已做去底；图标、按钮、面板原图是绿幕，已做去绿。
- 书架格顶部带一株绿植、月目标板格右下角有小番茄涂鸦，原图如此，切分后保留。
- 角色坐桌后脚部被桌挡住，脚部水平线无法从画面单独验证；网格等分以 openbixel 报告为准。
- 面板第 4 格是横向卡片而非纵向卡片，如需纵向天赋面板，请用 ui_panel_1-3 复用或另行生成。
