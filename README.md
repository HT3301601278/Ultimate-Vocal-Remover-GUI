# Ultimate Vocal Remover GUI v5.6 (终极人声移除工具 GUI v5.6)
<img src="https://raw.githubusercontent.com/Anjok07/ultimatevocalremovergui/master/gui_data/img/UVR_v5.6.png?raw=true" />

[![发布版本](https://img.shields.io/github/release/anjok07/ultimatevocalremovergui.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases/latest)
[![下载量](https://img.shields.io/github/downloads/anjok07/ultimatevocalremovergui/total.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases)

## 关于

本应用使用最先进的音源分离模型从音频文件中移除人声。UVR 的核心开发者训练了此软件包中提供的所有模型(除了 Demucs v3 和 v4 4-stem 模型)。

- **核心开发者**
    - [Anjok07](https://github.com/anjok07)
    - [aufr33](https://github.com/aufr33)

- **支持项目**
    - [捐赠](https://www.buymeacoffee.com/uvr5)

## 安装说明

这些安装包包含了 UVR 界面、Python、PyTorch 和其他运行应用程序所需的依赖项。无需其他前置条件。

### Windows 安装

- 请注意:
    - 此安装程序适用于 Windows 10 或更高版本。
    - 不保证在 Windows 7 或更低版本系统上的功能。
    - 不保证在 Intel Pentium 和 Celeron CPU 系统上的功能。
    - 必须将 UVR 安装到 C:\ 主驱动器。安装到其他驱动器会导致不稳定。

- 通过以下链接下载 Windows 版 UVR 安装程序:
    - [主下载链接](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_v5.6.0_setup.exe)
    - [主下载链接镜像](https://www.mediafire.com/file_premium/jiatpgp0ljou52p/UVR_v5.6.0_setup.exe/file)
- 如果您使用 **AMD Radeon 或 Intel Arc 显卡**，可以尝试 OpenCL 版本:
    - [OpenCL 版本 - 主下载链接](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_v5.6.0_setup_opencl.exe)
- 已安装 UVR 用户的更新包说明:
    - 如果您已安装 UVR，可以直接覆盖安装此包，或从应用程序内直接下载，或[点击此处下载补丁](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_Patch_10_6_23_4_27.exe)。

<details id="WindowsManual">
  <summary>Windows 手动安装说明</summary>

### Windows 手动安装

- 在[这里](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip)下载并解压仓库
- 在[这里](https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe)下载并安装 Python
   - 安装时请确保勾选"添加 python.exe 到 PATH"
- 在解压的仓库目录中运行以下命令:

```
python.exe -m pip install -r requirements.txt
```

如果您有兼容的 Nvidia GPU，请运行以下命令:

```
python.exe -m pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu117
```

如果您没有安装 FFmpeg 或 Rubber Band，且想避免繁琐的安装过程，请按照以下说明操作。

**FFmpeg 安装**

- 在[这里](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)下载预编译版本
- 从压缩包中，将以下文件解压到 UVR 应用程序目录:
   - ```ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe```

**Rubber Band 安装**

要使用时间拉伸或音高变更工具，您需要安装 Rubber Band。

- 在[这里](https://breakfastquay.com/files/releases/rubberband-3.1.2-gpl-executable-windows.zip)下载预编译版本
- 从压缩包中，将以下文件解压到 UVR 应用程序目录:
   - ```rubberband-3.1.2-gpl-executable-windows/rubberband.exe```
   - ```rubberband-3.1.2-gpl-executable-windows/sndfile.dll```

</details>

### MacOS 安装
- 请注意:
    - MacOS Sonoma 鼠标点击问题已修复。
    - Mac M1 的 MPS (GPU) 加速已扩展到支持 Demucs v4 和所有 MDX-Net 模型。
    - 此软件包适用于 macOS Big Sur 及以上版本。
    - 不保证在 macOS Catalina 或更低版本系统上的功能。
    - 不保证在较旧或入门级 Mac 系统上的功能。
    - 安装完成后，首次启动应用程序可能需要 5-10 分钟(取决于您的 Macbook)。

- 通过以下链接下载 MacOS 版 UVR:
    - Mac M1 (arm64) 用户:
       - [主下载链接](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg)
       - [主下载链接镜像](https://www.mediafire.com/file_premium/u3rk54wsqadpy93/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg/file)

    - Mac Intel (x86_64) 用户:
       - [主下载链接](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg)
       - [主下载链接镜像](https://www.mediafire.com/file_premium/2gf1werx5ly5ylz/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg/file)

<details id="CannotOpen">
  <summary>MacOS 用户：无法打开 UVR？</summary>

> 由于 Apple 严格的应用程序安全性，您可能需要按照以下步骤操作才能打开 UVR。
>
> 首先，通过 Terminal.app 运行以下命令以允许从所有来源运行应用程序(建议在 UVR 正常打开后重新启用此限制)
> 
> ```bash
> sudo spctl --master-disable
> ```
> 
> 其次，运行以下命令以绕过公证: 
> 
> ```bash
> sudo xattr -rd com.apple.quarantine /Applications/Ultimate\ Vocal\ Remover.app
> ```

</details>

<details id="MacInstall">
  <summary>MacOS 手动安装说明</summary>

### MacOS 手动安装

- 在[这里](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip)下载并保存此仓库
- 在[这里](https://www.python.org/ftp/python/3.10.9/python-3.10.9-macos11.pkg)下载并安装 Python 3.10
- 在保存的目录中运行以下命令 - 

```
pip3 install -r requirements.txt
```

- 如果您使用的是 M1 Mac，请接着运行以下命令。如果不是，请跳过此步骤。 - 

```
cp /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/_soundfile_data/libsndfile_arm64.dylib /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/_soundfile_data/libsndfile.dylib
```

**FFmpeg 安装**

- 安装完成后，在[这里](http://www.osxexperts.net)下载适合您系统的 FFmpeg 二进制文件，并将其放入主应用程序目录。

**Rubber Band 安装**

要使用时间拉伸或音高变更工具，您需要安装 Rubber Band。

- 在[这里](https://breakfastquay.com/files/releases/rubberband-3.1.2-gpl-executable-windows.zip)下载预编译版本
- 从压缩包中，将以下文件解压到 UVR/lib_v5 应用程序目录:
   - ```rubberband-3.1.2-gpl-executable-macos/rubberband```

此过程已在 MacBook Pro 2021 (使用 M1) 和 MacBook Air 2017 上测试，并确认可用。

</details>

### Linux 安装（更新说明）

<details id="LinuxInstall">
  <summary>查看 Linux 安装说明</summary>

<br />

**这些安装说明适用于基于 Debian 和 Arch 的 Linux 系统。**

---

#### **步骤 1: 下载仓库**
- 从 [GitHub](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip) 下载并保存此仓库。
- 将下载的文件解压到您选择的目录。

---

#### **步骤 2: 安装依赖**
根据您的系统类型使用以下命令：

**对于基于 Debian 的系统 (Ubuntu, Mint 等)：**
```bash
sudo apt update && sudo apt upgrade
sudo apt-get install -y ffmpeg python3-pip python3-tk
```

**对于基于 Arch 的系统 (EndeavourOS)：**
```bash
sudo pacman -Syu
sudo pacman -S ffmpeg python-pip tk
```

---

#### **步骤 3: 设置虚拟环境（推荐）**
设置虚拟环境(venv)可确保程序的依赖项不会与系统范围的 Python 包发生冲突。

1. **导航到解压的仓库目录：**
   ```bash
   cd /path/to/ultimatevocalremovergui
   ```

2. **创建虚拟环境：**
   ```bash
   python3 -m venv venv
   ```

3. **激活虚拟环境：**
   - 对于 **基于 Debian 和 Arch 的系统：**
     ```bash
     source venv/bin/activate
     ```

4. **在虚拟环境中安装依赖：**
   ```bash
   pip install -r requirements.txt
   ```

---

#### **步骤 4: 运行应用程序**
在虚拟环境激活的情况下，启动应用程序：
```bash
python UVR.py
```

---

#### **重要说明**
1. **避免修改系统文件：**  
   之前的说明建议删除 `/usr/lib/python3.11/EXTERNALLY-MANAGED` 文件，这是危险的，可能会破坏 Python 包管理。请**不要**删除此文件。

2. **为什么使用虚拟环境？**  
   虚拟环境可以隔离程序的依赖项，防止与系统 Python 包发生冲突。更多信息请参见[这里](https://stackoverflow.com/questions/75602063/pip-install-r-requirements-txt-is-failing-this-environment-is-externally-mana/75696359#75696359)。

3. **已知问题和讨论：**  
   - [问题 #1578](https://github.com/Anjok07/ultimatevocalremovergui/issues/1578)  
   - [拉取请求 #1068](https://github.com/Anjok07/ultimatevocalremovergui/pull/1068)

---

如果遇到问题，请参考 [GitHub Issues](https://github.com/Anjok07/ultimatevocalremovergui/issues) 页面寻求帮助。

</details>

### 其他应用说明
- Nvidia GTX 1060 6GB 是 GPU 转换的最低要求。
- Nvidia GPUs 至少需要 8GBs 的 V-RAM。
- AMD Radeon GPU 支持有限。
   - 目前有一个针对 AMD GPU 用户的分支工作正在进行中，请参见[这里](https://github.com/Anjok07/ultimatevocalremovergui/tree/v5.6-amd-gpu)
- 此应用程序仅兼容 64 位平台。
- 此应用程序依赖于 Rubber Band 库来处理时间拉伸和音高变化选项。
- 此应用程序依赖于 FFmpeg 来处理非 wav 音频文件。
- 应用程序将自动记住您的设置，当关闭应用程序时。
- 转换时间将显著依赖于您的硬件。
- 这些模型是计算密集型的。

### 性能：
- 模型加载时间更快。
- 导入/导出音频文件更快。

## 故障排除

### 常见问题

- 如果 FFmpeg 未安装，应用程序将在用户尝试转换非 WAV 文件时抛出错误。
- 内存分配错误通常可以通过降低 "Segment" 或 "Window" 大小来解决。

#### MacOS Sonoma 左键点击问题
在 MacOS Sonoma 上存在一个已知问题，即应用程序内的左键点击无法正常工作。这个问题影响了所有在 Sonoma 上使用 Tkinter 构建的应用程序，现已解决。如果您仍然遇到问题，请通过以下链接下载最新版本 - [链接](https://github.com/Anjok07/ultimatevocalremovergui/releases/tag/v5.6)

此问题的跟踪记录在[这里](https://github.com/Anjok07/ultimatevocalremovergui/issues/840)。

### 问题报告

在提交新问题时，请尽可能详细地描述。

如果可能，请点击"开始处理"按钮左侧的"设置按钮"，然后点击"错误日志"按钮，获取可以提供给我们的详细错误信息。

## 许可证

**Ultimate Vocal Remover GUI** 代码采用 [MIT 许可证](LICENSE)。

- **请注意：** 对于所有希望使用我们模型的第三方应用程序开发者，请遵守 MIT 许可证，为 UVR 及其开发者提供适当的信用。

## 致谢
- [ZFTurbo](https://github.com/ZFTurbo) - 创建并训练了新的 MDX23C 模型权重。
- [DilanBoskan](https://github.com/DilanBoskan) - 您在项目初期的贡献对 UVR 的成功至关重要。感谢您！
- [Bas Curtiz](https://www.youtube.com/user/bascurtiz) - 设计了官方 UVR 标志、图标、横幅和启动画面。
- [tsurumeso](https://github.com/tsurumeso) - 开发了原始 VR 架构代码。
- [Kuielab & Woosung Choi](https://github.com/kuielab) - 开发了原始 MDX-Net AI 代码。
- [Adefossez & Demucs](https://github.com/facebookresearch/demucs) - 开发了原始 Demucs AI 代码。
- [KimberleyJSN](https://github.com/KimberleyJensen) - 为 MDX-Net 和 Demucs 的训练脚本实现提供建议和帮助。感谢您！
- [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) - 帮助在 MDX-Net AI 代码中实现分块。感谢您！

## 贡献

- 对于任何对 **Ultimate Vocal Remover GUI** 的持续开发感兴趣的人，请向我们发送拉取请求，我们会进行审查。
- 本项目完全开源，任何人都可以免费使用和修改。
- 我们只维护 **Ultimate Vocal Remover GUI** 和提供的模型的开发和支持。

## 参考文献
- [1] Takahashi 等人，"用于音频源分离的多尺度多频带 DenseNets"，https://arxiv.org/pdf/1706.09588.pdf
