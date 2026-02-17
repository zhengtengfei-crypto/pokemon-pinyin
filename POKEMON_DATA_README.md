# 宝可梦数据生成器使用说明

## 📋 功能说明

这个脚本可以自动生成所有宝可梦的中文名称、拼音和学习题目配置。

## 🚀 快速开始

### 1. 安装依赖

```bash
pip3 install pypinyin requests
```

### 2. 运行脚本

```bash
cd /Users/zhengtengfei/Documents/web_ai_game/pokemon-pinyin
python3 generate_pokemon_data.py
```

### 3. 选择生成范围

- **选项1**：第一世代（1-151）- 推荐先用这个测试
- **选项2**：前三世代（1-386）
- **选项3**：所有世代（1-1025）- 需要完整的中文名称数据
- **选项4**：自定义范围

### 4. 复制数据到游戏中

脚本会生成 `pokemon_database.js` 文件，将其内容复制到 `index.html` 中替换现有的 `pokemonDatabase`。

## ✅ 完整数据已就绪

### 当前状态

- ✅ 脚本已内置**全部1025只**宝可梦的中文名称（简体中文）
- ✅ 数据来源：PokeAPI官方CSV数据
- ✅ 涵盖第一世代到第九世代所有宝可梦
- ✅ 已生成完整的 `pokemon_database.js` 文件（1.3MB）

### 数据来源

本项目使用了以下开源数据：
- **PokeAPI** (https://pokeapi.co/) - 官方Pokemon数据API
- **PokeAPI CSV数据** - Pokemon简体中文名称
- **pypinyin库** - 中文拼音自动生成

感谢开源社区的贡献！

## 📊 生成的数据格式

```javascript
{
    id: 1,
    name: "妙蛙种子",
    pinyin: ["miào", "wā", "zhǒng", "zǐ"],
    image: "https://raw.githubusercontent.com/PokeAPI/sprites/...",
    challenges: [
        { target: "m", type: "initial", options: ["m", "n", "l"], charIndex: 0 },
        { target: "w", type: "initial", options: ["w", "u", "v"], charIndex: 1 },
        ...
    ]
}
```

## 🎯 智能题目生成

脚本会自动：
- ✅ 拆分拼音为声母和韵母
- ✅ 根据易混淆规则生成干扰项
- ✅ 重点考察 b/d/p/q、zh/z/ch、an/ang、in/ing 等难点
- ✅ 每个字生成多个题目（声母题+韵母题）

## 🔧 自定义配置

### 修改易混淆规则

编辑脚本中的 `CONFUSING_INITIALS` 和 `CONFUSING_FINALS` 字典来调整干扰项生成规则。

### 调整题目数量

修改 `generate_challenges()` 函数中的逻辑来控制每个字生成几个题目。

## 📝 示例

运行脚本后会生成类似如下的输出：

```
✅ 已生成：#001 妙蛙种子 - miào wā zhǒng zǐ
✅ 已生成：#002 妙蛙草 - miào wā cǎo
✅ 已生成：#003 妙蛙花 - miào wā huā
...
✅ 已生成：#151 梦幻 - mèng huàn

✅ 完成！共生成 151 只宝可梦的数据
```

## 🆘 常见问题

### Q: 拼音声调不准确怎么办？
A: pypinyin 库在处理多音字时可能不准确，建议手动校对常见宝可梦的拼音。

### Q: 如何添加更多宝可梦？
A: 在 `POKEMON_CHINESE_NAMES` 字典中添加新的映射：
```python
POKEMON_CHINESE_NAMES = {
    ...
    152: "菊草叶",
    153: "月桂叶",
    ...
}
```

### Q: 如何修改图片源？
A: 修改 `image_url` 变量的格式字符串，可以使用 52poke Wiki 或其他图床。

## 💡 使用建议

### 性能优化建议

由于完整数据库包含 1025 只宝可梦（1.3MB），建议：

1. **渐进式加载**：优先加载用户已遭遇的宝可梦数据
2. **图片懒加载**：仅在需要时加载图片
3. **缓存策略**：使用 Service Worker 缓存常用数据

### 自定义筛选

您可以修改脚本来只生成特定世代：

```bash
# 只生成第一世代
python3 generate_pokemon_data.py
# 选择选项 1

# 或修改脚本中的 ID 范围
```

### 数据更新

当有新世代宝可梦发布时：
1. 从 PokeAPI 下载最新的 CSV 数据
2. 运行脚本重新生成完整数据库
3. 更新 `pokemon_database.js`

---

**✅ 项目已完成**：包含全部 1025 只宝可梦的拼音学习游戏已就绪！
