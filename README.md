[**🇨🇳中文**](https://github.com/shibing624/ChatPilot/blob/main/README.md) | [**🌐English**](https://github.com/shibing624/ChatPilot/blob/main/README_EN.md) | [**📖文档/Docs**](https://github.com/shibing624/ChatPilot/wiki) | [**🤖模型/Models**](https://huggingface.co/shibing624) 

<div align="center">
  <a href="https://github.com/shibing624/ChatPilot">
    <img src="https://github.com/shibing624/ChatPilot/blob/main/docs/favicon.png" height="150" alt="Logo">
  </a>
</div>

-----------------

# ChatPilot: Chat Agent
[![PyPI version](https://badge.fury.io/py/ChatPilot.svg)](https://badge.fury.io/py/ChatPilot)
[![Downloads](https://static.pepy.tech/badge/ChatPilot)](https://pepy.tech/project/ChatPilot)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![python_version](https://img.shields.io/badge/Python-3.9%2B-green.svg)](requirements.txt)
[![GitHub issues](https://img.shields.io/github/issues/shibing624/ChatPilot.svg)](https://github.com/shibing624/ChatPilot/issues)
[![Wechat Group](https://img.shields.io/badge/wechat-group-green.svg?logo=wechat)](#Contact)


**ChatPilot**: Chat with Agent. 基于chat agent实现了联网搜索，文件、网址对话功能（类kimi chat，文件，拖进来；网址，发出来），支持OpenAI API。


## Features

- 本项目基于Agent实现了搜索问答
- 本项目基于Agent实现了文件对话(RAG)，实现了通过URL自动解析内容功能，复现了 kimi chat(文件，拖进来；网址，发出来) 的文件、网址对话功能
- 本项目基于Agent实现了python代码解释器，支持E2B虚拟环境和本地python编译器环境运行代码
- 支持前后端服务分离，前端使用Svelte，后端使用FastAPI
- 支持语音输入输出，支持图像生成
- 支持用户管理，权限控制，支持聊天记录导入导出

## Demo

Official Demo: https://chat.mulanai.com

HuggingFace Demo: https://huggingface.co/spaces/shibing624/ChatPilot

![](https://github.com/shibing624/ChatPilot/blob/main/docs/hf.png)

## Install
```shell
pip install -U chatpilot
```

or

```shell
git clone https://github.com/shibing624/ChatPilot.git
cd ChatPilot
pip install -e .
```


## Usage

### 1. 构建前端web

两种方法构建前端：
1. 下载打包并编译好的前端 [buid.zip](https://github.com/shibing624/ChatPilot/releases/download/v0.0.2/build.zip) 解压到项目web目录下。
2. 自己使用npm构建前端

Requirements:

- 🐰 [Node.js](https://nodejs.org/en) >= 20.10 or [Bun](https://bun.sh) >= 1.0.21
- 🐍 [Python](https://python.org) >= 3.9

```sh
git clone https://github.com/shibing624/ChatPilot.git
cd ChatPilot/

# Copying required .env file
cp .env.example .env

# Building Frontend Using Node
cd web
npm install
npm run build
```
输出：项目`web`目录产出`build`文件夹，包含了前端编译输出文件。

### 2. 启动后端服务

```shell
cd ..
pip install -r requirements.txt -U
bash start.sh
```
好了，现在你的应用正在运行：http://0.0.0.0:8080 Enjoy! 😄


## Contact

- Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/ChatPilot.svg)](https://github.com/shibing624/ChatPilot/issues)
- 邮件我：xuming: xuming624@qq.com
- 微信我：加我*微信号：xuming624, 备注：姓名-公司-NLP* 进NLP交流群。

<img src="docs/wechat.jpeg" width="200" />


## Citation

如果你在研究中使用了ChatPilot，请按如下格式引用：

APA:
```latex
Xu, M. ChatPilot: LLM agent toolkit (Version 0.0.2) [Computer software]. https://github.com/shibing624/ChatPilot
```

BibTeX:
```latex
@misc{ChatPilot,
  author = {Ming Xu},
  title = {ChatPilot: llm agent},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/shibing624/ChatPilot}},
}
```

## License


授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加ChatPilot的链接和授权协议。


## Contribute
项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：

 - 在`tests`添加相应的单元测试
 - 使用`python -m pytest -v`来运行所有单元测试，确保所有单测都是通过的

之后即可提交PR。

## Reference

- [Open WebUI](https://github.com/shibing624/ChatPilot)
- [langchain-ai/langchain](https://github.com/langchain-ai/langchain)