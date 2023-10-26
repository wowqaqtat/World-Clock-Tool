# 世界时钟工具🌎

世界时钟工具（World Clock Tool），是一款用于全球城市时区查询设计的小型工具。它的主要功能是帮助用户了解并管理他们的时区，无论是在旅行、工作还是日常生活中，都能提供一定的便利。

适用于对时区有需求的人群，包括但不限于：

* 旅行者 ：在计划旅行时，需要知道目的地的时间，以便安排行程。
* 商务人士 ：在进行跨时区的商务沟通时，准确的时区信息非常重要。
* 学生 ：在学习或生活过程中，有时区的概念也是非常重要的。
* 开发者 ：在进行跨时区的编程时，准确的时区信息可以帮助避免各种问题。

功能特点：

* 个性化设置 ：用户可以自定义时区，方便在不同地区进行跨时区的计算和比较。
* 实时更新 ：工具会根据系统时间更新时区数据。
* 简单易用 ：界面简洁明了，操作流程清晰易懂。

## 主要功能

* [X] 支持城市名、国家名模糊搜索。
* [X] 支持用户自行添加城市数据。
* [X] 保存搜索记录。
* [X] 窗体可调节大小，内置默认模式、迷你模式、搜索历史模式。

# 截图

<img src="https://raw.githubusercontent.com/wowqaqtat/World-Clock-Tool/main/doc/界面.png" height="200px"> <img src="https://raw.githubusercontent.com/wowqaqtat/World-Clock-Tool/main/doc/选择城市.png" height="200px"> <img src="https://raw.githubusercontent.com/wowqaqtat/World-Clock-Tool/main/doc/历史记录.png" height="200px">

## 使用方法

1. 克隆此项目到本地。
2. 进入项目目录，根据需要修改 `city.json` 文件。
3. 输入 `python main.py` 命令运行程序。
4. 输入 `pyinstaller -F -w main.py` 将程序打包为 `exe` 文件。

**也可以直接使用我打包好的应用程序，体验一下：**

1. 下载并解压到本地 `World_Clock_Tool.rar` .
2. 运行 `World_Clock_Tool.exe` .

## 注意事项

1. 城市数据来源于网络，作者不保证数据的准确性，仅供测试。用户可以在 `city.json` 文件中自行添加相应的城市信息。
2. 时间计算的依据是计算机设置的时间，请确保您的计算机时间正确，否则可能导致时间计算错误。
3. main.py或exe文件，要与 `city.json` 文件放在同一目录下。
4. 程序未考虑[夏令时](https://baike.baidu.com/item/%E5%A4%8F%E4%BB%A4%E6%97%B6)。

## 联系我们

- 本程序基于 [MIT](https://opensource.org/licenses/MIT) 许可证开源。
- 本程序不定时更新，如果大家在使用的过程中，发现任何bug或有不错的想法，欢迎提出交流。
- 源代码：[https://github.com/wowqaqtat/World-Clock-Tool](https://github.com/wowqaqtat/World-Clock-Tool)
- 视频讲解：bilibili
- 邮箱：[help@haodukeji.cn](mailto:help@haodukeji.cn)
