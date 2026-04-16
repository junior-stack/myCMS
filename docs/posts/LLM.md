---
date:
    created: 2026-04-16
draft: true
tags:
  - Programming
---
My note about LLM framework
<!-- more -->

# 1. Relevant framework
LLM Frameworks:
- LlamaIndex/Ollama
- Langchain/LangGraph
- Google adk
- OpenAI sdk

Model Provider:
- Openrouter: purchase credit for a particular model
- Azure
- Gemini
- Groq
- OpenAI
- Ollama

Resources:
- copilot workflows: https://github.com/github/awesome-copilot

Tools:
- agenda: prompt management
- ralph: ai automation
- airbyte: context management
- agency swarm
- n8n

# 2. RAG Agent
Ref: Google search (how to make google adk agent expose API)

production Rag features: https://www.youtube.com/watch?v=AUQJ9eeP-Ls
agent evaluation, using MCP Tools, deploy on vertex engine: 
- https://www.youtube.com/watch?v=p0iMDGBMtrc
- https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_claude_with_adk_on_agent_engine.ipynb
adk + nextjs: https://www.youtube.com/watch?v=tX_DdvwRync
UI For adk agent:
- https://www.youtube.com/watch?v=y7damsm8Qos
- https://www.youtube.com/watch?v=sabu9gRFflM
- https://www.youtube.com/watch?v=jrFFEPWoB1Q



# 3. MCP & Skill
## 3.1 MCP

Summary of what MCP of a coding agent can do:
- interact with external database
- query documentation within mcp server(context 7)
- 

MCP Markets:
- glama.ai
- smithery.ai
- cursor.directory
- lmsystems.ai


Useful MCPs:
- AgentDesk/BrowserTools: give cursor access to browser console logs
- firecrawl: turn websites to LLM-ready data(index online docs)
- Sequential thinking
- Puppeteer: browser automation & web scraping
- Brave Search: web & local search
- `context7.com`: up-to-date online docs for LLM
- supabase: interact with postgresql cloud platform
- Playwright: open browser, click links, screenshot, browser UX reviewer agent

MCP Transport type:
- `stdio`: communicate locally via `stdout`
- `sse`: communicate locally or remotely via Http endpoint

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP()

mcp.run(transport="stdio") # or sse
```

~~~tabs
---tab Agent
Integrate MCP server to AI agents(using cursor):
1. add the `.cursorrule`(https://github.com/VRSEN/agency-swarm/blob/main/.cursorrules) into the repo
2. Go to cursor chat: `I want to build an agent that <agent_purpose>`, cursor will ask you details according to the `.cursorrule` to generate a `prd.txt`
3. Provide the link of the MCP server you are going to integrate with and the doc link of MCP Server for agency swarm, cursor will generate agent code files
---tab cursor
How to integrate MCP to cursor:
4. Go to https://smithery.ai/ and type `sequential thinking`
5. Click `Sequential Thinking`, in the webpage, select cursor and click the "One-Click Install" button, which redirect you to cursor
6. click install in the cursor Setting in cursor, this will result the following changes  in `%USERPROFILE%\.cursor\mcp.json`(or you can also install in project scope by applying the changes in `<project_dir>/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "Sequential Thinking": {
      "type": "http",
      "url": "https://server.smithery.ai/@smithery-ai/server-sequential-thinking",
      "headers": {}
    }
  }
}
```
---tab Claude code
Example(with context 7):
Remote:
- `claude mcp add --transport http context7 --scope project https://mcp.context7.com/mcp`
- `claude mcp add --transport sse context7 --scope project https://mcp.context7.com/sse`
Local:
- `claude mcp add context7 -- npx -y @upstash/context7-mcp`

~~~








# 4. A2A

# 5. AI Coding workflow

AI coding agents:
- cline
- codex
- cursor(built from vs code & support vs code extensions)
- windsurf(similar to cursor, belong to jetbrain)
- copilot(vs code)
- claude code
- antigravity


## 5.1 Basics
Terminology:
- context window: comprise of input(system prompt + user prompt) and output token

How to check how full is a context window(claude code):
> use `/context` can help you find out. Use `/compact` to summarize the context and truncate the used context in context window.

Work modes of AI: AI coding is inefficient and often fails when planning and executing at the same time. It would be better if planning and executor modes are separate:
- Plan: Describe changes, coding agent ask questions in iterative Q/A and creates `planning.md` at the end to list instructons and tasks
- Executor: Execute `planning.md`

Claude code commands:
- `claude --dangerously-skip-permissions`

agentic workflow folders:
> .cursor/
> > rules/
> > > ARD.mdc: architecture decision records
> > > PRD.mdc
> > > workflow.mdc
> > > folder-structure.mdc
> > 
> > agents.mdc
> > .cursorrules: define the context & instructions for AI models


## 5.2 workflow for general start-up

Plan phase(`PRD.mdc`: https://github.com/agency-ai-solutions/nextjs-firebase-ai-coding-template/blob/main/.cursor/rules/PRD.mdc)
1. Select `gpt-5` as the model and choose `plan` mode, ask the coding agent `Ask me questions until you have enough context to fill out @PRD.mdc`
2. Descibe and answer the LLM's questions, then ask the coding agent: `Do you have any followup questions?`
3. After answering all of the questions, type: `Now draft the PRD.mdc`
4. type `break down the PRD into separate tasks @task-template.mdc`
5. type `Please scope types for each request, response and database models inside each task` to list the properties and methods of project classes in the `<task_name>.mdc`

Execution Phase:
1. select the model to be `claude-4-sonnet` and the work mode to be `agent`, type `IMPLEMENT @<taskname>.mdc` until all tasks are executed
2. For a specific `<tastname>.mdc` agent window, add real data to corresponding project folder and prompt the model : `I added <real_data_filename> in <test_folder_name>. Test it with a real integration test`
3. Final step: let the code agent document key decisions: `Document all key decisions in @ARD.mdc`

youtube: https://www.youtube.com/watch?v=3myosgzKvZ0
- github: https://github.com/agency-ai-solutions/nextjs-firebase-ai-coding-template
## 5.3 Parallel agents execution

medium: https://carlrannaberg.medium.com/my-current-ai-coding-workflow-f6bdc449df7f

## 5.4 Cloud code agent
Summary:
> - Github cloud code agent can be assigned issues and create PR on their own
> - 

Github copilot agent: https://www.youtube.com/watch?v=R9KSJ0Vfy8I
Claude code:




# 6. Coding Agent
## 6.1 Github Copilot

### 6.1.1 Context Tools
Go to Chat Window > Add Context > Tools, then select a tool

## 6.2 Claude
### 6.2.1 Login
Terminal:
1. After installing through `npm`, launch claude in terminal through `npx claude`
2. You can log in through: Claude account with subscription   or Anthropic Console account(no subscription plan)
	- Anthropic Console account: after authorizing in browser, go to the terminal and see "login successful and press enter to continue". Then press enter to continue until you can see welcome. (API usage billing dashboard: https://platform.claude.com/settings/billing)

VS code:
1. Install Claude code from vs code extension market, 
2. Then log in by `ctrl + shift + p`, open claude code in new tab and login methods are the same as above

### 6.2.2 Pricing
Anthropic Console account(https://platform.claude.com/docs/en/about-claude/pricing):
- pay-as-you-go model, purchase at least 5 US dollar pre-paid credits
- **Token costs:** Cost $3.00 per million input tokens ($6.00/MTok if context >200K), cost $15.00 per million output tokens ($22.50/MTok if context >200K).
- **Code execution:**  1,550 free hours/month, then $0.05/hour.
- On avg 6 USD per day for a user

### 6.2.3 Claude markdown
`Claude.md`:
- create `claude.md`
1. For a project, type `init` will create a `Claude.md` as the project codebase context:
	- if the project is existing, claude will explore and analyze the source code
	- if it is a newly created project, claude will ask questions and user's answers will be used to fill the `Claude.md`
- add custom instructions to `claude.md`:
1. add `#` before the instruction in console, the instruction will be added at the bottom of the development Notes of the `claude.md`

### 6.2.4 Context management
how to keep context clean after context window is full:
- `/exit` or `/clear`: clear the current session context and start a new session
- `/compact`: compact the chat context into summary
- `esc` twice: display previous point in chat & rewind to a previous point in the session

how to check how full the context window is:
- `/context`: display current token usage, available tokens, & breakdown
- `/statusline`: display the percentage of the context window being used

resume to previous chat window:
- `/resume`: display list of chats to be selected to be resumed

### 6.2.5 Tools & commands
Built-in tools list: https://code.claude.com/docs/en/settings#tools-available-to-claude

Defining a customized commands:
1. Create a `<taskname>.md` file under the directory of `.claude/commands`
```md
---
argument-hint: <arg1> | <arg2>
---
## Context
Parse $ARGUMENTS to get the following values:

- [var1]: <arg1> from $ARGUMENTS
- [var2]: <arg2> from $ARGUMENTS
  
## Task
Do the task according to [var1] and [var2] provided

## Step-by-step implementation

## Expected outcome

## Testing & Verification

## Extra guideline
```
2. Restart claude and type command `/<taskname>` will invoke this command and coding agent may ask questions, or you can also provide more details by  providing arguments`/<taskname> <task_name> | <detail>`

### 6.2.6 Subagent
list agents: `/agents` and can prompt create new agent

agents can be created by claude code:
- Code reviewer
- Code Simplifier
- Security Reviewer
- UX Reviewer

Creating a UX Reviewer agent:
1. Describe what this agent do:
	> Expert UI & UX engineer who reviews UI & UX of React component in a browser using Playwright, takes screenshot, then offers feedback on how to improve components in terms of visual design, user experience and accessibility
2. Checking the tools the agent can access will create an agent in `.claude/agents`(Recommended `playwright` tool in MCP tool sets)

### 6.2.7 Github
Summary: by setting up the github workflow, we can:
- assign issues to claude code and let it create pr to resolve
- auto-review PR and let claude code provide comments

Steps to setup claude code github:
1. install github cli
2. `gh auth login`
3. in claude code: `/install-github-app`

## 6.3 Cursor
common commands:
- `@docs`: select a doc site or add docs as context
- `@web`: add site as context



# 6. Agent pipeline
Tools for each stage of pipeline:
- Retrieve information
	- Internal system
		- Zenesk(customer support agent)
		- Slack
		- Notion



# 7. Context Engineering
coding workflow: https://github.com/VRSEN/context-engeineering-advanced-techniques/blob/main/.cursor/rules/workflow.md

context engineering: https://www.youtube.com/watch?v=BkfLE6gMmM4

## 7.1 Agent observability
https://www.youtube.com/watch?v=-bx_aKdIthw


# 8. Workflow template for project types

## 8.1 workflow for develop agent
Workflow for developing agents:
- https://github.com/VRSEN/mcp-code-exec-agent/blob/main/.cursor/rules/workflow.mdc

# 8. Useful prompts


