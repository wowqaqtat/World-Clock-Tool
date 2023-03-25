# 世界时钟工具🌎

世界时钟工具，是一款用于查询全球城市时区的小工具，适用于对时区有需求的人群。（World Clock Tool）

## 使用方法

1. 克隆此项目到本地。
2. 进入项目目录，根据需要修改 `city.json` 文件。
3. 输入 `python main.py` 命令运行程序。
4. 输入 `pyinstaller -F -w main.py` 将程序打包为 `exe` 文件。

**也可以直接使用我打包好的应用程序，体验一下：**

1. 下载并解压到本地 `World_Clock_Tool.rar` .
2. 运行 `World_Clock_Tool.exe` .

## 功能点

- 支持城市名、国家名模糊搜索。
- 支持用户自行添加城市数据。
- 保存搜索记录。
- 窗体可调节大小，内置默认模式、迷你模式、搜索历史模式。

## 注意事项

1. 城市数据来源于网络，作者不对数据准确性负责，仅供测试。用户可以在 `city.json` 文件中自行添加相应的城市信息。
2. 时间计算的依据是计算机设置的时间，请确保您的计算机时间正确，否则可能导致时间计算错误。
3. main.py或exe文件，要与 `city.json` 文件放在同一目录下。
4. 程序未考虑[夏令时](https://baike.baidu.com/item/%E5%A4%8F%E4%BB%A4%E6%97%B6)。

## 联系我们

- 本程序基于 [MIT](https://opensource.org/licenses/MIT) 许可证开源。
- 本程序不定时更新，如果大家在使用的过程中，发现任何bug或有不错的想法，欢迎提出交流。
- 源代码：[https://github.com/wowqaqtat/World-Clock-Tool](https://github.com/wowqaqtat/World-Clock-Tool)
- 视频讲解：bilibili
- 邮箱：[help@haodukeji.cn](mailto:help@haodukeji.cn)
