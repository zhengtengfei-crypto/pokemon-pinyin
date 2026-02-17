# 🎮 宝可梦拼音大搜查 (Pokémon Pinyin Quest)

一款专为儿童设计的汉语拼音学习游戏，结合宝可梦主题，让孩子在游戏中轻松掌握拼音知识。

## ✨ 功能特点

### 🎯 核心玩法
- **点击草丛** → 遭遇神秘宝可梦黑影
- **拼音挑战** → 完成拼音填空题（声母/韵母/声调）
- **精灵球选择** → 3个选项中选择正确答案
- **捕捉收集** → 答对后将宝可梦加入图鉴

### 📚 教育功能
- **易混淆字母训练**：重点考察 b/d/p/q 等形近字母
- **前后鼻音区分**：针对 in/ing、an/ang 等难点
- **声调识别**：所有拼音都带正确声调显示
- **即时纠错反馈**："博士的教学时刻"提供记忆口诀

### 🎨 儿童友好设计
- **超大字体**：标题、拼音、按钮都经过放大优化
- **明显按钮**：精灵球按钮更大（160x160px）更容易点击
- **柔和配色**：使用粉色-蓝色-绿色渐变，色彩丰富但不刺眼
- **圆润设计**：所有元素都有大圆角，更加友好
- **答案展示**：答题后立即显示正确答案，强化学习效果

### 💾 离线支持
- ✅ **完全离线**：所有1025张宝可梦图片已本地化（126.52 MB）
- ✅ 使用 LocalStorage 本地存储进度
- ✅ Service Worker 智能缓存
- ✅ 无需联网即可完整游玩
- ✅ 捕捉记录永久保存在设备上

### 📱 设备支持
- ✅ iPad（主要适配设备）
- ✅ iPhone
- ✅ 其他平板/手机浏览器
- ✅ 支持触屏操作

## 🚀 使用方法

### 方法一：直接在浏览器中打开（推荐）

1. 用 Safari 浏览器打开 `index.html` 文件
2. 点击 Safari 底部的**分享按钮** 📤
3. 选择**"添加到主屏幕"**
4. 设置应用名称（默认"宝可梦拼音大搜查"）
5. 点击**添加**

现在您的 iPad 主屏幕上会出现应用图标，点击即可像原生应用一样使用！

### 方法二：通过本地服务器运行

```bash
# 在项目目录中运行
python3 -m http.server 8000

# 然后在 iPad Safari 中访问
# http://[你的电脑IP]:8000
```

### 方法三：部署到云端（可选）

可以将文件上传到：
- **Vercel**：拖拽文件夹即可部署
- **Netlify**：支持拖拽部署
- **GitHub Pages**：推送到 GitHub 仓库

部署后可以通过网址访问，多设备同步使用。

## 📦 文件说明

```
pokemon-pinyin/
├── index.html                  # 主应用文件（HTML/CSS/JS）
├── pokemon_database.js         # 宝可梦数据库（1025只，1.3MB）
├── images/
│   └── pokemon/                # 本地宝可梦图片（1025张，126.52MB）
│       ├── 1.png               # 妙蛙种子
│       ├── 2.png               # 妙蛙草
│       └── ...
│       └── 1025.png            # 桃歹郎
├── generate_pokemon_data.py    # 数据生成脚本
├── download_images.py          # 图片下载脚本
├── update_image_paths.py       # 图片路径更新脚本
├── POKEMON_DATA_README.md      # 数据生成说明
├── manifest.json               # PWA 配置文件
├── service-worker.js           # 离线支持（含图片缓存）
├── icon-generator.html         # 图标生成工具
├── icon-192.png                # 192x192 应用图标
├── icon-512.png                # 512x512 应用图标
└── README.md                   # 项目说明文档
```

## 🎨 创建应用图标

目前提供了 `icon.svg` 源文件，您需要将其转换为 PNG 格式：

### 在线转换工具（推荐）
1. 访问 https://www.aconvert.com/cn/image/svg-to-png/
2. 上传 `icon.svg`
3. 设置尺寸为 192x192，下载保存为 `icon-192.png`
4. 重复步骤，设置尺寸为 512x512，保存为 `icon-512.png`

### 使用命令行工具
```bash
# 需要安装 ImageMagick
convert -background none -resize 192x192 icon.svg icon-192.png
convert -background none -resize 512x512 icon.svg icon-512.png
```

## 🎮 游戏说明

### 主界面按钮
- **游戏**：开始拼音挑战
- **图鉴**：查看已捕捉的宝可梦
- **设置**：清除进度/管理数据

### 拼音题目类型
1. **声母挑战**：考察 b、p、d、t、g、k 等声母
2. **韵母挑战**：考察 a、o、e、i、u、ü 及复合韵母
3. **整体认读**：考察 chi、shi、zi、ci 等
4. **鼻音挑战**：重点区分前后鼻音

### 教学口诀（错误时显示）
- **b/d 混淆**："左下半圆 d d d，右下半圆 b b b"
- **p/q 混淆**："左上半圆 q q q，右上半圆 p p p"
- **前后鼻音**："ang 是后鼻音，张大嘴巴读 ang"
- **in/ing**："ing 后面有个 g"

## 📝 数据库说明

**✅ 完整版本：包含全部 1025 只宝可梦！**

数据库涵盖：
- 🎮 **第一世代**（1-151）：妙蛙种子、皮卡丘、超梦等经典宝可梦
- 🎮 **第二世代**（152-251）：菊草叶、火球鼠、小锯鳄等
- 🎮 **第三世代**（252-386）：木守宫、火稚鸡、水跃鱼等
- 🎮 **第四世代**（387-493）：草苗龟、小火焰猴、波加曼等
- 🎮 **第五世代**（494-649）：藤藤蛇、暖暖猪、水水獭等
- 🎮 **第六世代**（650-721）：哈力栗、火狐狸、呱呱泡蛙等
- 🎮 **第七世代**（722-809）：木木枭、火斑喵、球球海狮等
- 🎮 **第八世代**（810-905）：敲音猴、炎兔儿、泪眼蜥等（剑盾）
- 🎮 **第九世代**（906-1025）：新叶喵、呆火鳄、润水鸭等（朱紫）

每只宝可梦都包含：
- ✅ 完整中文名称（简体中文）
- ✅ 准确拼音标注（含声调）
- ✅ 智能生成的拼音挑战题目
- ✅ 官方高清图片链接

## 🔧 自定义扩展

### 数据自动生成

本项目使用 Python 脚本自动生成全部 1025 只宝可梦数据，详见 [POKEMON_DATA_README.md](POKEMON_DATA_README.md)

```bash
# 重新生成数据库（如需修改）
python3 generate_pokemon_data.py
```

### 手动添加宝可梦

如需手动添加，编辑 `pokemon_database.js` 文件：

```javascript
{
    id: 1026,  // 宝可梦图鉴编号
    name: "新宝可梦",
    pinyin: ["xīn", "bǎo", "kě", "mèng"],  // 注意：全部小写
    image: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1026.png",
    challenges: [
        { target: "x", type: "initial", options: ["x", "s", "sh"], charIndex: 0 },
        { target: "īn", type: "final", options: ["īn", "íng", "ín"], charIndex: 0 }
    ]
}
```

**重要提示**：拼音必须全部小写，否则语音引擎会使用英文发音！

### 修改题目难度

调整 `challenges` 数组中的干扰项：
- **简单**：使用差异较大的干扰项（如 P 和 M）
- **困难**：使用易混淆的干扰项（如 b 和 d）

### 添加新的教学口诀

在 `teachingTips` 对象中添加新规则：

```javascript
const teachingTips = {
    "zh-z": "记住：zh 是翘舌音，舌头要往上翘！",
    // ... 其他口诀
};
```

## 🐛 常见问题

### Q: 图片无法显示？
A: 宝可梦图片来自 GitHub PokeAPI，需要联网加载。如果无法访问，可以：
1. 下载图片到本地
2. 修改 `image` 字段为本地路径

### Q: 进度丢失了？
A: 进度存储在浏览器的 LocalStorage 中，清除浏览器缓存会导致丢失。建议：
- 不要清除 Safari 的网站数据
- 或者使用"导出进度"功能（可自行添加）

### Q: 如何备份进度？
A: 打开浏览器控制台，运行：
```javascript
// 导出进度
console.log(localStorage.getItem('pokemonPinyinProgress'));

// 导入进度
localStorage.setItem('pokemonPinyinProgress', '你的进度JSON');
```

### Q: 想要更多宝可梦？
A: 可以访问设计文档中提到的 NotebookLM 链接获取更多拼音数据，或参考上方"自定义扩展"部分。

## 📄 技术栈

- **纯前端**：HTML5 + CSS3 + Vanilla JavaScript
- **PWA 技术**：支持离线使用和安装到主屏幕
- **响应式设计**：适配各种屏幕尺寸
- **触屏优化**：大按钮、防误触设计

## 📜 许可证

本项目仅供个人学习使用。宝可梦相关版权归任天堂/Game Freak/Creatures Inc.所有。

## 🙏 鸣谢

- 宝可梦图片来源：[PokeAPI](https://pokeapi.co/)
- 拼音教学参考：52poke Wiki
- 开发辅助：Claude Code by Anthropic

---

**祝您的孩子在游戏中快乐学习拼音！** 🎉

如有问题或建议，欢迎反馈！
