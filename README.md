<h1 align="center">fuck_cqooc</h1>

![GitHub](https://img.shields.io/github/license/Fatpandac/fuck_cqooc)  ![GitHub all releases](https://img.shields.io/github/downloads/Fatpandac/fuck_cqooc/total)  ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Fatpandac/fuck_cqooc?include_prereleases)  [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Fatpandac/fuck_cqooc/master.svg)](https://results.pre-commit.ci/latest/github/Fatpandac/fuck_cqooc/master)

<details>
<summary>这是一个简单的 「cqooc」(http://www.cqooc.com) 刷课工具。</summary>

> 🥁 We don't need no education
>
> 🎹 We don't need no thought control
>
> 🎸 No dark sarcasm in the classroom
>
> 🎙️ Teacher, leave those kids alone
</details>

## 使用方法

1. 安装
    - 源码
    下载源码后运行`pip install -r requirements.txt` 或运行 Python 虚拟环境运行 `pipenv install`,之后再双击打开`fuck_cqooc.pyw`。
    - 二进制文件
    对于 Windows/Mac 系统用户，你还可以选择使用编译好的文件，[在这下载](https://github.com/Fatpandac/fuck_cqooc/releases)。
2. 启动程序
    - 等待程序启动。进入登陆界面之后，输入你的重庆高校在线课程平台的用户名和密码，点击登录。
3. 选择课程
    - 登录成功进入主界面之后，左侧列表中将会展示你的课程列表。选取其中一个课程，右侧列表中将会展示该课程的任务列表。
4. 开始运行程序
    - 选取一个或多个任务并将其勾选。选择完成之后，点击右下方的"fuck"按钮，开始跳过选中的任务。完成之后，任务列表将会自动刷新。

## 常见问题

- 我的用户名和密码没错，但我不能登录?

这种情况可能的原因是，程序的登录请求被服务器拒绝。
这种情况下，你需要在浏览器中打开重庆高校在线课程平台，手动完成一次登录，然后回到程序中，再尝试重新登录。

- 跳过任务花费的时间特别长，这是为什么?

这是因为重庆高校在线课程平台服务器的管控策略。短时间跳过太多任务，你可能会遭到网站临时屏蔽。屏蔽不会持续太久，不到一分钟就会解除。
但为了保证所有任务都能成功跳过，程序设置跳过每个任务之间都会间隔一段时间，具体是30秒。

## Special Thanks

<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains Logo (Main) logo." width="168">
