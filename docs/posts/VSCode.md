---
date:
    created: 2025-02-01
tags:
  - Tool
---
VSCode configurations.
<!-- more -->

# 0. Installation
1. Install
2. After installing,  right click desktop link > properties, paste`"<VSCODE_INSTALL_DIRECTORY>\VS code\Code.exe" --extensions-dir "<DESIRED_EXTENSION_PATH>"`
3. when you launch vscode from the desktop link, you can install or load extensions in the `<DESIRED_EXTENSION_PATH>`
# 1. Config
## 1.1 Environ variable
Environment variables that can be used in `launch.json`

| VAR                     | Role                                                       |
| ----------------------- | ---------------------------------------------------------- |
| cwd                     | the task runner's current working directory on startup     |
| workspaceFolder         | absolute path of current open folder in workspace          |
| workspaceRootFolderName | folder name of current open folder in workspace            |
| relativeFile            | path of current open file relative to `$workspaceFolder`   |
| file                    | absolute path of current open file                         |
| fileBasename            | file name of current open file                             |
| fileBasenameNoExtension | file name of current open file excluding the extension     |
| fileDirname             | absolute path of current open file excluding the file name |
| fileExtension           | extension of current open file                             |
| `env:<ENV_NAME>`        | value of `ENV_NAME`                                        |





## 2. Config files
- launch.json(debugger setting)
- settings.json
- tasks.json(config to test and build by vscode)

tasks.json(example:

```json
{
	"version": "2.0.0",
	"tasks": [
		{
			"label": "make clean",
			"command": "make",
			"type": "shell",
			"args": [
				"clean"
			],
			"options": {
                // cwd specify work path of current task to apply command
				"cwd": "${fileDirname}"
			},
			"group": "none"  // group value is one of "none", "build", "test"
		},
		{
			"label": "make lab3",
			"command": "make",
			"type": "shell",
			"args": [
				"lab3"
			],
			"options": {
				"cwd": "${fileDirname}"
			},
			"group": "build",
            // "dependsOn" means this task happen after the list of tasks
			"dependsOn": [
				"make clean"
			], 
            //display all the gcc warnings and errors in the problem pannel      
            //instead of in the terminal pannel
			"problemMatcher": "$gcc" 
		}
	]
}
```



# 2. Useful plugins

## 2.1 Remote - SSH
This plugin allows you to open folder on remote machines without download

### 2.1.1 Establish remote connection
1. Search and install "Remote - SSH" extension from vs code extensions market
2. `ctrl + shift + p`, type "remote", select "Connect Current window to Host"
3. Type `<USER_NAME>@<DOMAIN>`, then enter password, there you go

When you work in this environment, you can edit files or install extension on remote end



### 2.1.2 Config passwordless conn
see [[Linux#1.2.1 passwordless login]]

## 2.2 Remote Repositories
This plugin allows you to open github repo without cloning

1. Install **Remote Repositories**
2. **Ctrl + shift + p**, select **open remote repositories**
3. Type `<GITHUB_USER_NAME>/<REPO_NAME>` will open the repo

# 3. Sync settings
1. Sign in > Turn on Setting syncs
2. Select data for sync
3. Sign in with github

Once success,
1. ctrl+shift+p, select **show sync data**, will open **manage sync data** on left side pannel