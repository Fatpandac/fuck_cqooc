# fuck_cqooc [![sync -> gitee](https://github.com/Fatpandac/fuck_cqooc/actions/workflows/sync-to-gitee.yml/badge.svg?branch=master&event=push)](https://github.com/Fatpandac/fuck_cqooc/actions/workflows/sync-to-gitee.yml)

<details>
<summary>这是一个简单的 <a hraf="http://www.cqooc.com">cqooc 刷课工具。</a></summary>

> 🥁 We don't need no education
>
> 🎹 We don't need no thought control
>
> 🎸 No dark sarcasm in the classroom
>
> 🎙️ Teacher, leave those kids alone
</details>

## [Core 的样例](./sample.py)

只需要运行 `python3 sample.py` 它将会告诉你 Core 的运行方式。

## 使用方法

1. 安装
    - 源码
    下载源码后运行`pip install -r requirements.txt` 或运行 Python 虚拟环境运行 `pipenv install`,之后再双击打开`fuck_cqooc.pyw`。
    - 二进制文件
    对于 Windows 系统用户，你还可以选择使用exe文件，[在这下载](https://github.com/Fatpandac/fuck_cqooc/releases)。
2. 启动程序
    - 等待程序启动。进入登陆界面之后，输入你的重庆高校在线课程平台的用户名和密码，点击登录。
3. 选择课程
    - 登录成功进入主界面之后，左侧列表中将会展示你的课程列表。选取其中一个课程，右侧列表中将会展示该课程的任务列表。
4. 开始运行程序
    - 选取一个或多个任务并将其勾选。选择完成之后，点击右下方的"fuck"按钮，开始跳过选中的任务。完成之后，任务列表将会自动刷新。

## 常见问题

- 我的用户名和密码没错，但我不能登录

这种情况可能的原因是，程序的登录请求被服务器拒绝。
这种情况下，你需要在浏览器中打开重庆高校在线课程平台，手动完成一次登录，然后回到程序中，再尝试重新登录。

- 跳过任务花费的时间特别长，这是为什么

这是因为重庆高校在线课程平台服务器的管控策略。短时间跳过太多任务，你可能会遭到网站临时屏蔽。屏蔽不会持续太久，不到一分钟就会解除。
但为了保证所有任务都能成功跳过，程序设置跳过每个任务之间都会间隔一段时间，具体是30秒。

- 跳过的过程中按钮没有反应

为了防止反复多次跳过任务，执行任务期间，程序会阻止按钮的点击，直到任务完成。
如果程序进入无响应状态，跳过任务仍然在进行，请不要尝试关闭程序。
