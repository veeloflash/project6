# 大项目第6周作业

## 任务说明

本项目实现了一个基于西班牙语关键词的用户状态检测模块，用于识别学习过程中的四种主要困难状态：

- `cannot_start`：不会开始
- `concept_confusion`：不理解概念
- `stuck_on_step`：卡步骤
- `expression_difficulty`：表达困难

## 运行方式

1. 安装依赖（可选，默认纯 Python 无额外依赖）：
   ```bash
   python -m pip install -r requirements.txt
   ```
2. 运行主程序：
   ```bash
   python main.py
   ```
3. 输入 `exit` 或 `quit` 退出程序。

## 核心逻辑

- 将关键词配置存放在 `state_keywords.json`，便于后续维护。
- `detect_state(text)` 返回一个包含：
  - `primary_state`：最优先处理的主状态
  - `matched_states`：所匹配到的所有状态
  - 当输入为空或无匹配时，返回错误说明。

## 测试

运行测试：

```bash
python -m pytest
```

测试覆盖了：

- 空输入验证
- 四种状态识别
- 多状态输入优先级
- 无关文本返回无状态
- 关键词配置文件存在性检查

## 已知限制

- 当前匹配为基于关键词的简单规则，不包含机器学习。
- 真实问卷场景中可能需要更丰富的语料覆盖和上下文理解。
- 如果一个输入同时匹配多种状态，当前按严格优先级返回主状态。

## 第7周接入建议

后续可将 `detect_state()` 的返回结构接入 `decide_action(state)`：

```python
result = detect_state(user_input)
if "primary_state" in result:
    next_action = decide_action(result["primary_state"])
```
