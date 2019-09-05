# lektor-qiniu Lektor CMS  七牛云插件





本插件让你在Lektor CMS里，一键部署网站项目到七牛云空间.

## 主要功能

1. 一键部署网站项目到七牛云空间

2. 一键部署网站项目到七牛云空间文件夹

3. 设置排除文件夹和文件，上传时将忽略这些

4. 自动更新CDN缓存
   
   



## 准备工作

既然是七牛云插件，顾名思义，你得先有个七牛云空间； 没有的话可以点此注册：

——》    [`七牛云官网`](https://portal.qiniu.com/signup?code=1hltq2pevt7bm) 



**注意，本插件没有附带任何七牛云注册和管理bucket的功能**，将来也许会添加进去，但目前没这计划，说实话也没必要。



你需要自己去注册并建立空间，具体可以参考七牛云文档。



同时你应该会使用Lektor CMS， 这是一个静态网页生成器，目前来说是我用过的最好的此类工具之一。



## 安装插件

在Lektor CMS里安装插件非常简单， 在项目终端下，输入：

```console

lektor plugins add lektor-qiniu
```

Lektor 就会自动帮你把插件装好， 当然装好不等于可以立刻使用，还需要一点点的设置。 



## 使用说明

插件安装完毕后， 在项目的.lektorproject 文件里，应该自动增加了这么一行：

```ini

[packages]

lektor-qiniu= 0.1.2
```

在这一段下面，添加一个发布服务器，代码如下：

```ini

[servers.qiniu]

name = qiniu

enabled = yes

target = qiniu://<YOUR-BUCKET>
```

解释一下， 这是Lektor 的部署服务器的规定写法，具体意思可以查文档，这里你需要改的就只有 target那一行，**<YOUR-BUCKET>** 换成你自己的bucket名字即可。



假如你希望部署到bucket中的某一个文件夹，那么就在后面添加文件名：

```ini

[servers.qiniu]

name = qiniu

enabled = yes

target = qiniu://<YOUR-BUCKET>/<NAME-OF-FOLDER>
```

举个栗子， 如果你希望部署网站到名为 "abcde"的bucket,  文件夹为 "fjhi", 那么你可以这么写：

```ini

[servers.qiniu]

name = qiniu

enabled = yes

target = qiniu://abcde/fjhi
```



保存之后，你就可以在Lektor 后台的部署键里面，看到这个部署服务器了。



## 配置文件

在正式运行之前，你需要把自己的七牛云配置设置好。



在项目根文件下有一个**configs** 文件夹， 这个是Lektor用来保存所有插件的配置文件， 如果没有找到这个文件夹，那么你需要自己新建这个文件夹。



在**configs**文件夹里，新建一个名为**qiniu.ini**的配置文件，注意不要用其它名字，否则会报错。



配置文件内容如下，你也可以从本项目的sample_config文件夹里复制：

```ini

[auth]

Access_Key = replace_with_your_own_AK

Secret_Key = replace_with_your_won_SK



[cdn]

refresh_enable = yes

refresh_url = https://www.your-own-site.com/



[exclusions]

dirs = .lektor

files =
```

具体解释如下：

#### 认证信息

 **auth** 字段保存七牛云的认证信息，你需要自行获得Access_Key 和Secret_Key； 拿到后填入即可。

#### 更新CDN缓存

七牛云是自带CDN的，但有个不足是起CDN缓存不会即时更新，因此bucket内容改变之后，需要你手动去CDN里面更新预缓存。



本插件就添加了自带更新CDN的功能， 在**cdn**字段里，把 **refresh_enable** 设置为 **yes** ，然后把 **refresh_url** 设置为你需要更新的目录名，通常是你网站根目录的地址；设置完毕后，每次部署后，系统会自动帮你把CDN缓存更新，是不是很爽啊？ 

#### 排除上传文件夹和文件

有些文件夹或者文件你不是很想上传，比如我项目中的assets文件夹， 里面很多初始化的图片和静态文件，第一次上传之后，后续用不着每次都重新上传，那么可以在**exclusions**字段里面设置， **dir**是设置文件夹，**files**设置文件，中间用英文的','逗号隔开。

```ini

[exclusions]

dirs = .lektor, dir1, dir2

files = file1, file2,file3
```

特别需要注意的是 **.lektor** 文件夹, Lektor 官方建议排除这个文件夹，因此建议你保留这一项，除非你有其它想法.

### 关于 Lektor CMS

Lektor CMS 目前是我最喜欢的静态网站工具之一， 以下是一些我用Lektor 制作的网站，限于工作原因暂时不能把它们开源，以后有机会会考虑。

[`新风网`](https://www.xinfengtv.com)

[`Intersonic Group`](https://www.intersonicgroup.com)

[`F&S Always Auto Parts`](https://www.fnsalways.com)

[`THEORING Seal Rings`](https://theoring.com)

[`THORING 密封圈`](https://www.theoring.com)



如果你觉的不错，强烈推荐你试试Lektor， 官网： [`Lektor CMS Official Site`](https://www.getlektor.com)
