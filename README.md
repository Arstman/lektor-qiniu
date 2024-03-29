# lektor-qiniu  Lektor CMS 七牛云插件

lektor-qiniu is a plugin to deploy your lektor site to a qiniu cloud bucket.

[简体中文说明](https://github.com/Arstman/lektor-qiniu/blob/master/README-CN.md)

## Main Features

1. deploy your site to your qiniu bucket
2. deploy your site to a folder in a qiniu bucket
3. exclude files and directories from deployment.
4. refresh your qiniu cdn.

## Before Installation

You may need a bucket from qiniu cloud to deploy your lektor project. Qiniu Cloud provides 10GB storage and cdn for free, that should be enough for most small projects.

Go to [`QINIU Cloud`](https://portal.qiniu.com/signup?code=1hltq2pevt7bm) for more details.

 **This plugin does not do anything to help you create or configure qiniu account or bucket.**  You will have to make it done by yourself. 

## Installation

There ways to install plugin in Lektor, the easy ways is run below command in your project.

```console
lektor plugins add lektor-qiniu
```

Press Enter and lektor will automatically download and install this plugin for you.

## Usage

After Installation, open your lektorproject file, first it should have a section like this:

```ini
[packages]
lektor-qiniu= 0.1.3
```

then below this section, you need add your bucket and folder(optional) as a target of a deploy server, like this:

```ini
[servers.qiniu]
name = qiniu
enabled = yes
target = qiniu://<YOUR-BUCKET>
```

or if you want deploy your site to a folder in a bucket, mostly for backups, you can add server section as below:

```ini
[servers.qiniu]
name = qiniu
enabled = yes
target = qiniu://<YOUR-BUCKET>/<NAME-OF-FOLDER>
```

for example, if you want to deploy your site to a bucket name "abcde", folder "fjhi", you will need to add a server section as below:

```ini
[servers.qiniu]
name = qiniu
enabled = yes
target = qiniu://abcde/fjhi
```

after this you should see a server shows when you push the deploy button in your Lektor Admin Dashboard.

but still you will need just 5 minutes to configure this plugin to make it works.

## Configuration

After setup your target server, you need to configure the plugin to make it works.

Go to your project's configs folder, which should be in root directory of your project. this folder is where Lektor keep the configuration files of all plugins. If you can't find any **configs** folder in your project's root directory, you need create it.

In configs folder, create a configuration file exactly named **qiniu.ini**.

#### Attention: DO NOT name the configuration file with other names, otherwise this plugin will not work properly.

In this configuration file, you will need add few more sections, you can copy a sample configuration ini file from the sample_config folder, it looks like this:

```ini
[auth]
Access_Key = replace_with_your_own_AK
Secret_Key = replace_with_your_won_SK

[cdn]
refresh_enable =  yes
refresh_url = https://www.your-own-site.com/

[exclusions]
dirs = .lektor
files =  
```

#### Credentials

You need to get your own Access Key and Secret Key from Qiniu Admin Dashboard, and put them in the **auth**  section.

#### Refresh cdn cache

mostly, Qiniu provides a free(with limitations) cdn for your bucket site, after you update your bucket file, the cdn wouldn't update automatically, therefore you will need to refresh your bucket site's directory (via your site's root url), for more details you can check Qiniu's documentation.

fortunately, you don't need to do refresh manually, you can just set the **refresh_enable** to **yes** in your **cdn** section, and change the refresh_url to your site's root url. this plugin will automatically refresh your cdn site after all files are uploaded.

#### exclusions

Another function this plugin provides is exclude folders or files you want to upload during deployment. 

To exclude files or folders, just put the name of the folders or files in the **exclusions** section of configuration file, separated each one with commas. 

```ini
[exclusions]
dirs = .lektor, dir1, dir2
files =  file1, file2,file3
```

One special folder here is **.lektor**, which Lektor officially suggests that this folder should be exclude during deployment, therefore you should keep at least this one, unless you have other needs for this folder.

### About Lektor CMS

Lektor CMS is one of my favorite static website generators, I have use this in production for several projects, you can see some of my sites as below:

[`新风网`](https://www.xinfengtv.com) 
[`Intersonic Group`](https://www.intersonicgroup.com) 
[`F&S Always Auto Parts`](https://www.fnsalways.com) 
[`THEORING Seal Rings`](https://theoring.com) 
[`THORING 密封圈`](https://www.theoring.com) 

Looks pretty good, right? Thanks for lektor, you can try this best Static CMS as well via [`Lektor CMS Official Site`](https://www.getlektor.com) 
